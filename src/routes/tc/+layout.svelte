<script>
	import Header from '$lib/tc/Header.svelte';
	import Footer from '$lib/tc/Footer.svelte';
</script>

<div id="tc-page-style">
	<main>
		<slot />
	</main>

	<Footer />
</div>

<style>
	@import url(https://fonts.googleapis.com/css?family=Lato:700,400);

	#tc-page-style {
		background: rgb(0, 6, 14); /* Old browsers */
		background: -moz-linear-gradient(
			left,
			rgba(0, 6, 14, 1) 0%,
			rgba(0, 15, 34, 1) 17%,
			rgba(0, 24, 54, 1) 33%,
			rgba(0, 46, 102, 1) 67%,
			rgba(0, 58, 128, 1) 83%,
			rgba(0, 70, 156, 1) 100%
		); /* FF3.6+ */
		background: -webkit-gradient(
			linear,
			left top,
			right top,
			color-stop(0%, rgba(0, 6, 14, 1)),
			color-stop(17%, rgba(0, 15, 34, 1)),
			color-stop(33%, rgba(0, 24, 54, 1)),
			color-stop(67%, rgba(0, 46, 102, 1)),
			color-stop(83%, rgba(0, 58, 128, 1)),
			color-stop(100%, rgba(0, 70, 156, 1))
		); /* Chrome,Safari4+ */
		background: -webkit-linear-gradient(
			left,
			rgba(0, 6, 14, 1) 0%,
			rgba(0, 15, 34, 1) 17%,
			rgba(0, 24, 54, 1) 33%,
			rgba(0, 46, 102, 1) 67%,
			rgba(0, 58, 128, 1) 83%,
			rgba(0, 70, 156, 1) 100%
		); /* Chrome10+,Safari5.1+ */
		background: -o-linear-gradient(
			left,
			rgba(0, 6, 14, 1) 0%,
			rgba(0, 15, 34, 1) 17%,
			rgba(0, 24, 54, 1) 33%,
			rgba(0, 46, 102, 1) 67%,
			rgba(0, 58, 128, 1) 83%,
			rgba(0, 70, 156, 1) 100%
		); /* Opera 11.10+ */
		background: -ms-linear-gradient(
			left,
			rgba(0, 6, 14, 1) 0%,
			rgba(0, 15, 34, 1) 17%,
			rgba(0, 24, 54, 1) 33%,
			rgba(0, 46, 102, 1) 67%,
			rgba(0, 58, 128, 1) 83%,
			rgba(0, 70, 156, 1) 100%
		); /* IE10+ */
		background: linear-gradient(
			to right,
			rgba(0, 6, 14, 1) 0%,
			rgba(0, 15, 34, 1) 17%,
			rgba(0, 24, 54, 1) 33%,
			rgba(0, 46, 102, 1) 67%,
			rgba(0, 58, 128, 1) 83%,
			rgba(0, 70, 156, 1) 100%
		); /* W3C */
		font-family: Verdana, Geneva, Tahoma, sans-serif;
		color: #ffffff;
		background-color: #003092;
	}

	header {
		text-align: center;
	}

	:global(#tc-page-style a:link) {
		color: #b3b3b3;
	}
	:global(#tc-page-style a:visited) {
		color: #ffffff;
	}
	:global(#tc-page-style a:hover) {
		color: #7e7e7e;
	}
	:global(#tc-page-style a:active) {
		color: #ffffff;
	}

	img {
		max-width: 100%;
	}
</style>
