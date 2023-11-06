<!-- {% extends 'tcdbase2.html' %} -->

<div id="page-style">
<main>
	<nav>
		<table>
			<tr>
				<td> Navigation </td>
			</tr>

			<tr>
				<td>
					<a href="/deep/otherhome">Home</a>
				</td>
			</tr>

			<tr>
				<td>
					<a href="/deep/ddr">Dance Dance Revolution</a>
				</td>
			</tr>

			<tr>
				<td>
					<a href="/deep/stepmania">StepMania</a>
				</td>
			</tr>

			<tr>
				<td>
					<a href="/deep/reviewsfaqs">Reviews & FAQs</a>
				</td>
			</tr>

			<tr>
				<td>
					<a href="/deep/schoolprojects">School Projects</a>
				</td>
			</tr>
		</table>
	</nav>
	<hr />
	<slot></slot>
</main>
<footer class="footertwo">
	<hr />
	<p>
		To contact me for absolutely <b>anything</b> about the site (improvements, glitches, broken
		links, add-ons, fan-mail, etc.) please e-mail me at an old email address that no longer exists.
		Absolutely all, and I mean <i>all</i> e-mails welcome (except for you spammers,of course. No offense,
		but I don't really like that stuff. (Heck, I don't even like the color of the can. Dark blue? C'mon,
		you can do better than that.))
	</p>

	<p>
		Wow, I got <i>way</i> off topic... :)
	</p>

	<p>
		<a href="/">Exit the time capsule</a>
	</p>
</footer>
</div>

<style>
    @import url(https://fonts.googleapis.com/css?family=Lato:700,400);

#page-style {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: #000000;
    background-color: #00FA9A;
}

.bodyone {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: #000000;
    background-color: #00FF7F;
}

.bodytwo {
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    color: #000000;
    background-color: #00FA9A;
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
