import pandas as pd

data = [5,7,8,8,9,10,10,10,12,14]

freq_table = pd.Series(data).value_counts()
print(freq_table)

#  for large amount of data

import pandas as pd

data = [5,7,8,8,9,10,10,10,12,14]

freq_table = pd.Series(data).value_counts().sort_index()

print(freq_table)

import pandas as pd

data = [5,7,8,8,9,10,10,10,12,14]

freq_table = pd.Series(data).value_counts().sort_index()

df = pd.DataFrame({
    "Value": freq_table.index,
    "Frequency": freq_table.values
})

print(df)