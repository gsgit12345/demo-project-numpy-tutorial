import numpy as np


#step = (stop - start) / (num - 1)

# start → starting value

# stop → ending value

# num → total number of values you want

#step=stop−start​/num−1

line=np.linspace(0,10,4)

print (line)

line=np.linspace(0,10,4,endpoint=False)

print (line)