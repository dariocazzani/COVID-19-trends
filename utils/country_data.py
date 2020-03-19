from collections import defaultdict
import json
import sys
import requests

data = requests.get("https://pomber.github.io/covid19/timeseries.json").json()

def parse_countries() -> list:
    countries = list(data.keys())

    default_countries = ["Germany", "US", "Spain", "Norway", "Italy"]
    all_countries = list()

    new_countries = sys.argv[1:]
    new_countries = list(filter(lambda x: x in countries, new_countries))

    all_countries.extend(default_countries)
    all_countries.extend(new_countries)
    return all_countries

def compute_countries_confirmed_cases() -> dict:

    # Get all data for each country
    all_countries = parse_countries()
    confirmed = defaultdict(list)
    
    for c in all_countries:
        local_data = [d.get("confirmed") for d in data[c]]
        # Clean when there are dates with no update and a "sudden" jump
        new_local_data = list()

        for idx, d in enumerate(local_data):
            if idx > 1 and idx < len(local_data) and d - local_data[idx-1] == 0:
                new_local_data.append((local_data[idx-1] + local_data[idx+1]) / 2)
            else:
                new_local_data.append(d)

        confirmed[c] = new_local_data
    return confirmed