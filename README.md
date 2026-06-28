# Pleasant Prairie Triathlon 2026 — Results Scraper

Scrapes the Olympic Individual Overall results from the 2026 Pleasant Prairie Triathlon into a local JSON file.

## Usage

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

This fetches all 421 results (paginated at 100 per page) and writes them to `results.json`.

## Output

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
