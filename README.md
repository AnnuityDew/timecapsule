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
- Made routing better (nested folders); one html file for many awards
- Templates -> reusable components
- 500MB Docker container -> instant static pages
- static adapter
- S3 config (updating infra)