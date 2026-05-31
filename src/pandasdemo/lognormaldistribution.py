import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# generate log-normal data
data = np.random.lognormal(mean=0, sigma=1, size=1000)


# histogram
plt.hist(data, bins=10)
plt.title("Log-Normal Distribution")
plt.show()

# check normality of log values
stats.probplot(np.log(data), dist="norm", plot=plt)
plt.show()