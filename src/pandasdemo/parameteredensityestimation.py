import  numpy as np

import matplotlib.pyplot as plt
from scipy.stats import norm   # import normal distribution functions


data= np.array([165,170,168,172,169,171,167,173,166,174])


sigma=np.std(data)

mean=np.mean(data)

# Step 3: Create x values
x=np.linspace(min(data)-5,max(data)+5,100)

# Step 4: Compute PDF using estimated parameters
# norm.pdf() computes the probability density function
# using the normal distribution formula
# Step 4: Compute Probability Density Function
# -----------------------------

# Normal Distribution PDF:
#
# f(x) = 1 / (σ√(2π)) * e^(-(x-μ)^2 / (2σ^2))
#
# x = data value
# μ = mean
# σ = standard deviation

pdf=norm.pdf(x,mean,sigma)

# Step 5: Plot density

plt.hist(data,bins=5,density=True, alpha=0.5,label="Data Histogram")

plt.plot(x,pdf,'r',label="Estimated Normal PDF")

plt.legend()
plt.title("Parametric Density Estimation (Normal Distribution)")
plt.show()