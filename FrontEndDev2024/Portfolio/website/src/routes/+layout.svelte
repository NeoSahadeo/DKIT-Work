<script lang="ts">
	import '../app.css';
	import './home.css';
	import { onMount } from 'svelte';
	import { cache_control, load_user_data } from '$lib/utils';
	import Navigation from '$lib/components/navigation.svelte';
	import GeneralLoading from '$lib/components/generalLoading.svelte';
	import OtoLogo from '$lib/components/otoLogo.svelte';
	import { url_resolver } from '$lib/utils';
	import { user_data } from '$lib/shared.svelte';
	import { has_account, is_mobile } from '$lib/store';
	import { PROD } from '$lib/shared.svelte';

	let { children } = $props();
	let current_url = $state();

	$effect(() => {
		user_data;
		update_nav();
	});

	const update_nav = () => {
		let _has_account = cache_control({
			method: 'get',
			name: 'user_data'
		});
		if (_has_account === undefined) {
			has_account.set(false);
		} else {
			has_account.set(true);
		}
	};

	onMount(() => {
		update_nav();
		const data = load_user_data();
		if (data === null) {
			if (window.location.href === url_resolver() + 'signup' + (() => (PROD ? '.html' : ''))())
				return; // If on signup dont go back
			if (window.location.href !== url_resolver()) window.location.href = url_resolver();
		} else if (
			data !== null &&
			window.location.href === url_resolver() + 'signup' + (() => (PROD ? '.html' : ''))()
		) {
			window.location.href = cache_control({ method: 'get', name: 'current_page' }) as string;
		}
		current_url = window.location.href;

		if (window.innerWidth <= 640) {
			is_mobile.set(true);
		} else {
			is_mobile.set(false);
		}

		window.addEventListener('resize', (e) => {
			if (window.innerWidth >= 640) {
				is_mobile.set(false);
			} else {
				is_mobile.set(true);
			}
		});
	});
</script>

{#if $has_account === true}
	<Navigation />
{/if}
{#if current_url === url_resolver()}
	<div id="background_image" style="position: fixed;"></div>
{:else}
	<OtoLogo class="mx-auto mt-3 w-fit" />
	<GeneralLoading />
	<div id="background_darken" style="position: fixed;"></div>
	<div id="background_image_blur" style="position: fixed;"></div>
{/if}
<div id="background_gradient" style="position: fixed;"></div>

{@render children()}
