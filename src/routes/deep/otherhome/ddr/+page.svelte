<script>
	import HeaderTwo from '$lib/deep/HeaderTwo.svelte';
	import NavTwo from '$lib/deep/NavTwo.svelte';

	import SeoDeep from '$lib/deep/SeoDeep.svelte';
</script>

<SeoDeep title="Mr. Man Inc. - Dance Dance Revolution" description="" />
<HeaderTwo text={'Dance Dance Revolution'} subtext={['DDR, MAX...Two!!!']} />
<main>
	<NavTwo />
	<hr />
	<p>
		Dance Dance Revolution. The coolest, healthiest video game ever to grace Earth. No, you don't
		use your thumbs (unless you're lazy :). You actually use your feet to hit arrows on a pad. You
		hit the arrow that is lined up with the outline on the screen. No idea what I'm talking about?
		Then check out <a href="https://www.ddrfreak.com">DDR Freak</a>. They have a much better site
		than mine. I'll be posting here a lot with my new pictures and resources, so check back often!
	</p>

	<nav>
		<table align="top">
			<tr>
				<td> DDR Stuff </td>
			</tr>

			<tr>
				<td>
					<a href="/deep/otherhome/ddr/pics">Pictures</a>
				</td>
			</tr>

			<tr>
				<td>
					<a href="/deep/otherhome/ddr/videos">Videos</a>
				</td>
			</tr>

			<tr>
				<td>
					<a href="/deep/otherhome/ddr/links">Links</a>
				</td>
			</tr>
		</table>
	</nav>
</main>
