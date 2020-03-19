import matplotlib.pyplot as plt
import json
from collections import defaultdict
import numpy as np

from utils.plot import plot_cases, plot_growth
from utils.country_data import parse_countries, compute_countries_confirmed_cases
from utils.growth_rate import compute_growth_rate

ALIGN_AROUND = 400 # cases

if __name__ == "__main__":    
    # Compute the number of cases for each country
    confirmed = compute_countries_confirmed_cases()

    # Compute the index for each country in order to align around the same number of cases
    align_indexes = defaultdict(list)
    for c, v in confirmed.items():
        dist = np.abs(np.array(v) - ALIGN_AROUND)
        align_indexes[c] = np.argmin(dist)

    growths = compute_growth_rate(confirmed)

    plot_cases(confirmed, align_indexes)
    plot_growth(growths, align_indexes)