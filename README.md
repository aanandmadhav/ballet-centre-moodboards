# The Ballet Centre — Website Mood Boards

Two contrasting design directions for the new website, as a small static site you can host and share live.

- `index.html` — landing page linking both directions
- `direction-a-timeless-stage.html` — Direction A (heritage / elegant)
- `direction-b-the-programme.html` — Direction B (bold / colour-coded)
- `images/` — generated imagery + `logo.webp`
- `generate_assets.py` — regenerates the imagery via Imagen 4.0

Client: The Ballet Centre (Dubai) · Performing Art School · Est 1986
Prepared for: Yamu Media

---

## View locally

Open `index.html` in a browser, or run a local server from this folder:

```bash
cd ballet-centre-moodboards
python3 -m http.server 8000
# then open http://localhost:8000
```

---

## Publish a live link with GitHub Pages

1. Create a new GitHub repo (e.g. `ballet-centre-moodboards`).
2. From this folder:

   ```bash
   git init
   git add .
   git commit -m "Ballet Centre mood boards v1"
   git branch -M main
   git remote add origin https://github.com/<your-username>/ballet-centre-moodboards.git
   git push -u origin main
   ```

3. On GitHub: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, pick `main` / `/ (root)`, Save.
4. Wait ~1 minute. Your live link is:

   `https://<your-username>.github.io/ballet-centre-moodboards/`

Share that URL. Direction pages are at `/direction-a-timeless-stage.html` and `/direction-b-the-programme.html`.

> Tip: keep the repo **private** if you'd rather the client only sees the link, not the source. Pages still works on private repos for the deployed site.

---

## Regenerate or change the imagery

The key is read from `Brain/utilities/.env` (`GEMINI_API_KEY`).

```bash
python3 generate_assets.py
```

- Edit the prompts in `generate_assets.py` to change any shot.
- Bump `VERSION = "v1"` to `"v2"` so new files sit next to the old ones instead of overwriting, then update the `-v1` references in the HTML.

---

## How to iterate on the boards

Everything is plain HTML + CSS with no build step, so edits are direct:

- **Colours** live in the `:root { --var }` block at the top of each page. Change a hex there and it updates everywhere.
- **Type** is loaded from Google Fonts in the `<head>` `<link>`. Swap a family name in both the link and the CSS to try a different voice.
- **Copy / taglines** are inline in the HTML — search for the text and edit.
- **Images** are in `images/`; replace a file (keep the name) or point the `src` at a new one.

### Likely next moves
1. Client picks a direction from the live link.
2. On the winner: refine palette + type into real design tokens.
3. Build out full page comps (Home, About, Classes, Timetable) in Figma or code.
4. Develop the WordPress theme.
