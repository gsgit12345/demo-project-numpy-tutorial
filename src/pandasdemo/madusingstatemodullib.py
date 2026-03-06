import numpy as np
from statsmodels.robust.scale import mad

from statsmodels import robust
# Example dataset
data = np.array([10, 12, 14, 15, 100])
# Calculate Median Absolute Deviation
mad_value = mad(data)
print("MAD:", mad_value)



#pip install statsmodels