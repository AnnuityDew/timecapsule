<script lang="ts">
	export let text: string = "";
	export let subtext: string[] = [];
	export let imgfile: string = "";
	export let imgwidth: number = 0;
	export let imgheight: number = 0;
</script>

<header>
    <h1>{text}</h1>
	{#if subtext}
	{#each subtext as subheader}
	<h5>{subheader}</h5>
	{/each}
	{/if}
	{#if imgfile}<img src="/timecapsuledeep/images/{imgfile}" width={imgwidth || null} height={imgheight || null}>{/if}
</header>

<style>
    header {
		text-align: center;
	}
</style>