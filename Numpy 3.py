import numpy as np

rng = np.random.default_rng(seed=123)
arr1 = rng.integers(0,101,size = 100)

mean_value= np.mean(arr1)
hist,bins = np.histogram(arr1,bins= 10)

print(mean_value)
print("Histogram: ", hist)
print("Bins:  ", bins)