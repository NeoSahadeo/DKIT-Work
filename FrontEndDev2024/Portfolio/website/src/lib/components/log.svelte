<script lang="ts">
	import { logger } from '$lib/store';
</script>

<div class="relative z-10 max-h-32 w-1/2 overflow-y-scroll bg-black px-3">
	<h2>Logs:</h2>
	{#each $logger as [] as log}
		<p>
			{log}
		</p>
	{/each}
</div>
