<script lang="ts">
	import { url_resolver } from '$lib/utils';
	import { has_account } from '$lib/store';
	import { PROD } from '$lib/shared.svelte';

	const scalar = 0.08;
</script>

<title> Home </title>
<div class="relative flex flex-col items-end gap-5 pr-5 pt-20">
	<svg
		width="15em"
		xmlns="http://www.w3.org/2000/svg"
		id="screenshot-f252f7ce-4e09-8002-8005-56f88667891f"
		viewBox="2198 679 493 264"
		style="-webkit-print-color-adjust::exact"
		xmlns:xlink="http://www.w3.org/1999/xlink"
		fill="none"
		version="1.1"
	>
		<style>
		</style>
		<g id="shape-f252f7ce-4e09-8002-8005-56f88667891f" rx="0" ry="0">
			<g id="shape-f252f7ce-4e09-8002-8005-56d427bfb4f7">
				<g
					transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
					class="text-container"
					x="2198"
					y="679"
					width="442"
					height="192"
					rx="0"
					ry="0"
				>
					<defs>
						<linearGradient
							id="fill-color-gradient-render-581-0-0"
							x1="0.5010242948485821"
							y1="0.08940397519146918"
							x2="0.5010242948485821"
							y2="0.9139073137882586"
							gradientTransform=""
						>
							<stop offset="0" stop-color="#ff0000" stop-opacity="1"> </stop>
							<stop offset="1" stop-color="#c7d834" stop-opacity="1"> </stop>
						</linearGradient>
						<pattern
							patternUnits="userSpaceOnUse"
							x="2198"
							y="679"
							width="441.09637451171875"
							height="232.86746215820312"
							id="fill-0-render-581-0"
						>
							<g>
								<rect
									width="441.09637451171875"
									height="232.86746215820312"
									style="fill:url(#fill-color-gradient-render-581-0-0)"
								>
								</rect>
							</g>
						</pattern>
					</defs>
					<g class="fills" id="fills-f252f7ce-4e09-8002-8005-56d427bfb4f7">
						<text
							x="2198"
							y="891.0481853485107"
							dominant-baseline="ideographic"
							textLength="441.09637451171875"
							lengthAdjust="spacingAndGlyphs"
							style="text-transform:none;font-family:&quot;Sirin Stencil&quot;;letter-spacing:normal;font-style:normal;font-weight:400;white-space:pre;font-size:160px;text-decoration:none solid rgba(0, 0, 0, 0);direction:ltr"
							fill="url(#fill-0-render-581-0)">音 Oto</text
						>
					</g>
				</g>
			</g>
			<g id="shape-f252f7ce-4e09-8002-8005-56f779b085d9">
				<g
					transform="matrix(1.000000, 0.000000, 0.000000, 1.000000, 0.000000, 0.000000)"
					class="text-container"
					x="2220"
					y="871"
					width="471"
					height="72"
					rx="0"
					ry="0"
				>
					<defs>
						<linearGradient
							id="fill-color-gradient-render-582-0-0"
							x1="0.5002175404498187"
							y1="0.08849557183116351"
							x2="0.5002175404498187"
							y2="0.9148230045877485"
							gradientTransform=""
						>
							<stop offset="0" stop-color="#c7d834" stop-opacity="1"> </stop>
							<stop offset="1" stop-color="#ff8800" stop-opacity="1"> </stop>
						</linearGradient>
						<pattern
							patternUnits="userSpaceOnUse"
							x="2220"
							y="871"
							width="470.795166015625"
							height="87.13253021240234"
							id="fill-0-render-582-0"
						>
							<g>
								<rect
									width="470.795166015625"
									height="87.13253021240234"
									style="fill:url(#fill-color-gradient-render-582-0-0)"
								>
								</rect>
							</g>
						</pattern>
					</defs>
					<g class="fills" id="fills-f252f7ce-4e09-8002-8005-56f779b085d9">
						<text
							x="2220"
							y="950.4216871261597"
							dominant-baseline="ideographic"
							textLength="470.795166015625"
							lengthAdjust="spacingAndGlyphs"
							style="text-transform:none;font-family:&quot;Sirin Stencil&quot;;letter-spacing:normal;font-style:normal;font-weight:400;white-space:pre;font-size:60px;text-decoration:none solid rgba(0, 0, 0, 0);direction:ltr"
							fill="url(#fill-0-render-582-0)">The Music Platform</text
						>
					</g>
				</g>
			</g>
		</g>
	</svg>
	{#if $has_account === false}
		<div class="mr-10 whitespace-nowrap">
			<a
				href={url_resolver() + 'signup' + (() => (PROD ? '.html' : ''))()}
				class="rounded bg-orange-500 px-3 py-1">Set up Account</a
			>
		</div>
	{/if}
	<p class="rounded bg-black bg-opacity-80 px-4 py-1 font-bold">
		Built with <a
			target="_blank"
			class="whitespace-nowrap rounded bg-orange-600 px-3 py-1 shadow-lg"
			href="https://svelte.dev/"
		>
			<svg
				xmlns="http://www.w3.org/2000/svg"
				class="inline"
				width={256 * scalar}
				height={308 * scalar}
				viewBox="0 0 256 308"
				><path
					fill="#ff3e00"
					d="M239.682 40.707C211.113-.182 154.69-12.301 113.895 13.69L42.247 59.356a82.2 82.2 0 0 0-37.135 55.056a86.57 86.57 0 0 0 8.536 55.576a82.4 82.4 0 0 0-12.296 30.719a87.6 87.6 0 0 0 14.964 66.244c28.574 40.893 84.997 53.007 125.787 27.016l71.648-45.664a82.18 82.18 0 0 0 37.135-55.057a86.6 86.6 0 0 0-8.53-55.577a82.4 82.4 0 0 0 12.29-30.718a87.57 87.57 0 0 0-14.963-66.244"
				/><path
					fill="#fff"
					d="M106.889 270.841c-23.102 6.007-47.497-3.036-61.103-22.648a52.7 52.7 0 0 1-9.003-39.85a50 50 0 0 1 1.713-6.693l1.35-4.115l3.671 2.697a92.5 92.5 0 0 0 28.036 14.007l2.663.808l-.245 2.659a16.07 16.07 0 0 0 2.89 10.656a17.14 17.14 0 0 0 18.397 6.828a15.8 15.8 0 0 0 4.403-1.935l71.67-45.672a14.92 14.92 0 0 0 6.734-9.977a15.92 15.92 0 0 0-2.713-12.011a17.16 17.16 0 0 0-18.404-6.832a15.8 15.8 0 0 0-4.396 1.933l-27.35 17.434a52.3 52.3 0 0 1-14.553 6.391c-23.101 6.007-47.497-3.036-61.101-22.649a52.68 52.68 0 0 1-9.004-39.849a49.43 49.43 0 0 1 22.34-33.114l71.664-45.677a52.2 52.2 0 0 1 14.563-6.398c23.101-6.007 47.497 3.036 61.101 22.648a52.7 52.7 0 0 1 9.004 39.85a51 51 0 0 1-1.713 6.692l-1.35 4.116l-3.67-2.693a92.4 92.4 0 0 0-28.037-14.013l-2.664-.809l.246-2.658a16.1 16.1 0 0 0-2.89-10.656a17.14 17.14 0 0 0-18.398-6.828a15.8 15.8 0 0 0-4.402 1.935l-71.67 45.674a14.9 14.9 0 0 0-6.73 9.975a15.9 15.9 0 0 0 2.709 12.012a17.16 17.16 0 0 0 18.404 6.832a15.8 15.8 0 0 0 4.402-1.935l27.345-17.427a52.2 52.2 0 0 1 14.552-6.397c23.101-6.006 47.497 3.037 61.102 22.65a52.68 52.68 0 0 1 9.003 39.848a49.45 49.45 0 0 1-22.34 33.12l-71.664 45.673a52.2 52.2 0 0 1-14.563 6.398"
				/></svg
			>
			Svelte 5</a
		>
		<a
			target="_blank"
			href="https://tailwindcss.com/"
			class="whitespace-nowrap rounded bg-blue-200 px-3 py-1 text-black shadow-lg"
		>
			<svg
				class="inline"
				xmlns="http://www.w3.org/2000/svg"
				width={256 * scalar}
				height={154 * scalar}
				viewBox="0 0 256 154"
				><defs
					><linearGradient id="logosTailwindcssIcon0" x1="-2.778%" x2="100%" y1="32%" y2="67.556%"
						><stop offset="0%" stop-color="#2298bd" /><stop
							offset="100%"
							stop-color="#0ed7b5"
						/></linearGradient
					></defs
				><path
					fill="url(#logosTailwindcssIcon0)"
					d="M128 0Q76.8 0 64 51.2Q83.2 25.6 108.8 32c9.737 2.434 16.697 9.499 24.401 17.318C145.751 62.057 160.275 76.8 192 76.8q51.2 0 64-51.2q-19.2 25.6-44.8 19.2c-9.737-2.434-16.697-9.499-24.401-17.318C174.249 14.743 159.725 0 128 0M64 76.8q-51.2 0-64 51.2q19.2-25.6 44.8-19.2c9.737 2.434 16.697 9.499 24.401 17.318C81.751 138.857 96.275 153.6 128 153.6q51.2 0 64-51.2q-19.2 25.6-44.8 19.2c-9.737-2.434-16.697-9.499-24.401-17.318C110.249 91.543 95.725 76.8 64 76.8"
				/></svg
			>
			Tailwind
		</a>
		and my hands.
	</p>
</div>
