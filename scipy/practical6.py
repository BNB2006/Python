import numpy as np
from scipy import stats

data = np.array([10, 15, 10, 18, 20, 10, 25, 30, 10])

mean_value = np.mean(data)
mean_value = np.round(mean_value, decimals=1)

median_value = np.median(data)

mode_result = stats.mode(data)

print("Dataset:", data)
print("Mean:", mean_value)
print("Median:", median_value)
print("Mode:", mode_result.mode, "(Count:", mode_result.count, ")")