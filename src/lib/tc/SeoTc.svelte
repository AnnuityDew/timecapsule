<script lang="ts">
	export let title: string;
	export let description: string;
</script>

<svelte:head>
	<title>Mike Tarpey{title}</title>
	<meta NAME="Description" CONTENT={description} />
	<meta name="author" content="Mike Tarpey" />
	<meta name="viewport" content="width=device-width, initial-scale=1.0" />
	<meta NAME="Keywords" CONTENT="michael mike patrick tarpey college senior uconn irish landstown class of 2010" />
	<!-- favicon stuff -->
	<meta name="msapplication-TileColor" content="#2d89ef" />
	<meta name="theme-color" content="#ffffff" />
	<link rel="apple-touch-icon" sizes="180x180"
	  href="/index/favicon/apple-touch-icon.png" />
	<link rel="icon" type="image/png" sizes="32x32"
	  href="/index/favicon/favicon-32x32.png" />
	<link rel="icon" type="image/png" sizes="16x16"
	  href="/index/favicon/favicon-16x16.png" />
	<link rel="manifest" href="/index/favicon/site.webmanifest" />
	<link rel="mask-icon" href="/index/favicon/safari-pinned-tab.svg" color="#5bbad5" />
	<link rel="shortcut icon" href="/index/favicon/favicon.ico" />
</svelte:head>
