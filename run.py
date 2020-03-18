import matplotlib.pyplot as plt
import json
from collections import defaultdict
import numpy as np
import requests
import sys

data = requests.get("https://pomber.github.io/covid19/timeseries.json").json()

def parse_countries(data:json) -> list:
    countries = list(data.keys())

    default_countries = ["Germany", "US", "Spain", "Norway", "Italy"]
    all_countries = list()

    def get_listed_countries(candidate):
        if candidate in countries:
            return True
        return False

    new_countries = sys.argv[1:]
    new_countries = list(filter(get_listed_countries, new_countries))

    all_countries.extend(default_countries)
    all_countries.extend(new_countries)
    return all_countries


all_countries = parse_countries(data)

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

align_around = 400
align_indexes = defaultdict(list)
for c, v in confirmed.items():
    dist = np.abs(np.array(v) - align_around)
    align_indexes[c] = np.argmin(dist)

# Simple graph
plt.subplot(2, 3, 1)
for c, v in confirmed.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    plt.plot(v, label=c, linewidth=linewidth)

plt.legend(loc="upper left")
plt.title("Number of cases", fontsize=14, fontweight='bold')
plt.xlabel("Days since February 22 2020")

# Simple aligned
plt.subplot(2, 3, 2)
for c, v in confirmed.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    plt.plot(v[align_indexes[c]:], label=c, linewidth=linewidth)
    
plt.legend(loc="upper left")
plt.title("Number of cases", fontsize=14, fontweight='bold')
plt.xlabel("Days since cases are around 400")

# Logarithm Gradient
plt.subplot(2, 3, 3)
for c, v in confirmed.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    array = np.array(v)
    log_array = np.log10(array+1)
    array = np.gradient(log_array)
    plt.plot(array, label=c, linewidth=linewidth)

plt.legend(loc="upper left")
plt.title("Gradient of number of cases in log scale", fontsize=14, fontweight='bold')
plt.xlabel("Days since February 22 2020")

# Logarithm
plt.subplot(2, 3, 4)
for c, v in confirmed.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    array = np.array(v)
    plt.plot(np.log10(array+1), label=c, linewidth=linewidth)

plt.legend(loc="upper left")
plt.title("Number of cases in log scale", fontsize=14, fontweight='bold')
plt.xlabel("Days since February 22 2020")

# Logarithm aligned
plt.subplot(2, 3, 5)
for c, v in confirmed.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    array = np.array(v)
    plt.plot(np.log10(array[align_indexes[c]:]+1), label=c, linewidth=linewidth)

plt.legend(loc="upper left")
plt.title("Number of cases in log scale", fontsize=14, fontweight='bold')
plt.xlabel("Days since cases are around 400")

# Logarithm aligned Gradient
plt.subplot(2, 3, 6)
for c, v in confirmed.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    array = np.array(v)
    alinged_array = array[align_indexes[c]:]
    log_array = np.log10(alinged_array+1)
    array = np.gradient(log_array)
    plt.plot(array, label=c, linewidth=linewidth)

plt.legend(loc="upper left")
plt.title("Gradient of number of cases in log scale", fontsize=14, fontweight='bold')
plt.xlabel("Days since cases are around 400")

plt.show()

""" GROWTH RATE """
def compute_moving_avg(values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma

growth_rate = defaultdict(list)
for c, v in confirmed.items():
    cases = v
    diffs = [1] + [cases[i+1]+1 - cases[i]+1 for i in range(len(cases)-1)]
    growth_rate[c] = [diffs[i+1] / diffs[i] for i in range(len(diffs)-1)]

growth_rate_global_moving_average = defaultdict(list)
for c, v in growth_rate.items():
    moving_avg = list()
    for idx, _ in enumerate(v):
        moving_avg.append(sum(v[:idx])/ (idx+1))
    growth_rate_global_moving_average[c] = moving_avg

growth_rate_moving_average = defaultdict(list)
for c, v in growth_rate.items():
    growth_rate_moving_average[c] = compute_moving_avg(v, 5)


# Raw Growth Rate
plt.subplot(2, 3, 1)
for c, v in growth_rate.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    plt.plot(v, label=c, linewidth=linewidth)
    
plt.legend(loc="upper left")
plt.title("Growth Rate Raw", fontsize=14, fontweight='bold')
plt.xlabel("Days since February 22 2020")

# Raw Growth Rate
plt.subplot(2, 3, 2)
for c, v in growth_rate_moving_average.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    plt.plot(v, label=c, linewidth=linewidth)
    
plt.legend(loc="upper left")
plt.title("Growth Rate moving average 5 days", fontsize=14, fontweight='bold')
plt.xlabel("Days since February 22 2020")


plt.subplot(2, 3, 3)
for c, v in growth_rate_global_moving_average.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    plt.plot(v, label=c, linewidth=linewidth)
    
plt.legend(loc="upper left")
plt.title("Growth Rate global moving average", fontsize=14, fontweight='bold')
plt.xlabel("Days since February 22 2020")


plt.subplot(2, 3, 4)
for c, v in growth_rate.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    plt.plot(v[align_indexes[c]:], label=c, linewidth=linewidth)
    
plt.legend(loc="upper left")
plt.title("Growth Rate Raw", fontsize=14, fontweight='bold')
plt.xlabel("Days since cases are around 400")


plt.subplot(2, 3, 5)
for c, v in growth_rate_moving_average.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    plt.plot(v[align_indexes[c]:], label=c, linewidth=linewidth)
    
plt.legend(loc="upper left")
plt.title("Growth Rate moving average 5 days", fontsize=14, fontweight='bold')
plt.xlabel("Days since cases are around 400")


plt.subplot(2, 3, 6)
for c, v in growth_rate_global_moving_average.items():
    if c == "Italy":
        linewidth = 2.5
    else:
        linewidth = 1.4
    plt.plot(v[align_indexes[c]:], label=c, linewidth=linewidth)
    
plt.legend(loc="upper left")
plt.title("Growth Rate global moving average", fontsize=14, fontweight='bold')
plt.xlabel("Days since cases are around 400")

plt.show()