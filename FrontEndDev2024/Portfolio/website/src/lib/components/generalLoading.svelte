<script lang="ts">
	import cat_loading from '$lib/assets/images/cat-loading.gif';
	import { loading_song, other_loading } from '$lib/store';
	import Log from './log.svelte';

	let { override = false } = $props();

	$effect(() => {
		if ($other_loading) {
			document.body.style.overflow = 'hidden';
		} else {
			document.body.style.overflow = '';
		}
	});
</script>

{#if $other_loading || override}
	<div
		class="fixed left-0 top-0 z-50 flex h-screen w-screen flex-col items-center justify-center gap-3"
	>
		<h1 class="relative z-50 text-2xl font-bold">Loading...</h1>
		<img src={cat_loading} class="relative z-10 w-1/2 rounded-lg" alt="Loading" />
		<Log />
		<div
			class="absolute left-0 top-0 z-0 h-screen w-screen bg-black bg-opacity-80 backdrop-blur-sm"
		></div>
	</div>
{/if}
