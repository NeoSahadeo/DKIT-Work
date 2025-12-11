<script lang="ts">
	import './signup.css';
	import { cache_control, shuffler, url_resolver } from '$lib/utils';
	import { next_song, request_songs } from '$lib/song_api';
	import { other_loading } from '$lib/store';
	import { player_data } from '$lib/shared.svelte';
	import { user_data } from '$lib/shared.svelte';
	import { PROD } from '$lib/shared.svelte';

	let default_volume = $state(3);
	let username = $state('');
	let email = $state('');
	let phone_number = $state() as number;
	let ahead = $state(1);
	let date_of_birth = $state(0);
	let preferred_color = $state('#FF0000');
	let accepted_terms = $state(false);

	const create_account = () => {
		if (accepted_terms)
			cache_control({
				name: 'user_data',
				method: 'set',
				data: JSON.stringify({
					preferred_color,
					default_volume,
					keep_image: true,
					keep_gradient: true,
					keep_dull: true,
					ahead // How many songs to look ahead.
				})
			});
	};
</script>

<div class="flex flex-col gap-3">
	<form
		id="signup"
		class="mx-auto mt-10"
		style="max-width: 500px; width: 100%;"
		onsubmit={async (e) => {
			e.preventDefault();
			other_loading.set(true);
			create_account();
			// Request song list
			await request_songs();
			// Shuffle playlist
			const song_list = cache_control({ method: 'get', name: 'song_list' });
			if (song_list) {
				const song_array = JSON.parse(song_list);
				player_data.queue_list = shuffler(song_array);
				player_data.volume = default_volume * 0.01;
				cache_control({
					name: 'player_data',
					method: 'set',
					data: JSON.stringify(player_data)
				});

				// Load the song
				const current_song = next_song();
				if (current_song) {
					player_data.current = current_song;
					player_data.queue_list = player_data.queue_list.slice(1); // Remove the song from queue

					cache_control({
						name: 'player_data',
						method: 'set',
						data: JSON.stringify(player_data)
					});
				}

				// Set current page
				cache_control({
					name: 'current_page',
					method: 'set',
					data: 'player'
				});
			} else {
				// Error
			}

			other_loading.set(false);
			// Redirect after
			window.location.href = url_resolver() + 'player' + (() => (PROD ? '.html' : ''))();
		}}
	>
		<h1
			class="rounded-t-lg px-12 py-3 text-center text-2xl text-white"
			style="background-color: #ee4110;"
		>
			Set up account
		</h1>
		<section class="flex flex-col gap-3 rounded-b-lg bg-white px-4 pb-2 pt-4" style="color: black;">
			<div class="flex flex-row items-center gap-5 rounded bg-yellow-400 px-3 py-3">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					class="flex-shrink-0"
					width={40}
					height={40}
					viewBox="0 0 24 24"
					><path
						fill="#1e1e00"
						d="M4.47 21h15.06c1.54 0 2.5-1.67 1.73-3L13.73 4.99c-.77-1.33-2.69-1.33-3.46 0L2.74 18c-.77 1.33.19 3 1.73 3M12 14c-.55 0-1-.45-1-1v-2c0-.55.45-1 1-1s1 .45 1 1v2c0 .55-.45 1-1 1m1 4h-2v-2h2z"
					/></svg
				>
				<p style="color: #1e1e00;">
					All data on this site is saved on local storage. No information saved will be transfered
					out of your computer.
				</p>
			</div>
			<div class="flex flex-row items-center gap-5 rounded bg-red-600 px-3 py-3">
				<svg xmlns="http://www.w3.org/2000/svg" width={60} height={60} viewBox="0 0 16 16"
					><g fill="#1e0101"
						><path
							d="M10.371 8.277v-.553c0-.827-.422-1.234-.987-1.234c-.572 0-.99.407-.99 1.234v.553c0 .83.418 1.237.99 1.237c.565 0 .987-.408.987-1.237m2.586-.24c.463 0 .735-.272.735-.744s-.272-.741-.735-.741h-.774v1.485z"
						/><path
							d="M4.893 0a.5.5 0 0 0-.353.146L.146 4.54A.5.5 0 0 0 0 4.893v6.214a.5.5 0 0 0 .146.353l4.394 4.394a.5.5 0 0 0 .353.146h6.214a.5.5 0 0 0 .353-.146l4.394-4.394a.5.5 0 0 0 .146-.353V4.893a.5.5 0 0 0-.146-.353L11.46.146A.5.5 0 0 0 11.107 0zM3.16 10.08c-.931 0-1.447-.493-1.494-1.132h.653c.065.346.396.583.891.583c.524 0 .83-.246.83-.62c0-.303-.203-.467-.637-.572l-.656-.164c-.61-.147-.978-.51-.978-1.078c0-.706.597-1.184 1.444-1.184c.853 0 1.386.475 1.436 1.087h-.645c-.064-.32-.352-.542-.797-.542c-.472 0-.77.246-.77.6c0 .261.196.437.553.522l.654.161c.673.164 1.06.487 1.06 1.11c0 .736-.574 1.228-1.544 1.228Zm3.427-3.51V10h-.665V6.57H4.753V6h3.006v.568H6.587Zm4.458 1.16v.544c0 1.131-.636 1.805-1.661 1.805c-1.026 0-1.664-.674-1.664-1.805V7.73c0-1.136.638-1.807 1.664-1.807s1.66.674 1.66 1.807ZM11.52 6h1.535c.82 0 1.316.55 1.316 1.292c0 .747-.501 1.289-1.321 1.289h-.865V10h-.665V6.001Z"
						/></g
					></svg
				>
				<p style="color: #1e0101;">
					Make sure you are on an unmetered connection or a subsequent data plan.
				</p>
			</div>
			<div class="flex flex-col">
				<label for="primary_color"> primary_color </label>
				<input
					name="primary_color"
					type="color"
					bind:value={preferred_color}
					style="padding: 0px;"
				/>
			</div>
			<div class="flex flex-col">
				<label for="email"> Email </label>
				<input
					name="email"
					placeholder="Email Address"
					type="email"
					pattern="[a-zA-Z0-9]*@[a-zA-Z0-9]*\..*"
					bind:value={email}
				/>
			</div>
			<div class="flex flex-col">
				<label for="dob"> Date of Birth </label>
			</div>
			<input name="dob" type="date" bind:value={date_of_birth} />
			<div class="flex flex-col">
				<label for="default_volume"> Default Volume: {default_volume}%</label>
			</div>
			<input name="default_volume" type="range" min="0" max="100" bind:value={default_volume} />
			<div class="flex flex-col">
				<label for="username"> Username </label>
				<input placeholder="Username" type="text" name="username" bind:value={username} />
			</div>
			<div class="flex flex-col">
				<label for="download_ahead"
					>Download Ahead<span class="text-sm"
						>&nbsp;(How many songs will be downloaded ahead for seamless playback; 1 should be fine)</span
					></label
				>
				<input name="download_ahead" type="number" bind:value={ahead} min="0" max="10" />
			</div>
			<div class="flex flex-col">
				<label for="telephone"> Phone Number </label>
				<input name="telephone" placeholder="Phone number" type="tel" bind:value={phone_number} />
			</div>
			<div class="flex flex-row items-center gap-3">
				<label for="terms" class="font-bold">
					I have Read and will Accept the <a
						class="font-bold text-blue-800"
						href="https://youtu.be/dQw4w9WgXcQ"
						target="_blank"
						>term and conditions
					</a></label
				>
				<input name="terms" type="checkbox" bind:checked={accepted_terms} required />
			</div>
			<input
				type="submit"
				value="Set up account"
				class="mr-auto w-fit cursor-pointer rounded-lg px-3 py-2 font-bold text-white"
				style="background-color: #ee640c;"
			/>
		</section>
	</form>
	<div id="spacer" class=" h-12 w-full" style="height: 3em;"></div>
</div>
