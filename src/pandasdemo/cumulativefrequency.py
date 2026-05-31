import pandas as pd
import matplotlib.pyplot as plt


data_set=[5,7,8,8,9,10,10,10,12,14]

series=pd.Series(data_set)

frequency=series.value_counts().sort_index()

cumulative_frequency=frequency.cumsum()

df = pd.DataFrame({
    "Frequency": frequency,
    "Cumulative Frequency": cumulative_frequency
})

print(df)
# Plot Frequency Chart
plt.figure()

df["Frequency"].plot(kind="bar")

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Frequency Distribution")

plt.show()
