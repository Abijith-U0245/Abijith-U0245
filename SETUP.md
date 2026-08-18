# Setup guide

This repo is your GitHub profile README (`github.com/Abijith-U0245/Abijith-U0245`).
Follow these steps once to get every animation and live stat working.

## 1. Create/confirm the special repo
- Repo name must be **exactly** your username: `Abijith-U0245`
- Must be **public**
- If it doesn't exist yet: github.com/new → name it `Abijith-U0245` → check "Add a README" → create

## 2. Push these files
```bash
git clone https://github.com/Abijith-U0245/Abijith-U0245.git
cd Abijith-U0245
# copy everything from this folder (README.md, assets/, .github/) into that cloned folder
git add .
git commit -m "Revamp profile README"
git push
```

## 3. Enable Actions
- Go to the repo → **Settings → Actions → General**
- Under "Workflow permissions", select **Read and write permissions** → Save
- Go to the **Actions** tab → you should see "Generate Snake Animation" and "Generate Metrics"
- Click each → **Run workflow** (manual first run) so the `output` branch and `metrics.svg` get created

## 4. (Optional) Metrics token
The `metrics.yml` workflow can use the default `GITHUB_TOKEN` for public data.
If you want private repo stats included, create a Personal Access Token with `repo` scope,
then add it as a repo secret named `METRICS_TOKEN` (Settings → Secrets and variables → Actions → New repository secret).
If you skip this, just change `token: ${{ secrets.METRICS_TOKEN }}` to `token: ${{ secrets.GITHUB_TOKEN }}` in metrics.yml.

## 5. Double check
- Visit `github.com/Abijith-U0245` — your README should now show:
  - Hero banner + typing animation
  - Custom section header bars (from `assets/headers/`)
  - Skill card row (from `assets/skill-cards.svg`)
  - Live stats/streak/top-langs cards
  - Contribution snake animation (after the workflow's first run finishes — refresh in a minute)

## Notes
- All custom SVGs live in `assets/` — edit the Python-free SVG files directly, or regenerate with the included `gen_svgs.py` if you want to change colors/text (ask Claude to update it any time).
- The palette is Navy → Indigo → Accent (`#0F172A`, `#1E1B4B`, `#312E81`, `#4F46E5`, `#A5B4FC`) — consistent across every custom asset so it doesn't look stitched together.
