import { awards } from '../data.js';

export function load({ params }) {
	const award = awards.find((award) => award.slug === params.slug);
	return { ...award };
}