import matplotlib.pyplot as plt
import json
from collections import defaultdict
import numpy as np

from utils.plot import plot
from utils.italy_data import compute_provinces_confirmed_cases

ALIGN_AROUND = 20 # cases

if __name__ == "__main__":    
    # Compute the number of cases for each country
    confirmed = compute_provinces_confirmed_cases()

    # Compute maximum number of cases we can align around: min (ALIGN_AROUND, x)
    # Take the second biggest one
    minimums = [sorted(v)[-2] for c, v in confirmed.items()]
    new_align_around = np.minimum(ALIGN_AROUND, np.min(minimums))

    # Compute the index for each country in order to align around the same number of cases
    align_indexes = defaultdict(list)
    for c, v in confirmed.items():
        dist = np.abs(np.array(v) - ALIGN_AROUND)
        align_indexes[c] = np.argmin(dist)


    plot(confirmed, align_indexes, ALIGN_AROUND, "cases")
