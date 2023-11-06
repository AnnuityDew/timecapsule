<!-- {% extends 'base.html' %}

{% block description %}
<meta name="description" content="Mike Tarpey's website time capsule.
The site has changed a lot throughout the years...pages from the past
can be viewed here!">
{% endblock %}

{% block title %} - time capsule{% endblock %}

{% block header %}time capsule{% endblock %} -->
<div id="page-style">
	<main>
		<p>This is the time capsule.</p>

		<p>
			I bought tarpey.dev with the primary goal of improving my programming skills by building out
			some small apps...but I haven't lost sight of the fact that my website used to be an important
			portal for me to express what I was feeling (especially during an emotionally turbulent high
			school and college career). I think it makes sense for me to give these pages I built during
			my academic career a place of their own.
		</p>

		<p>
			Just about everything contained within is untouched since the last iteration of
			michaeltarpey.com (probably since 2013 or so). The high school pages are even older than that.
			I scrubbed each page for inactive email addresses and old scripts before uploading.
		</p>

		<p>
			<b class="bold_warning"
				>Some links won't work, and the profile information is obviously pretty dated.</b
			>
			If you're looking for my up-to-date resume, you can visit
			<a class="inline" href="https://www.linkedin.com/in/mptarpey/">LinkedIn</a>.
		</p>

		<p>
			There are three hidden pages that are only accessible by typing in the correct URL. (From what
			I can tell, this is intended behavior from past me. I was still uploading HTML templates for
			these pages, but there are no links to them within the site.)
		</p>

		<p>With all that said...</p>

		<div class="button-div">
			<a href="/tc">
				<sl-button class="sl-blue-button" size="large" style="width: 100%"
					>Click here to enter the time capsule!</sl-button
				>
			</a>
		</div>
		<div class="button-div">
			<a href="/deep">
				<sl-button class="sl-red-button" size="large" style="width: 100%"
					>Wait...there's ANOTHER time capsule?</sl-button
				>
			</a>
		</div>
	</main>
</div>

<style>
	@import url(https://fonts.googleapis.com/css?family=Lato:700,400);

	/* most of the site*/
	:global(*) {
		box-sizing: content-box;
	}

	:global(html) {
		overflow: hidden;
		height: 100%;
	}

	:global(body) {
		margin: 0;
		overflow: auto;
		height: 100%;
	}

	:global(#page-style) {
		overflow: auto;
		min-height: 100vh;
	}

	main {
		max-width: 800px;
		padding-left: 20px;
		padding-right: 20px;
		margin-left: auto;
		margin-right: auto;
		text-align: left;
	}

	#page-style {
		font-family: 'Lato', sans-serif;
		background-color: #000000;
		color: #ffffff;
		font-size: 24px;
		margin: 0px;
	}

	.button-div {
		padding: 10px 0px;
	}

	/* shoelace light button */
	.sl-blue-button::part(base) {
		background: rgba(0, 195, 255, 0.3);
		border: solid 2px rgba(0, 195, 255, 1);
		font-weight: 700;
	}

	.sl-blue-button::part(base):hover {
		background: rgba(0, 195, 255, 0.4);
	}

	.sl-blue-button::part(base):active {
		background: rgba(0, 195, 255, 0.2);
	}

	.sl-blue-button::part(base):focus {
		box-shadow: 0 0 0 3px rgba(0, 195, 255, 0.33);
	}

	.sl-blue-button::part(label) {
		font-family: 'Lato', sans-serif;
		color: rgb(255, 255, 255);
		font-size: 20px;
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

	a.inline {
		background-color: #000000;
	}
	a.inline:link {
		color: #66d9ff;
	}
	a.inline:visited {
		color: #ffe066;
	}
	a.inline:hover {
		color: #99e6ff;
	}
	a.inline:active {
		color: #99e6ff;
	}
</style>
