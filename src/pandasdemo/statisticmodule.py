import statistics

data = [10, 20, 30, 40, 50]

mean_value = statistics.mean(data)

print(mean_value)


import numpy as np

data = np.array([10, 20, 30, 40, 50])

mean_value = np.mean(data)

print(mean_value)


import pandas as pd

data = pd.Series([10, 20, 30, 40, 50])

mean_value = data.mean()

print(mean_value)