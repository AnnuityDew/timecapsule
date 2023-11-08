<script>
	import Header from '$lib/tc/Header.svelte';
	import Seo from '$lib/tc/SeoTc.svelte';
	export let data;
</script>

<Seo
	title="'s High School Career"
	description="This is Mike Tarpey's high school career page, featuring all of his accomplishments as a member of Landstown High School's Class of 2010."
/>
<Header
	text="Mike Tarpey"
	subtext={['Valedictorian, Class of 2010']}
	imgfile="gradpic.jpg"
	imgheight={500}
	imgwidth={250}
/>

<main>
	<p>
		<b><u>High School Resume</u></b><br />
		-Basic Technical Drawing (1 year)<br />
		-Engineering Drawing (1 year)<br />
		-Architectural Drawing (1 year)<br />
		-Digital Visualization (1 year, in progress)<br />
		-AP European History (1 year, 3 - Qualified)<br />
		-AP Computer Science [Java, projects can be found <a href="/tc/javaprojects">here</a>] (1 year,
		5 - Extremely Well Qualified)<br />
		-AP English Language & Composition (1 year, 4 - Well Qualified)<br />
		-AP US History (1 year, 3 - Qualified)<br />
		-AP Calculus BC (1 year, 5 - Extremely Well Qualified)<br />
		-AP Statistics (1 year, 5 - Extremely Well Qualified)<br />
		-AP English Literature & Composition (1 year, 4 - Well Qualified)<br />
		-AP US Government (1 year, 5 - Extremely Well Qualified)<br />
		-AP Physics C (1 year, 4 - Well Qualified)<br />
		-AP Macroeconomics (1 year, 5 - Extremely Well Qualified)<br />
		-AP Microeconomics (1 year, 4 - Well Qualified)<br />
		-Japanese Language (4 years)<br />
		-<a href="/tc/portfolio07">Freshman English Digital Portfolio</a><br />
		-<a href="https://oddfod.net/portfolio/2008/4B/92/">Sophomore English Digital Portfolio</a><br
		/>
		-<a href="/tc/portfolio09">Junior English Digital Portfolio</a><br />
		-<a href="/tc/portfolio10">Senior English Digital Portfolio</a><br />
	</p>

	<p>
		<b><u>Grade School Achievements & Awards</u></b><br />
		-<a href="/tc/diploma"
			>Graduated as Valedictorian of Landstown High School's Class of 2010, with a 4.5368 GPA</a
		><br />
		-Former member of Landstown High School's chapter of the National Honor Society<br />
		-Former member of Landstown High School's chapter of the Japanese National Honor Society<br />
		-Attending the University of Connecticut in the fall of 2010, on an Academic Excellence Scholarship<br
		/>
		-National Merit Scholar for 2010 (Walgreen Co. Scholarship)<br />
		-Best SAT scores: 690 Reading (March 2009), 800 Math (November 2009), 760 Writing (March 2009), 2250
		overall<br />
		-2190 on the March 14th, 2009 SAT - 690 Reading, 740 Math, 760 Writing (10/12 Essay)<br />
		-2170 on the November 7th, 2009 SAT - 670 Reading, 800 Math, 700 Writing (8/12 Essay)<br />
		-33/36 on the October 24th, 2009 ACT - 34 English, 35 Math, 33 Reading, 31 Science, 30 Combined English/Writing
		(7/12 Essay) <br />
		-Terrific Tiger Award (Straight As) 1st through 5th Grade<br />
		-Duke TIP Recognition in 2005 for SAT Score (1150/1600)<br />
		-Landstown Middle School Class of 2006 Shield of Distinction<br />
		-President's Student Service Award for 2006<br />
		{#each data.awards as { slug, title }}
			-<a href="/tc/mths/{slug}">{title}</a><br />
		{/each}
		-National AP Scholar for 2010<br />
	</p>
</main>
