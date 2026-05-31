import pandas as pd
import matplotlib.pyplot as plt

data = [12,15,15,18,20,20,20,22,25]

series = pd.Series(data)

# Frequency table
frequency = series.value_counts().sort_index()

print("Frequency Table")
print(frequency)

# Histogram
plt.figure()

plt.hist(series, bins=5)

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Histogram of Numerical Data")

plt.show()