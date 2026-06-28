import requests
import json
import math
import time

BASE_URL = "https://www.pleasantprairietri.com/Race/Results/53294"
RESULT_SET_ID = 664399
PER_PAGE = 100

HEADERS = {
    "Accept": "application/json, */*; q=0.01",
    "Referer": "https://www.pleasantprairietri.com/Race/Results/53294",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/149.0.0.0 Safari/537.36"
    ),
}

# Column indices in each result row (matches the API's headings array)
IDX_PLACE        = 0
IDX_BIB          = 1
IDX_NAME         = 2
IDX_GENDER       = 3
IDX_GENDER_PLACE = 4
IDX_AGE          = 5
IDX_AGE_GRADE    = 6
IDX_AGE_PLACE    = 7   # may contain "\n" for multi-division
IDX_DIVISION     = 8   # may contain "\n" for multi-division
IDX_CITY         = 9
IDX_STATE        = 10
IDX_SWIM         = 11
IDX_T1           = 12
IDX_BIKE         = 13
IDX_BIKE_PACE    = 14
IDX_T2           = 15
IDX_RUN          = 16
IDX_RUN_PACE     = 17
IDX_CLOCK_TIME   = 18
IDX_COUNTRY      = 19
IDX_CHIP_TIME    = 20


def split_field(value):
    """Return (primary, secondary) for a potentially newline-separated field."""
    if isinstance(value, str) and "\n" in value:
        primary, secondary = value.split("\n", 1)
        return primary, secondary
    return value, None


def parse_row(row):
    age_place_primary, age_place_secondary = split_field(row[IDX_AGE_PLACE])
    division_primary, division_secondary = split_field(row[IDX_DIVISION])

    age_grade_raw = row[IDX_AGE_GRADE]
    age_grade = float(age_grade_raw) if age_grade_raw not in (None, "", "0") else None

    return {
        "place":                 row[IDX_PLACE],
        "bib":                   row[IDX_BIB],
        "name":                  row[IDX_NAME],
        "gender":                row[IDX_GENDER],
        "age":                   row[IDX_AGE],
        "age_grade_pct":         age_grade,
        "gender_place":          row[IDX_GENDER_PLACE],
        "age_place_primary":     age_place_primary,
        "age_place_secondary":   age_place_secondary,
        "division_primary":      division_primary,
        "division_secondary":    division_secondary,
        "city":                  row[IDX_CITY],
        "state":                 row[IDX_STATE],
        "country":               row[IDX_COUNTRY],
        "swim_time":             row[IDX_SWIM],
        "t1_time":               row[IDX_T1],
        "bike_time":             row[IDX_BIKE],
        "bike_pace":             row[IDX_BIKE_PACE],
        "t2_time":               row[IDX_T2],
        "run_time":              row[IDX_RUN],
        "run_pace":              row[IDX_RUN_PACE],
        "clock_time":            row[IDX_CLOCK_TIME],
        "chip_time":             row[IDX_CHIP_TIME],
    }


def fetch_page(session, page):
    params = {
        "resultSetId": RESULT_SET_ID,
        "page": page,
        "num": PER_PAGE,
        "search": "",
    }
    resp = session.get(BASE_URL, params=params, headers=HEADERS, timeout=15)
    resp.raise_for_status()
    return resp.json()


def fetch_all():
    all_results = []

    with requests.Session() as session:
        first_page = fetch_page(session, 1)
        num_results = first_page["resultSet"]["numResults"]
        total_pages = math.ceil(num_results / PER_PAGE)
        print(f"Total results: {num_results}  |  Pages: {total_pages}")

        for row in first_page["resultSet"]["results"]:
            all_results.append(parse_row(row))
        print(f"  Page 1: {len(first_page['resultSet']['results'])} rows")

        for page in range(2, total_pages + 1):
            time.sleep(0.5)  # be polite
            data = fetch_page(session, page)
            rows = data["resultSet"]["results"]
            for row in rows:
                all_results.append(parse_row(row))
            print(f"  Page {page}: {len(rows)} rows")

    return all_results


if __name__ == "__main__":
    print("Fetching results...")
    results = fetch_all()
    print(f"\nTotal rows collected: {len(results)}")

    output_path = "results.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Saved → {output_path}")
