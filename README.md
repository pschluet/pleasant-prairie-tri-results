# Pleasant Prairie Triathlon 2026 — Results

Results explorer and data scraper for the 2026 Pleasant Prairie Olympic Triathlon.

## Results Explorer

Open `index.html` in a browser (no server needed — double-click to open from `file://`).

Requires an internet connection to load the D3 charting library from CDN.

**Features:**
- Kernel density estimate (KDE) distributions for all 6 race segments: Swim, T1, Bike, T2, Run, and Overall. Each plot shows a faint full-field curve and a bold filtered-subset curve for comparison.
- Filter by gender, age range, primary division, and secondary division.
- Search by athlete name or bib number.
- Select multiple athletes to pin them on every plot with color-coded markers showing their time, percentile, and rank (e.g. "Top 2% (9/418)").
- Athlete summary strip with per-segment stats for all selected athletes.
- Sortable results table; click any row to pin/unpin that athlete.

## Scraper

To regenerate `results.json` from the live results page:

1. Create a virtual environment and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests
```

2. Run the scraper:

```bash
python scrape_results.py
```

This fetches all 421 results (paginated at 100 per page) and writes them to `results.json`. The race data is already embedded in `index.html`, so re-running the scraper requires regenerating `index.html` as well (see comments at the top of `scrape_results.py`).

## Data fields

Each entry in `results.json` contains:

| Field | Description |
|---|---|
| `place` | Overall finishing place |
| `bib` | Bib number |
| `name` | Athlete name |
| `gender` | M / F |
| `age` | Age |
| `age_grade_pct` | Age-adjusted performance percentage (higher = better) |
| `gender_place` | Place within gender |
| `age_place_primary` | Age group place (primary division) |
| `age_place_secondary` | Age group place (secondary division, if applicable) |
| `division_primary` | Primary division (e.g. `M4044`) |
| `division_secondary` | Secondary division (e.g. `M Overall`, for age group winners) |
| `city` | Athlete's city |
| `state` | Athlete's state |
| `country` | Athlete's country |
| `swim_time` | Swim split (1.5K) |
| `t1_time` | Transition 1 time |
| `bike_time` | Bike split (40K) |
| `bike_pace` | Bike pace (mph) |
| `t2_time` | Transition 2 time |
| `run_time` | Run split (10K) |
| `run_pace` | Run pace (min/mile) |
| `clock_time` | Gun/clock time |
| `chip_time` | Chip time (usually empty) |
