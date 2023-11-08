<script lang="ts">
	export let title: string;
	export let description: string;
</script>

<svelte:head>
	<title>Mike Tarpey{title}</title>
	<meta NAME="Description" CONTENT={description} />
</svelte:head>
