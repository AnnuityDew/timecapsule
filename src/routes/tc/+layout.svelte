<div id="page-style">
<header><h1>TODO dynamic?</h1></header>
<main>
	<slot />
</main>

<footer>
	<p>
		To contact Mike Tarpey, type up an e-mail and send it to an old email address that no longer
		exists.
	</p>

	<p>
		<a href="/">Exit the time capsule</a>
	</p>
</footer>
</div>

<style>
	@import url(https://fonts.googleapis.com/css?family=Lato:700,400);

	#page-style {
		background: rgb(0,6,14); /* Old browsers */
		background: -moz-linear-gradient(left,  rgba(0,6,14,1) 0%, rgba(0,15,34,1) 17%, rgba(0,24,54,1) 33%, rgba(0,46,102,1) 67%, rgba(0,58,128,1) 83%, rgba(0,70,156,1) 100%); /* FF3.6+ */
		background: -webkit-gradient(linear, left top, right top, color-stop(0%,rgba(0,6,14,1)), color-stop(17%,rgba(0,15,34,1)), color-stop(33%,rgba(0,24,54,1)), color-stop(67%,rgba(0,46,102,1)), color-stop(83%,rgba(0,58,128,1)), color-stop(100%,rgba(0,70,156,1))); /* Chrome,Safari4+ */
		background: -webkit-linear-gradient(left,  rgba(0,6,14,1) 0%,rgba(0,15,34,1) 17%,rgba(0,24,54,1) 33%,rgba(0,46,102,1) 67%,rgba(0,58,128,1) 83%,rgba(0,70,156,1) 100%); /* Chrome10+,Safari5.1+ */
		background: -o-linear-gradient(left,  rgba(0,6,14,1) 0%,rgba(0,15,34,1) 17%,rgba(0,24,54,1) 33%,rgba(0,46,102,1) 67%,rgba(0,58,128,1) 83%,rgba(0,70,156,1) 100%); /* Opera 11.10+ */
		background: -ms-linear-gradient(left,  rgba(0,6,14,1) 0%,rgba(0,15,34,1) 17%,rgba(0,24,54,1) 33%,rgba(0,46,102,1) 67%,rgba(0,58,128,1) 83%,rgba(0,70,156,1) 100%); /* IE10+ */
		background: linear-gradient(to right,  rgba(0,6,14,1) 0%,rgba(0,15,34,1) 17%,rgba(0,24,54,1) 33%,rgba(0,46,102,1) 67%,rgba(0,58,128,1) 83%,rgba(0,70,156,1) 100%); /* W3C */
		font-family: Verdana, Geneva, Tahoma, sans-serif;
		color: #FFFFFF;
		background-color: #003092;
	}

	header {
		text-align: center;
	}

	footer {
		font-size: 75%;
		text-align: center;
	}

	a:link {color: #B3B3B3;}
	a:visited {color: #FFFFFF;}
	a:hover {color: #7e7e7e;}
	a:active {color: #FFFFFF;}

	img {
		max-width: 100%;
	}
</style>

