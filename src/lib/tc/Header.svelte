<script lang="ts">
	export let text: string = "";
	export let subtext: string[] = [];
	export let imgfile: string = "";
	export let imgwidth: number = 0;
	export let imgheight: number = 0;
	export let nav: boolean = false;
	import Nav from "./Nav.svelte";
</script>

<header><h1>{text}</h1>
{#if subtext}
{#each subtext as subheader}
<h4>{subheader}</h4>
{/each}
{/if}
{#if nav}<Nav/>{/if}
{#if imgfile}<img src="/timecapsule/images/{imgfile}" width={imgwidth || null} height={imgheight || null}>{/if}
</header>

<style>
	header {
		text-align: center;
	}
</style>
