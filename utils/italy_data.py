from collections import defaultdict
import json
import sys
import requests

data = requests.get("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-json/dpc-covid19-ita-province.json").json()

def parse_provinces() -> list:
    provinces = list(set([element.get("sigla_provincia") for element in data]))

    default_provinces = ["VA", "BG", "MI", "CO", "RO"]
    all_provinces = list()

    new_provinces = sys.argv[1:]
    new_provinces = list(filter(lambda x: x in provinces, new_provinces))

    all_provinces.extend(default_provinces)
    all_provinces.extend(new_provinces)
    return all_provinces

def compute_provinces_confirmed_cases() -> dict:

    # Get all data for each country
    all_provinces = parse_provinces()
    confirmed = defaultdict(list)
    
    for p in all_provinces:
        local_data = [element.get("totale_casi") for element in data if element.get("sigla_provincia") == p]
        new_local_data = list()

        # Clean from "mistakes" in the data
        for idx, d in enumerate(local_data):
            if idx > 1 and idx < len(local_data) and d - local_data[idx-1] == 0:
                # Clean when there are dates with no update and a "sudden" jump
                new_local_data.append((local_data[idx-1] + local_data[idx+1]) / 2)
            if idx > 0 and d < local_data[idx-1]:
                # the total number of cases can't decrease
                new_local_data.append(max(local_data[:idx]))
            else:
                new_local_data.append(d)

        confirmed[p] = new_local_data
    return confirmed