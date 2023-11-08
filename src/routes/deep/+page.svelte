<script>
	import Seo from '$lib/tc/Seo.svelte';
</script>

<Seo
	title="'s DEEP time capsule"
	description="Mike Tarpey's website time capsule: Deep Edition.
	The site has changed a lot throughout the years...pages from the DEEP past
	can be viewed here!"
/>

<div class="page-style" id="deep-home-page-style">
	<header>
		<h1>time capsule deep</h1>
	</header>
	<main>
	<p>"This isn't just any time capsule. This is...the ADVANCED time capsule."</p>

	<p>Written entirely in my 8th grade Advanced Computers class (shoutout to Mrs. Potter).</p>

	<p>
		<b class="bold_warning">You've been warned.</b>
	</p>

	<div class="button-div">
		<a href="/deep/otherhome">
			<sl-button class="sl-red-button" size="large" style="width: 100%"
				>Click here to enter!</sl-button
			>
		</a>
	</div>
</main>
</div>

<style>
	@import url(https://fonts.googleapis.com/css?family=Lato:700,400);

	#deep-home-page-style {
		font-family: 'Lato', sans-serif;
		background-color: #000000;
		color: #ffffff;
		font-size: 24px;
		margin: 0px;
	}

	header, main {
		max-width: 800px;
		padding-left: 20px;
		padding-right: 20px;
		margin-left: auto;
		margin-right: auto;
		text-align: left;
	}

	.button-div {
		padding: 10px 0px;
	}

	/* shoelace red button */
	.sl-red-button::part(base) {
		background: rgba(241, 101, 101, 0.3);
		border: solid 2px rgb(241, 101, 101);
		font-weight: 700;
	}

	.sl-red-button::part(base):hover {
		background: rgba(241, 101, 101, 0.4);
	}

	.sl-red-button::part(base):active {
		background: rgba(241, 101, 101, 0.2);
	}

	.sl-red-button::part(base):focus {
		box-shadow: 0 0 0 3px rgba(241, 101, 101, 0.33);
	}

	.sl-red-button::part(label) {
		font-family: 'Lato', sans-serif;
		color: rgb(255, 255, 255);
		font-size: 20px;
	}

	.bold_warning {
		color: #ffa0e1;
	}
</style>
