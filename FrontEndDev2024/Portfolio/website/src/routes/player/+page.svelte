<script lang="ts">
	import './player.css';
	import { parseBlob, type IAudioMetadata } from 'music-metadata';
	import { is_mobile, logger } from '$lib/store';
	import MusicPlayer from '$lib/components/musicPlayer.svelte';
	import SearchIcon from '$lib/components/searchIcon.svelte';
	import { player_data, user_data } from '$lib/shared.svelte';
	import { onMount } from 'svelte';
	import { fetch_song, load_song, search_songs } from '$lib/song_api';
	import { cache_control, type DatabaseControl, shuffler } from '$lib/utils';
	import { other_loading } from '$lib/store';

	let cover_image_url = $state() as string;
	let rotation = $state(0) as number;
	let interval: any = null;
	let search_focus = $state(false);
	let search = $state('');
	let search_entries = $state([] as any[]);
	let load_initiated = $state(false);
	let external_player_data = $state(player_data);

	$effect(() => {
		external_player_data = player_data;
	});

	const search_box_offset = 50; // bottom playback_bar offset in pixels
	let search_box = $state() as HTMLElement;
	//let parent_height = $state() as number;

	let database = $state() as DatabaseControl;
	let current_song_data = $state() as any;

	$effect(() => {
		search_entries = search_songs(search);

		// Keep the state of the loading screen
		other_loading.set(load_initiated);
	});

	$effect(() => {
		player_data.state;
		if (!player_data.state && interval === null) {
			interval = setInterval(() => {
				rotation += 1;
			}, 60);
		} else if (player_data.state) {
			clearInterval(interval);
			interval = null;
		}

		calc_height();
	});

	const calc_height = () => {
		const playback_bar = document.getElementById('playback_bar');
		if (playback_bar && search_box) {
			search_box.style.maxHeight = `
			${playback_bar.getBoundingClientRect().top - search_box.getBoundingClientRect().bottom - search_box_offset}px`;
		}
	};

	// Updating the ID as well as the image. Can be fixed later.
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

	const trap_input = (e: Event) => {
		e.preventDefault();
	};

	const shuffle_songs = () => {
		const song_list = cache_control({
			method: 'get',
			name: 'song_list'
		});

		if (song_list) {
			const song_array = JSON.parse(song_list);
			player_data.queue_list = shuffler(song_array);
			logger.send('Songs shuffled. Caching data');
			cache_control({
				name: 'player_data',
				method: 'set',
				data: JSON.stringify(player_data)
			});
		}
	};

	onMount(() => {
		search_entries = search_songs(search);
		document.addEventListener('keypress', (e) => {
			if (e.code == 'Space' && !search_focus) {
				player_data.state = !player_data.state;
			}
		});

		//window.addEventListener('resize', () => {
		//	calc_height();
		//});
	});
</script>

<title> Player | {player_data.current}</title>

<section
	class="flex h-full flex-grow flex-col items-center justify-center justify-items-center md:grid"
	style="grid-template-columns: 1fr; grid-template-rows: auto 1fr 0.4fr auto;"
>
	<div
		style="width: {(() => {
			if (!$is_mobile) return '30em';
			return '100%';
		})()}; height: 2.3em; transition: 0.2s all; background-color: {(() => {
			if (search_focus) return 'rgb(17, 24, 39)';
		})()};"
		class="mt-10 flex flex-row items-center gap-2 bg-gray-900 pl-4 hover:bg-gray-800 sm:rounded-full"
	>
		<SearchIcon />
		<input
			type="text"
			placeholder="Search for music"
			class="w-full bg-transparent focus:outline-none"
			bind:value={search}
			onkeypress={() => {
				search_focus = true;
			}}
			onfocus={() => {
				search_focus = true;
			}}
			onblur={() => {
				search_focus = false;
			}}
		/>
	</div>
	{#if search.length === 0}
		<img
			src={cover_image_url}
			alt="Cover"
			class="my-auto h-64 w-64 rounded-full object-cover sm:h-80 sm:w-80 md:mx-auto"
			style="rotate: {rotation}deg; transition: 0.1s all;"
			id="cover_image_larger"
		/>
	{:else}
		<div
			class="mt-4 flex w-full flex-col items-start gap-1 self-start sm:px-32"
			style="overflow: auto;"
			bind:this={search_box}
		>
			{#each search_entries as entry}
				<button
					class="min-h-9 w-full overflow-hidden overflow-ellipsis whitespace-nowrap rounded px-3 py-2 text-start hover:drop-shadow-lg hover:hue-rotate-15"
					style="background-color: {user_data.preferred_color};"
					onclick={async () => {
						if (!load_initiated) {
							load_initiated = true;
							player_data.state = true; // Forces rescan

							const blob = await fetch_song(entry, database);
							await load_song(entry, database);
							if (blob) {
								await load_image(blob);
							}

							if (player_data.shuffle) shuffle_songs();

							// Reset
							search = '';
							search_focus = false;
							player_data.current = entry;
							player_data.time = 0;
							player_data.state = false;
							cache_control({
								name: 'player_data',
								method: 'set',
								data: JSON.stringify(player_data)
							});
							load_initiated = false;
						}
					}}>{(() => entry.slice(0, -4))()}</button
				>
			{/each}
		</div>
	{/if}
	<MusicPlayer
		class="bottom-0 mt-auto w-screen justify-between md:static md:absolute"
		section_class="contents"
		bind:cover_image_url
		bind:database
		bind:external_player_data
		{current_song_data}
	/>
</section>
