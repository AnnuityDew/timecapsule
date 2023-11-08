<script lang="ts">
	export let title: string;
	export let description: string;
</script>

<svelte:head>
	<title>Mike Tarpey{title}</title>
	<meta NAME="Description" CONTENT={description} />
	<!-- these keywords were only added in the high school version of the site -->
	<meta NAME="Keywords" CONTENT="michael mike patrick tarpey college senior uconn irish landstown class of 2010" />
</svelte:head>
