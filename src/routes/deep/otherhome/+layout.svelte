<script>
	import HeaderTwo from "$lib/deep/HeaderTwo.svelte";
	import FooterTwo from "$lib/deep/FooterTwo.svelte";
</script>
<!-- {% extends 'tcdbase2.html' %} -->

<div class=".page-style" id="deep2-page-style">
	<HeaderTwo/>
	<hr />
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

	.bodytwo {
		font-family: Verdana, Geneva, Tahoma, sans-serif;
		color: #000000;
		background-color: #00fa9a;
	}

	header {
		text-align: center;
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
