<script>
	import SeoTc from '$lib/tc/SeoTc.svelte';

	export let data;
</script>

<SeoTc
	title=", High School Senior - {data.appletName}"
	description="Landstown High School, Virginia Beach, VA, USA."
/>
<main>
	<p>
		The {data.appletName} applet would be showing here, but the applet tag is unfortunately dead in HTML5. RIP!
	</p>
    <applet code="/timecapsule/applets/{data.appletFile}" width=500 height=500></applet>
</main>

