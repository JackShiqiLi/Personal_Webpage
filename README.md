# Shiqi Li — academic website

A static adaptation of [hollina/template-job-market-website](https://github.com/hollina/template-job-market-website) for GitHub Pages. It preserves the selected template's Academic theme appearance by reusing its `public/css/academic.css` unchanged as `assets/academic.css`, with small local overrides.

The site uses ordinary HTML, CSS, and JavaScript. No R or Python runtime, npm installation, or build step is required to publish it. The repository root should contain this directory's files.

## Files and local preview

- `index.html`: biography, research, teaching, and contact content.
- `assets/academic.css`: the selected template's original Academic theme stylesheet.
- `assets/academic-LICENSE.txt`: retained MIT copyright and license notice for the theme.
- `assets/bootstrap-LICENSE.txt`: MIT license for Bootstrap, included in the theme stylesheet.
- `styles.css`: small local overrides and responsive adjustments.
- `site.js`: accessible mobile navigation.
- `.nojekyll`: serves the files directly through GitHub Pages.
- `files/CV_ShiqiLi.pdf`: downloadable academic CV.
- `ShiqiLi_photo.jpg`: supplied portrait; displayed with a CSS crop while the image file remains unchanged.

For an optional local preview, run this command from this directory. Python serves the static files locally; it is not part of the deployed website.

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open [the local preview](http://127.0.0.1:8000). Stop the server with `Ctrl+C`.

## GitHub repository and publishing

Use the existing repository [JackShiqiLi/Personal_Webpage](https://github.com/JackShiqiLi/Personal_Webpage). Add this directory's contents at the repository root and commit/push to `main`.

GitHub Pages is enabled and the website is live at [jackshiqili.github.io/Personal_Webpage/](https://jackshiqili.github.io/Personal_Webpage/). Its publishing source is `main` and `/(root)`. Pushing changes to `main` triggers a new deployment and updates the published site.

To review or restore the publishing settings:

1. Open **Repository Settings → Pages**. Under **Build and deployment**, select **Deploy from a branch**, then **main** and **/(root)**, and save.
2. Wait for deployment and check [the default project-site address](https://jackshiqili.github.io/Personal_Webpage/), including navigation and the CV download.

See [GitHub's publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site).

## Connect the preferred domain

The intended domain is `shiqi-li.com`; it has not been purchased. Domain registration and renewal are separate from GitHub Pages hosting. Confirm availability and the renewal price with the chosen registrar before registering it.

Once the domain is owned:

1. Open **GitHub account Settings → Pages → Add a domain** and enter `shiqi-li.com`. Add the exact **TXT** record GitHub supplies to the domain's DNS settings, then click **Verify**. Keep this TXT record. This is an account setting, separate from the repository setting.
2. Open **Repository Settings → Pages → Custom domain**, enter `shiqi-li.com`, and save **before** adding the routing records below. For branch deployment, GitHub creates a `CNAME` file containing the domain; pull that commit into the local checkout before the next push. Do not create a `CNAME` file or configure the custom domain before ownership is established.
3. At the DNS provider, configure these records. `@` means the bare domain; providers may label it differently.

| Type | Name | Value |
| --- | --- | --- |
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| CNAME | `www` | `JackShiqiLi.github.io` |

The CNAME target remains `JackShiqiLi.github.io`: it contains no protocol or path, including no `/Personal_Webpage/` suffix. Replace conflicting web-hosting records for these names while preserving unrelated records, including email records and the verification TXT record. Do not add a wildcard record. GitHub supports an apex `ALIAS` or `ANAME` record as an alternative to the four A records if the DNS provider offers it.

4. After DNS and certificate provisioning complete, enable **Enforce HTTPS** in the repository's Pages settings. DNS propagation and HTTPS availability can take up to 24 hours.
5. Check both `https://shiqi-li.com` and `https://www.shiqi-li.com`. With the bare domain selected as the custom domain, GitHub redirects `www` to it. Update the website's canonical/social metadata, sitemap if added, and CV website address to the final domain.

Official references: [domain verification](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/verifying-your-custom-domain-for-github-pages), [custom-domain and DNS setup](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site), and [HTTPS](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https).

## Maintain the content

| To change | Edit |
| --- | --- |
| Website words, headings, links, browser title, and meta descriptions | `index.html` |
| Colors, spacing, typography, layout, and portrait crop | `styles.css` |
| Downloadable CV | Replace `files/CV_ShiqiLi.pdf` |
| Profile portrait | Replace `ShiqiLi_photo.jpg` |
| Setup and maintenance instructions | `README.md`; this text is not rendered on the website |

In `index.html`, find the relevant section by its ID: `about` (biography and education), `research`, `work-in-progress`, `teaching`, or `contact`. Edit the words between HTML tags while preserving the tags and section IDs. For a link, change its `href` value to change the destination; change the text between `<a>` and `</a>` to change its label. The browser title and meta descriptions are near the top of the file in `<head>`.

Keep the reused `assets/academic.css` unchanged and retain its MIT notice when copying or distributing the site. Replace the CV and portrait at the same filenames to preserve their links. Preview changes at desktop and phone widths, check keyboard and mobile navigation, links, and downloads, then commit and push to `main`. With the current Pages configuration, pushes to `main` republish the site.

Biographical, education, research, and teaching information is drawn from the existing Google Site and academic CV. Keep paper titles, authors, statuses, dates, and research claims consistent with those sources. The profile uses the supplied `ShiqiLi_photo.jpg`; its displayed crop is controlled by CSS without modifying the original image. A job-market-paper PDF was not available for this draft; add a paper download only when the actual PDF is supplied.

The CV was copied unchanged from the workspace's `Academic/CV_ShiqiLi.pdf` and still includes the old Google Site URL. Update the source CV and replace the website copy once the canonical domain is finalized.

After launch, update links in academic profiles and application materials, and leave a prominent migration notice on the old Google Site so existing links remain useful.
