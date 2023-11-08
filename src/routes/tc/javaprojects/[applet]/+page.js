import { applets } from '../data.js';

export function load({ params }) {
	const applet = applets.find((applet) => applet.slug === params.applet);
	return { ...applet };
}
