import matplotlib.pyplot as plt
import json
from collections import defaultdict
import numpy as np

from utils.plot import plot
from utils.country_data import compute_countries_confirmed_cases

ALIGN_AROUND = 100 # cases

if __name__ == "__main__":    
    # Compute the number of cases for each country
    confirmed, confirmed_deaths = compute_countries_confirmed_cases()

    # Compute maximum number of cases we can align around: min (ALIGN_AROUND, x)
    # Take the second biggest one
    minimums_cases = [sorted(v)[-2] for c, v in confirmed.items()]
    minimums_deaths = [sorted(v)[-2] for c, v in confirmed_deaths.items()]
    new_align_around_cases = np.minimum(ALIGN_AROUND, np.min(minimums_cases))
    new_align_around_deaths = np.minimum(ALIGN_AROUND, np.min(minimums_deaths))

    # Compute the index for each country in order to align around the same number of cases
    align_indexes_cases = defaultdict(list)
    align_indexes_deaths = defaultdict(list)

    for c, v in confirmed.items():
        dist = np.abs(np.array(v) - new_align_around_cases)
        align_indexes_cases[c] = np.argmin(dist)
    for c, v in confirmed_deaths.items():
        dist = np.abs(np.array(v) - new_align_around_deaths)
        align_indexes_deaths[c] = np.argmin(dist)

    plot(confirmed, align_indexes_cases, new_align_around_cases, "cases")
    plot(confirmed_deaths, align_indexes_deaths, new_align_around_deaths, "deaths")