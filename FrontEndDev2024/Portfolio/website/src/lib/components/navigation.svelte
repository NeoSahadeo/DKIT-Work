<script lang="ts">
	import { url_resolver } from '$lib/utils';
	import { cache_control } from '$lib/utils';
	import { other_loading } from '$lib/store';
	import { onMount } from 'svelte';
	import { PROD, user_data, player_data } from '$lib/shared.svelte';
	import { writable } from 'svelte/store';

	let volume = writable(0);
	let show_nav = $state(false);
	let page_number = $state() as number;
	const page_order = ['home', 'player', 'about', 'profile'];
	let is_mutable = false;

	onMount(() => {
		const current_page = cache_control({
			name: 'current_page',
			method: 'get'
		});
		if (current_page) {
			page_number = page_order.indexOf(current_page as string) + 1;
			update_nav();
		}

		const _player_data = cache_control({
			name: 'player_data',
			method: 'get'
		});

		const parsed_player_data = JSON.parse(_player_data as string);
		volume.set(parsed_player_data.volume);
		is_mutable = true;
	});

	const update_nav = () => {
		const elements = document.querySelectorAll('.current');
		elements.forEach((e) => e.classList.remove('current'));

		const selected_element = document.getElementById(
			page_order[page_number - 1]
		) as HTMLAnchorElement;
		selected_element.classList.add('current');

		cache_control({
			name: 'current_page',
			method: 'set',
			data: page_order[page_number - 1]
		});

		if (window.location.href !== selected_element.href)
			window.location.href = selected_element.href;
	};

	const update_player_data = () => {
		if ($other_loading || !is_mutable) return;

		const _player_data = cache_control({
			name: 'player_data',
			method: 'get'
		});
		const parsed_player_data = JSON.parse(_player_data as string);

		player_data.time = parsed_player_data.time;
		player_data.volume = $volume;
		player_data.queue_list = parsed_player_data.queue_list;
		player_data.prev_queue = parsed_player_data.prev_queue;
		player_data.shuffle = parsed_player_data.shuffle;
		// @ts-ignore
		player_data.current = parsed_player_data.current_song ? parsed_player_data.current_song : null;

		cache_control({
			name: 'player_data',
			method: 'set',
			data: JSON.stringify(player_data)
		});
	};

	// Effect has weird loop bullshit
	volume.subscribe(() => {
		update_player_data();
	});

	// Scrapping this cause its janky.
	//<input
	//	type="range"
	//	min="1"
	//	max="4"
	//	bind:value={page_number}
	//	oninput={update_nav}
	//	onchange={() => {
	//		window.location.href = (
	//			document.getElementById(page_order[page_number - 1]) as HTMLAnchorElement
	//		).href;
	//	}}
	//	class="slider absolute rotate-90"
	//	style="top: 5em; left: -2.7em;"
	///>
</script>

<nav class="absolute right-4 top-3 z-20 w-fit md:left-4 md:top-10">
	{#if !show_nav}
		<button
			class="absolute right-0 z-20 block md:hidden"
			aria-label="Menu"
			onclick={() => {
				show_nav = !show_nav;
			}}
			><svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 16 16"
				><path
					fill="#ffffff"
					fill-rule="evenodd"
					d="M0 3.75A.75.75 0 0 1 .75 3h14.5a.75.75 0 0 1 0 1.5H.75A.75.75 0 0 1 0 3.75M0 8a.75.75 0 0 1 .75-.75h14.5a.75.75 0 0 1 0 1.5H.75A.75.75 0 0 1 0 8m.75 3.5a.75.75 0 0 0 0 1.5h14.5a.75.75 0 0 0 0-1.5z"
					clip-rule="evenodd"
				/></svg
			>
		</button>
	{:else}
		<button
			class="absolute right-0 z-20 block md:hidden"
			aria-label="Menu"
			onclick={() => {
				show_nav = !show_nav;
			}}
		>
			<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24"
				><path
					fill="#ffffff"
					d="m12 13.4l-4.9 4.9q-.275.275-.7.275t-.7-.275t-.275-.7t.275-.7l4.9-4.9l-4.9-4.9q-.275-.275-.275-.7t.275-.7t.7-.275t.7.275l4.9 4.9l4.9-4.9q.275-.275.7-.275t.7.275t.275.7t-.275.7L13.4 12l4.9 4.9q.275.275.275.7t-.275.7t-.7.275t-.7-.275z"
				/></svg
			>
		</button>
	{/if}
	{#if show_nav}
		<div
			class="fixed left-0 top-0 z-10 block flex w-screen flex-col items-center justify-center bg-black bg-opacity-70 pt-10 backdrop-blur md:hidden"
			style="height:100dvh"
		>
			<ul class="flex flex-col gap-3 text-center">
				<li class="flex">
					<a
						id="home"
						style="background-color: {user_data.preferred_color} ;"
						class="w-full rounded px-3 text-2xl text-white"
						href={url_resolver()}
						onclick={() => {
							page_number = 1;
							update_nav();
						}}
					>
						Home
					</a>
				</li>
				<li class="flex">
					<a
						id="player"
						class="w-full rounded px-3 text-2xl text-white"
						style="background-color: {user_data.preferred_color} ;"
						href={url_resolver() + 'player' + (() => (PROD ? '.html' : ''))()}
						onclick={() => {
							page_number = 2;
							update_nav();
						}}
					>
						Music Player
					</a>
				</li>
				<li class="flex">
					<a
						id="about"
						class="w-full rounded px-3 text-2xl text-white"
						style="background-color: {user_data.preferred_color} ;"
						onclick={() => {
							page_number = 3;
							update_nav();
						}}
						href={url_resolver() + 'about' + (() => (PROD ? '.html' : ''))()}
					>
						About
					</a>
				</li>
				<li class="flex">
					<a
						id="profile"
						class="w-full rounded px-3 text-2xl text-white"
						style="background-color: {user_data.preferred_color} ;"
						onclick={() => {
							page_number = 4;
							update_nav();
						}}
						href={url_resolver() + 'profile' + (() => (PROD ? '.html' : ''))()}
					>
						Profile
					</a>
				</li>
			</ul>
			<input
				class="mt-10"
				type="range"
				max="1"
				step="0.01"
				min="0"
				bind:value={$volume}
				oninput={update_player_data}
			/>
		</div>
	{/if}
	<ul class="hidden flex-col gap-3 md:flex">
		<li>
			<a
				id="home"
				class="text-gray-600"
				href={url_resolver()}
				onclick={() => {
					page_number = 1;
					update_nav();
				}}
			>
				Home
			</a>
		</li>
		<li>
			<a
				id="player"
				class="whitespace-nowrap text-gray-600"
				href={url_resolver() + 'player' + (() => (PROD ? '.html' : ''))()}
				onclick={() => {
					page_number = 2;
					update_nav();
				}}
			>
				Music Player
			</a>
		</li>
		<li>
			<a
				id="about"
				class="text-gray-600"
				onclick={() => {
					page_number = 3;
					update_nav();
				}}
				href={url_resolver() + 'about' + (() => (PROD ? '.html' : ''))()}
			>
				About
			</a>
		</li>
		<li>
			<a
				id="profile"
				class="text-gray-600"
				onclick={() => {
					page_number = 4;
					update_nav();
				}}
				href={url_resolver() + 'profile' + (() => (PROD ? '.html' : ''))()}
			>
				Profile
			</a>
		</li>
	</ul>
</nav>
