<script lang="ts">
	import { user_data } from '$lib/shared.svelte';
	import { cache_control, update_user_data } from '$lib/utils';
	import { onMount } from 'svelte';

	onMount(() => {
		const _user_data = cache_control({
			method: 'get',
			name: 'user_data'
		});
		const parsed_user_data = JSON.parse(_user_data as string);
		user_data.preferred_color = parsed_user_data.preferred_color;
		user_data.keep_gradient = parsed_user_data.keep_gradient;
		user_data.keep_image = parsed_user_data.keep_image;
		user_data.keep_dull = parsed_user_data.keep_dull;
		user_data.ahead = parsed_user_data.ahead;
		user_data.default_volume = parsed_user_data.default_volume;
	});

	$effect(() => {
		update_user_data(user_data);
	});
</script>

<title> Profile </title>
<section class="px-3 pr-3 pt-10 text-2xl md:pl-40">
	<h1>Profile Settings</h1>
	<br class="h-3 w-full bg-red-500" />
	<div class="flex flex-row gap-3">
		<label for="primary_color" class="text-base"> Primary Color </label>
		<input
			name="primary_color"
			type="color"
			bind:value={user_data.preferred_color}
			style="padding: 0px;"
		/>
	</div>
	<div>
		<label for="keep_dull" class="text-base">Keep background dull</label>
		<input name="keep_dull" type="checkbox" bind:checked={user_data.keep_dull} />
	</div>
	<div>
		<label for="keep_image" class="text-base">Keep Image</label>
		<input name="keep_image" type="checkbox" bind:checked={user_data.keep_image} />
	</div>
	<div>
		<label for="keep_gradient" class="text-base">Keep Gradient</label>
		<input name="keep_gradient" type="checkbox" bind:checked={user_data.keep_gradient} />
	</div>
	<br />
	<div class="flex flex-col">
		<label for="download_ahead" class="text-base"
			>Download Ahead<span class="text-sm"
				>&nbsp;(How many songs will be downloaded ahead for seamless playback; 1 should be fine)</span
			></label
		>
		<input
			name="download_ahead"
			class="w-fit text-base text-black"
			type="number"
			bind:value={user_data.ahead}
			min="0"
			max="10"
		/>
	</div>
</section>
