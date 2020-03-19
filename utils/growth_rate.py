import numpy as np
from collections import defaultdict


""" GROWTH RATE """
def compute_moving_avg(values, window):
    weights = np.repeat(1.0, window)/window
    sma = np.convolve(values, weights, 'valid')
    return sma

def compute_growth_rate(confirmed):
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
    
    return growth_rate, growth_rate_moving_average, growth_rate_global_moving_average