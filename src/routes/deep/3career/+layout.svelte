<script>
	import FooterOne from '$lib/deep/FooterOne.svelte';
	import NavOne from '$lib/deep/NavOne.svelte';
</script>

<div class=".page-style" id="deep1-page-style">
	<NavOne />
	<slot />
	<FooterOne />
</div>

<style>
	#deep1-page-style {
		font-family: Verdana, Geneva, Tahoma, sans-serif;
		color: #000000;
		background-color: #00ff7f;
		padding: 8px;
	}
</style>
