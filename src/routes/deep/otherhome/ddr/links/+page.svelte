<script>
	import HeaderTwo from '$lib/deep/HeaderTwo.svelte';
	import NavTwo from '$lib/deep/NavTwo.svelte';

	import Seo from '$lib/deep/SeoDeep.svelte';
</script>

<Seo title="Mr. Man Inc. - Dance Dance Revolution" description="" />
<HeaderTwo text={'Dance Dance Revolution'} subtext={['DDR, MAX...Two!!!']} />
<main>
	<NavTwo />
	<hr />
	<p>Here's all the DDR links I can come up with. I'll try to find new links whenever I can.</p>

	<hr />

	<table>
		<tr>
			<td>
				<a href="https://www.ddrfreak.com">DDR Freak</a> - I already told you about this one.
			</td>
		</tr>

		<tr>
			<td>
				<a href="https://www.ddruk.com">DDR UK</a> - This is a great site for official DDR stepfiles
				for StepMania. (And if you're interested in the European version of DDR.)
			</td>
		</tr>

		<tr>
			<td>
				<a href="https://www.ddrecall.com">DDRecall</a> - Play at the arcade? Post your scores here and
				compare to the world!
			</td>
		</tr>

		<tr>
			<td>
				<a href="https://www.ddrhometracker.com">DDR Home Tracker</a> - The home version equivalent of
				DDRecall.
			</td>
		</tr>
	</table>
</main>
