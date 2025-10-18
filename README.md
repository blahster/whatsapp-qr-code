# WhatsApp QR Generator (India +91)

A lightweight, single-file web page that generates a scannable QR code for WhatsApp’s click-to-chat link using an Indian phone number. Enter a 10-digit number and it creates a QR for: `https://wa.me/91<number>`.

## Features

- Single HTML file—no build, no backend
- Clean UI with a responsive, square QR canvas
- Digits-only input and Enter-to-generate
- Error correction level Q (robust for screenshots/printing)
- Copy URL and Download PNG actions
- Autofocus on the phone input for fast entry

## Live Demo

You can host with GitHub Pages or any static host. Example URL format:

```
https://blahster.github.io/whatsapp-qr-code
```

## Usage

1. Open `index.html` in any modern browser.
2. Type a 10-digit Indian mobile number (e.g., 9876543210).
3. Press Enter or click “Generate”.
4. Use “Copy URL” to copy the WhatsApp link or “Download PNG” to save the QR.

## How it works

- Builds the link: `https://wa.me/91<10-digit-number>`
- Uses a QR library (QRCode.js) to generate the matrix
- Renders the QR to a square HTML5 canvas with a proper white quiet zone and crisp scaling

## Project structure

```
.
├─ index.html        # Single-page app (or wa-qr.html)
└─ README.md         # This file
```

## Hosting with GitHub Pages

1. Create a new GitHub repository (e.g., `wa-qr`) and add `index.html`.
2. Commit and push:
   - `git init`
   - `git add index.html`
   - `git commit -m "Initial commit: WhatsApp QR page"`
   - `git branch -M main`
   - `git remote add origin https://github.com/<your-username>/wa-qr.git`
   - `git push -u origin main`
3. Enable Pages: Repo → Settings → Pages → Source: “Deploy from a branch” → Branch: `main` → Folder: `/root`.
4. Open your site at `https://<your-username>.github.io/wa-qr`.

## Notes on QR quality

- Keep error correction at Q (or H for maximum tolerance) for better readability in screenshots or prints.
- Ensure the canvas is square:
  - Intrinsic size: `width="480"` and `height="480"`
  - CSS: set `width` and avoid fixed `height` unless it matches width.
- Use image smoothing disabled to keep modules crisp.

## Customization

- Change the country code:
  - Update the builder function to `https://wa.me/<country_code><number>`.
- Prefill a message:
  - Append `?text=Your%20Message` to the link.
- Styles:
  - Tweak colors, spacing, and card layout in the `<style>` section.

## Local development

- Open the HTML file directly in your browser, or serve it with a simple static server:
  - Python: `python -m http.server`
  - Node: `npx serve`
- Edit in VS Code; changes are instant on refresh.

## License

MIT — do whatever you like with attribution.
