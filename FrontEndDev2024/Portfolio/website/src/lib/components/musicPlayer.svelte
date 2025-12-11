<script lang="ts">
	import './musicPlayer.css';
	import { onMount } from 'svelte';
	import { parseBlob, type IAudioMetadata } from 'music-metadata';
	import { user_data, player_data } from '$lib/shared.svelte';
	import { load_song, fetch_song, next_song, prev_song, skip_ahead } from '$lib/song_api';
	import { DatabaseControl, cache_control, sec_to_min, shuffler } from '$lib/utils';
	import { logger, other_loading } from '$lib/store';
	import { is_mobile } from '$lib/store';

	let audio = $state() as HTMLAudioElement;
	let current_time = $state() as number;
	let current_time_display = $state() as string;
	let duration = $state() as number;
	let played_side_effect = $state();
	let playback_bar = $state() as HTMLInputElement;
	let volume = $state(0) as number;
	let size = 0.8;
	let queue_list = $state([]) as any[];
	let prev_queue = $state([]) as any[];
	let current_song = $state('') as string | null;
	let shuffle = $state(false);
	let prev_volume: number | null = null;
	let can_mutate_player = false;
	let queue_container = $state() as HTMLElement;
	let show_queue_container = $state(false);

	let {
		class: class_list = '',
		section_class = '',
		current_song_data,
		cover_image_url = $bindable(),
		database = $bindable(),
		external_player_data = $bindable({})
	}: {
		cover_image_url: string;
		class: string;
		database: DatabaseControl;
		current_song_data: any;
		section_class: string;
		external_player_data: any;
	} = $props();

	let db = $state() as DatabaseControl;
	let title = $state() as string | undefined;
	let artist = $state() as string | undefined;

	const update_player_from_external = (data: any) => {
		current_time = data.time;
		volume = data.volume ? data.volume : player_data.volume;
		queue_list = data.queue_list;
		prev_queue = data.prev_queue;
		shuffle = data.shuffle;
		if (data.current) current_song = data.current;
	};
	$effect(() => {
		external_player_data;
		update_player_from_external(external_player_data);
	});

	const update_player_data = () => {
		if ($other_loading || !can_mutate_player) return;

		player_data.time = current_time;
		player_data.volume = volume;
		player_data.queue_list = queue_list;
		player_data.prev_queue = prev_queue;
		player_data.shuffle = shuffle;
		// @ts-ignore
		player_data.current = current_song ? current_song : null;

		cache_control({
			name: 'player_data',
			method: 'set',
			data: JSON.stringify(player_data)
		});
	};

	function update_media_state() {
		if (player_data.state === false) {
			player_data.state = true;
			audio.play();
		} else if (player_data.state === true) {
			player_data.state = false;
			audio.pause();
		}
		update_player_data();
	}

	const update_time_stamp = () => {
		current_time_display = sec_to_min(current_time);
	};

	function auto_play() {
		player_data.state = false;
		audio.play();
		update_player_data();
	}

	// Updating the ID as well as the image. Can be fixed later.
	// This is a not good. But oh well.
	const load_image = async (blob: Blob) => {
		if (blob) {
			const parsed_blob = await parseBlob(blob);
			const picture = parsed_blob.common.picture;
			if (picture) {
				const _blob = new Blob([picture[0].data], {
					type: picture[0].format
				});
				cover_image_url = URL.createObjectURL(_blob);
			}

			current_song_data = parsed_blob;
		}
	};

	const queue_song_control = async (song_name: string) => {
		const _player_data = cache_control({ name: 'player_data', method: 'get' });
		if (_player_data) {
			const parsed_player_data = JSON.parse(_player_data);
			volume = parsed_player_data.volume;
			current_time = parsed_player_data.time;
			queue_list = parsed_player_data.queue_list;
			prev_queue = parsed_player_data.prev_queue;
			current_song = song_name;
			shuffle = parsed_player_data.shuffle;
			await load_song_data();
			auto_play();
		}
	};

	onMount(() => {
		db = new DatabaseControl();
		database = db; // Reassign to better naming

		const open_state = database.poll_open();
		open_state.then(async () => {
			logger.send('Database is open');

			const _player_data = cache_control({
				name: 'player_data',
				method: 'get'
			});

			// If player data exists
			if (_player_data) {
				const parsed_player_data = JSON.parse(_player_data);
				volume = parsed_player_data.volume;
				current_time = parsed_player_data.time;
				queue_list = parsed_player_data.queue_list;
				prev_queue = parsed_player_data.prev_queue;
				current_song = parsed_player_data.current ? parsed_player_data.current : null;
				shuffle = parsed_player_data.shuffle;
				load_song_data();
				can_mutate_player = true;
				return;
			}

			const song_list = cache_control({
				name: 'song_list',
				method: 'get'
			});

			// Player data does not exist
			if (song_list) {
				const _song_list = JSON.parse(song_list);
				player_data.queue_list = shuffler(_song_list);
			}

			cache_control({
				name: 'player_data',
				method: 'set',
				data: JSON.stringify(player_data)
			});
			// Update next song
			const song_name = next_song() as string;

			// Get data
			let updated_player_data: any = cache_control({
				name: 'player_data',
				method: 'get'
			});
			updated_player_data = JSON.parse(updated_player_data as string);

			// Update local references
			volume = updated_player_data.volume;
			current_time = updated_player_data.time;
			queue_list = updated_player_data.queue_list;
			prev_queue = updated_player_data.prev_queue;
			current_song = song_name;
			shuffle = updated_player_data.shuffle;

			current_song = song_name; // make sure to update the song once loaded
			load_song_data();

			// Allow mutation when content is loaded.
			can_mutate_player = true;
			// Update player
			update_player_data();
		});

		// Get user_data from cache
		const _user_data = cache_control({
			method: 'get',
			name: 'user_data'
		});
		const parsed_user_data = JSON.parse(_user_data as string);

		// Update queue color
		const sub = 120;
		let red = parseInt(parsed_user_data.preferred_color.slice(1, 3), 16);
		let green = parseInt(parsed_user_data.preferred_color.slice(3, 5), 16);
		let blue = parseInt(parsed_user_data.preferred_color.slice(5, 7), 16);

		if (red >= sub) red -= sub;
		if (green >= sub) green -= sub;
		if (blue >= sub) blue -= sub;

		queue_container.style.backgroundColor = `rgb(${red}, ${green}, ${blue})`;
		queue_container.style.display = 'none';
	});

	// Updates the id view on song change.
	const update_id_view = () => {
		if (current_song_data) {
			title = current_song_data.common.title;
			artist = current_song_data.common.artist;
		}
	};

	const update_queue_container = () => {
		if (show_queue_container) {
			queue_container.style.display = 'block';
		} else {
			queue_container.style.display = 'none';
		}
	};

	const load_song_data = async () => {
		if (!current_song) return;
		const blob = await fetch_song(current_song, database);
		await load_song(current_song, database);

		if (blob) {
			const parsed_blob = await parseBlob(blob);
			current_song_data = parsed_blob;
			const picture = parsed_blob.common.picture;
			if (picture) {
				const _blob = new Blob([picture[0].data], {
					type: picture[0].format
				});
				cover_image_url = URL.createObjectURL(_blob);
			}

			// Update the id view on load.
			title = parsed_blob.common.title;
			artist = parsed_blob.common.artist;
		}
	};

	let updated_player_data = false;
	const update_interval = 2000; // milliseconds
	const update_playback = async () => {
		const ratio = (current_time / duration) * 100;
		playback_bar.style.background = `linear-gradient(90deg, ${user_data.preferred_color} ${ratio}%, #303030 ${ratio}%)`;

		if (!updated_player_data && can_mutate_player) {
			updated_player_data = true;
			setTimeout(() => {
				update_player_data();
				//player_data.time = current_time;
				//player_data.queue_list = queue_list;
				//player_data.current = current_song as string; // weird desync bug fixed?
				updated_player_data = false;
			}, update_interval);
		}

		// Reset playback at 100%
		// Also load a song if there is a queue
		if (ratio === 100) {
			audio.pause();

			const song_name = next_song();
			console.log(song_name);
			current_song = song_name;
			current_time = 0;

			if (song_name) {
				await queue_song_control(song_name);
				update_player_data();
				update_id_view();
				auto_play();
			}
		}
	};

	const lookahead_queue = async () => {
		const _player_data = cache_control({ name: 'player_data', method: 'get' });
		if (_player_data) {
			const _player_data_parsed = JSON.parse(_player_data);
			const ahead_array = _player_data_parsed.queue_list.slice(0, user_data.ahead);

			for (const x in ahead_array) {
				logger.send(`Prefetching song: ${ahead_array[x]}`);
				await fetch_song(ahead_array[x], database);
			}
		}
	};

	$effect(() => {
		played_side_effect;
		player_data;
		update_playback();
		update_time_stamp();
		update_id_view();
	});

	$effect(() => {
		player_data.current;
		lookahead_queue();
	});

	$effect(() => {
		if ($is_mobile) {
			show_queue_container = false;
			update_queue_container();
		}
	});
</script>

<audio
	bind:this={audio}
	bind:duration
	bind:currentTime={current_time}
	bind:paused={player_data.state}
	bind:played={played_side_effect}
	{volume}
	id="audio_player"
	class="hidden"
></audio>
<section class={'relative bottom-0 ' + section_class}>
	<div id="playback_bar" class="px-2 sm:px-10 md:px-20 xl:px-40">
		<span class="time_stamp"> {current_time_display} </span>
		<input
			type="range"
			oninput={() => {
				update_playback();
				update_player_data();
			}}
			bind:value={current_time}
			bind:this={playback_bar}
			min="0"
			max={duration}
			class="inputRange"
		/>
		<span class="time_stamp"> {sec_to_min(duration)} </span>
	</div>
	<div
		id="music_player"
		style={(() => {
			let css = `background-color: ${user_data.preferred_color};`;
			if ($is_mobile) {
				css += 'grid-template-columns: auto 1fr auto; ';
			} else {
				css += 'grid-template-columns: minmax(auto, 200px) 1fr auto; ';
			}
			return css;
		})()}
		class={'grid h-20 w-full items-center justify-items-center rounded-lg md:rounded-none ' +
			class_list}
	>
		<div
			style={(() => {
				let _default = 'grid-template-columns: auto auto;';
				if (!$is_mobile) {
					//_default += 'max-width: 20%;';
				}
				return _default;
			})()}
			class="grid justify-self-start"
		>
			<img src={cover_image_url} alt="Cover" class="ml-3 w-14 rounded shadow-2xl" />
			<div class="ml-2 mt-auto overflow-hidden">
				<p class="overflow-hidden overflow-ellipsis whitespace-nowrap font-bold" id="title">
					{(() => {
						return title;
						//if (title) return title.slice(0, 12) + '...';
					})()}
				</p>
				<p class="overflow-hidden overflow-ellipsis whitespace-nowrap text-sm">{artist}</p>
			</div>
		</div>
		{#if $is_mobile}
			<button
				aria-label="Play, Pause button"
				class="ml-auto mr-4"
				onkeydown={(e) => {
					e.preventDefault();
					if (e.code == 'Space') update_media_state();
				}}
				onclick={update_media_state}
			>
				{#if player_data.state}
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width={size * 2 * 32}
						height={size * 2 * 32}
						viewBox="0 0 24 24"><path fill="#ffffff" d="M8 19V5l11 7z" /></svg
					>
				{:else}
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width={32 * 2 * size}
						height={size * 2 * 32}
						viewBox="0 0 24 24"><path fill="#ffffff" d="M14 18V6h3.5v12zm-7.5 0V6H10v12z" /></svg
					>
				{/if}
			</button>
		{/if}
		<div
			class="mr-10 mr-10 hidden h-fit w-fit items-center gap-6 sm:ml-10 sm:ml-auto sm:grid md:mx-auto"
			style="grid-template-columns: repeat(5, auto); align-content: center;"
		>
			<button
				class="mr-7 hidden h-fit w-fit sm:block"
				aria-label="Shuffle"
				onclick={async () => {
					shuffle = !shuffle;

					const song_list = cache_control({
						method: 'get',
						name: 'song_list'
					});
					if (!song_list) {
						return;
					}
					lookahead_queue();
					const song_list_parsed = JSON.parse(song_list);
					prev_queue = []; // destroy prev on shuffle
					if (shuffle) {
						queue_list = shuffler(song_list_parsed);
					} else {
						queue_list = song_list_parsed;
					}
					update_player_data();
				}}
			>
				{#if shuffle}
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width={36 * size}
						height={36 * size}
						viewBox="0 0 256 256"
						><path
							fill="#ffffff"
							d="M237.66 178.34a8 8 0 0 1 0 11.32l-24 24a8 8 0 0 1-11.32-11.32L212.69 192h-11.75a72.12 72.12 0 0 1-58.59-30.15l-41.72-58.4A56.1 56.1 0 0 0 55.06 80H32a8 8 0 0 1 0-16h23.06a72.12 72.12 0 0 1 58.59 30.15l41.72 58.4A56.1 56.1 0 0 0 200.94 176h11.75l-10.35-10.34a8 8 0 0 1 11.32-11.32ZM143 107a8 8 0 0 0 11.16-1.86l1.2-1.67A56.1 56.1 0 0 1 200.94 80h11.75l-10.35 10.34a8 8 0 0 0 11.32 11.32l24-24a8 8 0 0 0 0-11.32l-24-24a8 8 0 0 0-11.32 11.32L212.69 64h-11.75a72.12 72.12 0 0 0-58.59 30.15l-1.2 1.67A8 8 0 0 0 143 107m-30 42a8 8 0 0 0-11.16 1.86l-1.2 1.67A56.1 56.1 0 0 1 55.06 176H32a8 8 0 0 0 0 16h23.06a72.12 72.12 0 0 0 58.59-30.15l1.2-1.67A8 8 0 0 0 113 149"
						/></svg
					>
				{:else}
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width={36 * size}
						height={36 * size}
						viewBox="0 0 16 16"
						><path
							fill="#ffffff"
							d="m12 12.707l2.146 2.147a.5.5 0 0 0 .708-.708l-13-13a.5.5 0 1 0-.708.708l3.071 3.07A6 6 0 0 0 2.75 4.75a.75.75 0 0 0 0 1.5c1.243 0 2.122.432 2.932 1.082q.228-.217.477-.466l.707.707C5.65 8.786 4.606 9.75 2.75 9.75a.75.75 0 0 0 0 1.5c2.52 0 3.96-1.4 5.177-2.616l.707.707l-.39.387c.556.463 1.186.882 1.94 1.162l.859.86a.75.75 0 0 0 .957.957m-.992-3.82l2.458 2.458l.314-.315a.75.75 0 0 0 0-1.06l-1.5-1.5a.75.75 0 0 0-1.271.417M8.326 6.204l1.069 1.068c.58-.452 1.198-.791 1.963-.94l-.137.138a.75.75 0 0 0 1.06 1.06l1.5-1.5a.75.75 0 0 0 0-1.06l-1.5-1.5a.75.75 0 1 0-1.06 1.06l.265.265c-1.328.161-2.326.732-3.16 1.41"
						/></svg
					>
				{/if}
			</button>
			<button
				class="hidden h-fit w-fit sm:block"
				aria-label="Skip Backward focus:outline-none"
				onclick={async () => {
					const song_name = prev_song();
					if (song_name) {
						other_loading.set(true);
						await queue_song_control(song_name);
						other_loading.set(false);
						auto_play();
					}
				}}
			>
				<svg
					width={27.023 * size}
					xmlns="http://www.w3.org/2000/svg"
					height={27 * size}
					id="screenshot-4e166da8-35a2-8081-8005-55d9a1c8e365"
					viewBox="1844.5 2788.5 27.023 27"
					style="-webkit-print-color-adjust::exact"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					fill="none"
					version="1.1"
				>
					<g id="shape-4e166da8-35a2-8081-8005-55d9a1c8e365">
						<g class="fills" id="fills-4e166da8-35a2-8081-8005-55d9a1c8e365">
							<path
								d="M1846.750,2788.500C1847.987,2788.500,1849.000,2789.513,1849.000,2790.750L1849.000,2813.250C1849.000,2814.487,1847.987,2815.500,1846.750,2815.500C1845.513,2815.500,1844.500,2814.487,1844.500,2813.250L1844.500,2790.750C1844.500,2789.513,1845.513,2788.500,1846.750,2788.500ZM1854.985,2803.845L1867.968,2813.003C1869.452,2814.060,1871.523,2812.980,1871.523,2811.157L1871.523,2792.843C1871.523,2791.020,1869.475,2789.963,1867.968,2790.997L1854.985,2800.155C1854.382,2800.576,1854.023,2801.265,1854.023,2802.000C1854.023,2802.735,1854.382,2803.424,1854.985,2803.845Z"
								style="fill:#ffffff"
							>
							</path>
						</g>
					</g>
				</svg>
			</button>
			<button
				class="hidden h-fit w-fit focus:outline-none sm:block"
				aria-label="Play, Pause button"
				onkeydown={(e) => {
					e.preventDefault();
					if (e.code == 'Space') update_media_state();
				}}
				onclick={update_media_state}
			>
				{#if player_data.state}
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width={60 * size}
						height={60 * size}
						viewBox="0 0 48 48"
					>
						<defs>
							<mask id="ipSPlay0">
								<g fill="none" stroke-linejoin="round" stroke-width="4">
									<path
										fill="#fff"
										stroke="#fff"
										d="M24 44c11.046 0 20-8.954 20-20S35.046 4 24 4S4 12.954 4 24s8.954 20 20 20Z"
									/>
									<path
										fill="#000"
										stroke="#000"
										d="M20 24v-6.928l6 3.464L32 24l-6 3.464l-6 3.464z"
									/>
								</g>
							</mask>
						</defs>
						<path fill="white" d="M0 0h48v48H0z" mask="url(#ipSPlay0)" />
					</svg>
				{:else}
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width={60 * size}
						height={60 * size}
						viewBox="0 0 48 48"
					>
						<defs>
							<mask id="ipSPauseOne0">
								<g fill="none" stroke-linejoin="round" stroke-width="4">
									<path
										fill="#fff"
										stroke="#fff"
										d="M24 44c11.046 0 20-8.954 20-20S35.046 4 24 4S4 12.954 4 24s8.954 20 20 20Z"
									/>
									<path stroke="#000" stroke-linecap="round" d="M19 18v12m10-12v12" />
								</g>
							</mask>
						</defs>
						<path fill="white" d="M0 0h48v48H0z" mask="url(#ipSPauseOne0)" />
					</svg>
				{/if}
			</button>
			<button
				class="hidden h-fit w-fit sm:block"
				aria-label="Skip Forward focus:outline-none"
				onclick={async () => {
					const song_name = next_song();
					if (song_name) {
						other_loading.set(true);
						await queue_song_control(song_name);
						other_loading.set(false);
						auto_play();
					}
				}}
			>
				<svg
					width={27 * size}
					xmlns="http://www.w3.org/2000/svg"
					height={27 * size}
					id="screenshot-4e166da8-35a2-8081-8005-55da36c353a4"
					viewBox="2011 2789 27 27"
					style="-webkit-print-color-adjust::exact"
					xmlns:xlink="http://www.w3.org/1999/xlink"
					fill="none"
					version="1.1"
				>
					<g id="shape-4e166da8-35a2-8081-8005-55da36c353a4">
						<g class="fills" id="fills-4e166da8-35a2-8081-8005-55da36c353a4">
							<path
								d="M2014.555,2813.503L2027.537,2804.345C2028.798,2803.445,2028.798,2801.555,2027.537,2800.678L2014.555,2791.497C2013.048,2790.463,2011.000,2791.520,2011.000,2793.343L2011.000,2811.657C2011.000,2813.480,2013.048,2814.537,2014.555,2813.503ZM2033.500,2791.250L2033.500,2813.750C2033.500,2814.987,2034.512,2816.000,2035.750,2816.000C2036.988,2816.000,2038.000,2814.987,2038.000,2813.750L2038.000,2791.250C2038.000,2790.013,2036.988,2789.000,2035.750,2789.000C2034.512,2789.000,2033.500,2790.013,2033.500,2791.250Z"
								style="fill:#ffffff"
							>
							</path>
						</g>
					</g>
				</svg>
			</button>
			<div class="relative flex">
				<div
					bind:this={queue_container}
					class="absolute bottom-12 right-0 ml-auto hidden max-h-60 min-h-0 w-80 flex-col gap-1 overflow-x-hidden overflow-y-scroll rounded-lg p-2 shadow-2xl drop-shadow-xl sm:flex"
				>
					<h1 class="text-md sticky top-0 rounded bg-black py-2 pl-2 font-bold">Your Queue</h1>
					{#each queue_list as item, index}
						{#if item !== null}
							<button
								class="my-1 h-10 w-full overflow-clip overflow-ellipsis whitespace-nowrap rounded py-2 pl-2 text-start font-bold"
								style="background-color: {user_data.preferred_color};"
								onclick={async () => {
									other_loading.set(true);
									current_song = skip_ahead(index);
									player_data.state = true;
									await load_song_data();
									let _player_data = cache_control({ method: 'get', name: 'player_data' });

									if (_player_data) {
										const parsed_data = JSON.parse(_player_data);
										queue_list = parsed_data.queue_list;
										prev_queue = parsed_data.prev_queue;
										update_player_data();
										player_data.state = false;
									}

									other_loading.set(false);
								}}
							>
								{(() => item.slice(0, -4))()}
							</button>
						{/if}
					{/each}
				</div>
				<button
					onclick={() => {
						show_queue_container = !show_queue_container;
						update_queue_container();
					}}
					class="relative ml-7 hidden h-fit w-fit sm:block"
					aria-label="Queue"
				>
					<svg
						width={25.5 * size}
						xmlns="http://www.w3.org/2000/svg"
						height={25.5 * size}
						id="screenshot-4e166da8-35a2-8081-8005-55db53b01f6b"
						viewBox="2118.25 2788.25 25.5 25.5"
						style="-webkit-print-color-adjust::exact"
						xmlns:xlink="http://www.w3.org/1999/xlink"
						fill="none"
						version="1.1"
					>
						<g id="shape-4e166da8-35a2-8081-8005-55db53b01f6b">
							<g class="fills" id="fills-4e166da8-35a2-8081-8005-55db53b01f6b">
								<path
									d="M2118.250,2792.500C2118.250,2790.153,2120.153,2788.250,2122.500,2788.250L2139.500,2788.250C2141.847,2788.250,2143.750,2790.153,2143.750,2792.500C2143.750,2794.847,2141.847,2796.750,2139.500,2796.750L2122.500,2796.750C2120.153,2796.750,2118.250,2794.847,2118.250,2792.500ZM2118.250,2803.656C2118.250,2802.776,2118.964,2802.063,2119.844,2802.063L2142.156,2802.063C2143.036,2802.063,2143.750,2802.776,2143.750,2803.656C2143.750,2804.536,2143.036,2805.250,2142.156,2805.250L2119.844,2805.250C2118.964,2805.250,2118.250,2804.536,2118.250,2803.656ZM2119.844,2810.563C2118.964,2810.563,2118.250,2811.276,2118.250,2812.156C2118.250,2813.036,2118.964,2813.750,2119.844,2813.750L2142.156,2813.750C2143.036,2813.750,2143.750,2813.036,2143.750,2812.156C2143.750,2811.276,2143.036,2810.563,2142.156,2810.563Z"
									style="fill:#ffffff"
								>
								</path>
							</g>
						</g>
					</svg>
				</button>
			</div>
		</div>
		<div
			class="hidden items-center justify-end justify-self-end md:flex"
			style="max-width: 20%; width: 100%;"
		>
			<button
				onclick={() => {
					if (prev_volume === null) {
						prev_volume = volume;
						volume = 0;
					} else {
						volume = prev_volume;
						prev_volume = null;
					}
				}}
			>
				{#if volume > 0.5}
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width={31 * size}
						height={31 * size}
						viewBox="0 0 24 24"
					>
						<g fill="white">
							<path
								d="M13 6.037c0-1.724-1.978-2.665-3.28-1.562L5.638 7.933H4c-1.105 0-2 .91-2 2.034v4.066c0 1.123.895 2.034 2 2.034h1.638l4.082 3.458c1.302 1.104 3.28.162 3.28-1.562z"
							/>
							<path
								fill-rule="evenodd"
								d="M14.786 7.658a.99.99 0 0 1 1.414-.014A6.14 6.14 0 0 1 18 12c0 1.662-.655 3.17-1.715 4.27a.99.99 0 0 1-1.414.014a1.03 1.03 0 0 1-.014-1.437A4.1 4.1 0 0 0 16 12a4.1 4.1 0 0 0-1.2-2.904a1.03 1.03 0 0 1-.014-1.438"
								clip-rule="evenodd"
							/>
							<path
								fill-rule="evenodd"
								d="M17.657 4.811a.99.99 0 0 1 1.414 0A10.22 10.22 0 0 1 22 12c0 2.807-1.12 5.35-2.929 7.189a.99.99 0 0 1-1.414 0a1.03 1.03 0 0 1 0-1.438A8.17 8.17 0 0 0 20 12a8.17 8.17 0 0 0-2.343-5.751a1.03 1.03 0 0 1 0-1.438"
								clip-rule="evenodd"
							/>
						</g>
					</svg>
				{:else if volume > 0}
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width={31 * size}
						height={31 * size}
						viewBox="0 0 24 24"
					>
						<g fill="white">
							<path
								d="M15 6.037c0-1.724-1.978-2.665-3.28-1.562L7.638 7.933H6c-1.105 0-2 .91-2 2.034v4.066c0 1.123.895 2.034 2 2.034h1.638l4.082 3.458c1.302 1.104 3.28.162 3.28-1.562z"
							/>
							<path
								fill-rule="evenodd"
								d="M16.786 7.658a.99.99 0 0 1 1.414-.014A6.14 6.14 0 0 1 20 12c0 1.662-.655 3.17-1.715 4.27a.99.99 0 0 1-1.414.014a1.03 1.03 0 0 1-.014-1.437A4.1 4.1 0 0 0 18 12a4.1 4.1 0 0 0-1.2-2.904a1.03 1.03 0 0 1-.014-1.438"
								clip-rule="evenodd"
							/>
						</g>
					</svg>
				{:else}
					<svg
						xmlns="http://www.w3.org/2000/svg"
						width={31 * size}
						height={31 * size}
						viewBox="0 0 24 24"
					>
						<path
							fill="white"
							d="M5.707 4.293a1 1 0 0 0-1.414 1.414l14 14a1 1 0 0 0 1.414-1.414l-.004-.005C21.57 16.498 22 13.938 22 12a9.97 9.97 0 0 0-2.929-7.071a1 1 0 1 0-1.414 1.414A7.97 7.97 0 0 1 20 12c0 1.752-.403 3.636-1.712 4.873l-1.433-1.433C17.616 14.37 18 13.107 18 12c0-1.678-.69-3.197-1.8-4.285a1 1 0 1 0-1.4 1.428A4 4 0 0 1 16 12c0 .606-.195 1.335-.59 1.996L13 11.586V6.135c0-1.696-1.978-2.622-3.28-1.536L7.698 6.284l-1.99-1.991ZM4 8h.586L13 16.414v1.451c0 1.696-1.978 2.622-3.28 1.536L5.638 16H4a2 2 0 0 1-2-2v-4a2 2 0 0 1 2-2"
						/>
					</svg>
				{/if}
			</button>
			<input
				class="mr-4"
				type="range"
				max="1"
				step="0.01"
				min="0"
				bind:value={volume}
				oninput={update_player_data}
			/>
		</div>
	</div>
</section>
