# Set up your CTRLGLITCH GitHub profile README

## 1. Open the right repository
1. Sign in to GitHub.
2. Open https://github.com/new
3. Create a **public** repository named exactly `ctrlglitch-arch` (your GitHub username).
4. Tick **Add a README file** if GitHub offers that option.

If you already have the special profile repository, use that one instead; do not create a duplicate.

## 2. Add the README
1. Download and extract `ctrlglitch_github_readme_bundle.zip`.
2. Open the included `README.md`.
3. In your profile repository, click `README.md` → pencil (Edit).
4. Replace the old contents with the new `README.md` contents.
5. Click **Commit changes**.

## 3. Upload the animation asset (required)
1. In the repository, click **Add file → Create new file**.
2. Name it `assets/ascii-blackhole.gif` (typing the slash creates the folder).
3. Open the included `assets/ascii-blackhole.gif` locally and upload it using **Add file → Upload files** instead if preferred.
4. Commit the file.

Important: the README references `assets/ascii-blackhole.gif`. The path and capitalization must match exactly.

## 4. Optional: regenerate or customize the animation
The ZIP includes `generate_ascii_blackhole.py`.
Install Python, then run:
    python -m pip install pillow
    python generate_ascii_blackhole.py

Run it from the extracted bundle's root folder. It writes `assets/ascii-blackhole.gif`.

## 5. Preview and troubleshoot
- Open your profile at https://github.com/ctrlglitch-arch
- If the GIF is missing, check that it exists at `assets/ascii-blackhole.gif`.
- External stats cards and icon services may occasionally fail; those are remote widgets, not GitHub data loss.
- GitHub READMEs do not support arbitrary JavaScript or CSS. The GIF loops automatically; hover-based 3D interactions need a separate website.
- Check that the links to LinkedIn, LeetCode and the CICR repository are correct before publishing.
- The stats services can take a little time to return data for a username/repository.

## Files
- `README.md` — updated, multicolor profile layout
- `assets/ascii-blackhole.gif` — looping multicolor ASCII art
- `generate_ascii_blackhole.py` — generator source
