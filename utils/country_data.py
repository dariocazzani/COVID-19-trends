from collections import defaultdict
import json
import sys
import requests
import numpy as np

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
    confirmed_deaths = defaultdict(list)
    world_cases = list()
    world_deaths = list()
    world_recovered = list()
    
    for c in all_countries:
        local_data_cases = [d.get("confirmed") for d in data[c]]
        local_data_deaths = [d.get("deaths") for d in data[c]]
        # Clean when there are dates with no update and a "sudden" jump
        new_local_data_cases = list()
        new_local_data_deaths = list()
    
        for idx, d in enumerate(local_data_cases):
            if idx > 1 and idx < len(local_data_cases)-1 and d - local_data_cases[idx-1] == 0:
                new_local_data_cases.append((local_data_cases[idx-1] + local_data_cases[idx+1]) / 2)
            else:
                new_local_data_cases.append(d)

        for idx, d in enumerate(local_data_deaths):
            if idx > 1 and idx < len(local_data_deaths)-1 and d - local_data_deaths[idx-1] == 0:
                new_local_data_deaths.append((local_data_deaths[idx-1] + local_data_deaths[idx+1]) / 2)
            else:
                new_local_data_deaths.append(d)

        confirmed[c] = new_local_data_cases
        confirmed_deaths[c] = new_local_data_deaths

    for _, v in data.items():
        cases = [d.get("confirmed") for d in v]
        world_cases.append(cases)
        deaths = [d.get("deaths") for d in v]
        world_deaths.append(deaths)
        recovered = [d.get("recovered") for d in v]
        world_recovered.append(recovered)
    
    world_deaths = np.sum(np.array(world_deaths),0)
    world_cases = np.sum(np.array(world_cases),0)    
    world_recovered = np.sum(np.array(world_recovered),0)    
    world_data = {"deaths":world_deaths, "cases":world_cases, "recovered":world_recovered}
        
    return confirmed, confirmed_deaths, world_data