<script lang="ts">
	import {
		update_user_data,
		load_user_data,
		cache_control,
		shuffler,
		DatabaseControl
	} from '$lib/utils';
	import { user_data, notifications, player_data } from '$lib/shared.svelte';
	import {
		request_songs,
		search_songs,
		fetch_song,
		load_song,
		next_song,
		prev_song
	} from '$lib/song_api';
	import MusicPlayer from '$lib/components/musicPlayer.svelte';
	import { onMount } from 'svelte';
	import { loading_song, logger, other_loading } from '$lib/store';
	import GeneralLoading from '$lib/components/generalLoading.svelte';

	let query = $state('');
	let current_song_data = $state();
	let cover_image_url = $state('');
	let database = $state() as DatabaseControl;
	let external_player_data = $state(player_data);

	//onMount(() => {
	//	load_user_data();
	//});

	//$effect(() => {
	//	update_user_data(user_data);
	//});

	const send_noti = () => {
		notifications.push({
			id: Math.random(),
			message: 'Hello world',
			timeout: 5,
			priority: 0
		});
	};

	const request_songys = async () => {
		console.log(await request_songs());
	};

	const search_songys = () => {
		console.log(search_songs(query));
	};

	$inspect(notifications);
	//$inspect(user_data);

	//$effect(() => console.log($other_loading));
</script>

<title> Debug </title>

<h1 class="mx-auto mt-4 w-fit text-2xl">音 OTO DEBUG</h1>
<p class="mx-auto">These are debug controls that are not meant for end-users.</p>

<div>
	<label for="color_input"> Color selector </label>
	<input bind:value={user_data.preferred_color} id="color_input" type="color" />
</div>

<div>
	<label for="toggle_dull"> Toggle Dull </label>
	<input bind:checked={user_data.keep_dull} id="toggle_dull" type="checkbox" />
</div>

<div>
	<label for="toggle_background"> Toggle Background </label>
	<input bind:checked={user_data.keep_image} id="toggle_background" type="checkbox" />
</div>

<div>
	<label for="toggle_gradient"> Toggle Gradient </label>
	<input bind:checked={user_data.keep_gradient} id="toggle_gradient" type="checkbox" />
</div>

<div>
	<label for="toggle_gradient"> Prefetch Amount </label>
	<input bind:value={user_data.ahead} id="toggle_gradient" type="number" class="text-black" />
</div>

<div>
	<label for="default_volume"> Default Volume </label>
	<input bind:value={user_data.default_volume} id="default_volume" type="range" min="0" max="100" />
</div>

<div>
	<button onclick={load_user_data} class="rounded bg-red-500 px-3"> Load user data </button>
</div>

<div>
	<button onclick={send_noti} class="rounded bg-red-500 px-3"> Send Notification </button>
</div>

<div>
	<button onclick={request_songys} class="rounded bg-green-500 px-3"> Request Song List </button>
</div>

<div>
	<input bind:value={query} placeholder="Search Song" class="text-black" />
	<button onclick={search_songys} class="rounded bg-green-600 px-3"> Search Song List </button>
</div>

<div>
	<input bind:value={query} placeholder="Search Song" class="text-black" />
	<button
		onclick={async () => {
			current_song_data = await fetch_song(query, db);
			console.log(current_song_data);
		}}
		class="rounded bg-blue-600 px-3"
	>
		Fetch song
	</button>
</div>

<div>
	<input bind:value={query} placeholder="Search Song" class="text-black" />
	<button
		onclick={async () => {
			await load_song(query, db);
		}}
		class="rounded bg-blue-600 px-3"
	>
		Load song
	</button>
</div>

<div>
	<button
		onclick={() => {
			db.set({
				name: '123',
				data: '123'
			});
		}}
	>
		Update database
	</button>
</div>

<div>
	<button
		onclick={() => {
			//db.delete({
			//	name: '123',
			//});
		}}
	>
		Delete entry
	</button>
</div>

<div>
	<button
		class="relative z-20 bg-green-800 px-3"
		onclick={() => {
			other_loading.update((value) => !value);
		}}>Toggle General Loading</button
	>
</div>

<div>
	<button
		class="bg-orange-500 px-3"
		onclick={() => {
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
		}}
	>
		Shuffle Songs
	</button>
</div>

<div>
	<button
		class="bg-purple-500 px-3"
		onclick={() => {
			console.log(next_song());
		}}
	>
		Next song
	</button>
</div>

<div>
	<button
		class="bg-purple-700 px-3"
		onclick={() => {
			console.log(prev_song());
		}}
	>
		Prev song
	</button>
</div>
<br />
<br />
<br />
<br />

<MusicPlayer
	class="mt-auto"
	section_class="contents"
	bind:cover_image_url
	bind:database
	bind:external_player_data
	{current_song_data}
/>

<GeneralLoading />
