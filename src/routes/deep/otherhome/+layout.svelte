<script>
	import FooterTwo from "$lib/deep/FooterTwo.svelte";
</script>

<div class=".page-style" id="deep2-page-style">
	<slot />
	<FooterTwo/>
</div>

<style>
	@import url(https://fonts.googleapis.com/css?family=Lato:700,400);

	#deep2-page-style {
		font-family: Verdana, Geneva, Tahoma, sans-serif;
		color: #000000;
		background-color: #00fa9a;
	}

	.bodyone {
		font-family: Verdana, Geneva, Tahoma, sans-serif;
		color: #000000;
		background-color: #00ff7f;
	}

	table {
		border: 1;
	}

	.footerone {
		font-size: 75%;
		text-align: left;
	}

	.footertwo {
		font-size: 75%;
		text-align: center;
	}

	img {
		max-width: 100%;
	}
</style>
