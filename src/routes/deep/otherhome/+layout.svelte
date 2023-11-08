<script>
	import FooterTwo from '$lib/deep/FooterTwo.svelte';
</script>

<div class="page-style" id="deep2-page-style">
	<slot />
	<FooterTwo />
</div>

<style>
	#deep2-page-style {
		font-family: Verdana, Geneva, Tahoma, sans-serif;
		color: #000000;
		background-color: #00fa9a;
		padding: 8px;
	}
</style>
