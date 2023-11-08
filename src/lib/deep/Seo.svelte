<script lang="ts">
	export let title: string;
	export let description: string;
</script>

<svelte:head>
	<title>{title}</title>
	<meta NAME="Description" CONTENT={description} />
</svelte:head>
