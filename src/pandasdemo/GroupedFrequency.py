import pandas as pd

data = [5,7,8,8,9,10,10,10,12,14]

bins = [5,8,11,14,17]

freq_table = pd.cut(data, bins=bins).value_counts()

print(freq_table)