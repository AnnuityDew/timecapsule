# timecapsule

Time capsule for miketarpey.com. We've come a long way since 2006...

### Reference

- Run `npm install` after cloning
- `npm run dev` to test locally
- Build a static site for S3 deployment by installing the static adapter: `npm i -D @sveltejs/adapter-static` (code added to `svelte.config.js` and the root `+layout.js`)
- `npm run build` to compile static site
- `aws s3 cp source destination` to update S3 (for now)

### Notes

- "Greener" code
- Looked at zola, didn't quite fit (reliance on Markdown)
- Lots of `url_for` rewrites
- Made routing better (nested folders); one html file for many awards. [Tutorial was great here.](https://learn.svelte.dev/tutorial/layout-data)
- Templates -> reusable components
- 500MB Docker container -> instant static pages
- [static adapter](https://kit.svelte.dev/docs/adapter-static)
- S3 config (updating infra, [trailing slash](https://kit.svelte.dev/docs/page-options#trailingslash))
- [No capitalized tags allowed!](https://svelte.dev/docs/basic-markup#tags)
- Component refactors into `lib`
- Figuring out styling
- SEOally
- HTTP redirect loop!? https://developers.cloudflare.com/ssl/troubleshooting/too-many-redirects/#encryption-mode-misconfigurations
- Prevent bounce with [this](https://stackoverflow.com/questions/29894997/prevent-ios-bounce-without-disabling-scroll-ability) and [this](https://stackoverflow.com/questions/32500876/how-to-prevent-white-space-bounce-after-scrolling-to-the-top-of-the-page-and-t)
- TODO analytics? html lang? hourglass favicon? remaining templates need a home
