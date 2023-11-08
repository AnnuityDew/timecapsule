<script lang="ts">
	export let text: string = "";
	export let subtext: string[] = [];
</script>

<header>
    <h1>{text}</h1>
	{#if subtext}
	{#each subtext as subheader}
	<h5>{subheader}</h5>
	{/each}
	{/if}
</header>

<style>
    header {
		text-align: center;
	}
</style>