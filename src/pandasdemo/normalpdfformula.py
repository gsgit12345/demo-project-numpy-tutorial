import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.linspace(-10, 10, 1000)

# Parameters of normal distribution
mu = 0        # μ = mean
sigma = 1     # σ = standard deviation

# -------------------------------
# Normal Distribution PDF Formula
#
#                 1
# f(x) = ---------------------- * e^(-(x-μ)^2 / (2σ^2))
#        σ * sqrt(2π)
# -------------------------------

# Step 1: Calculate sqrt(2π)
sqrt_part = np.sqrt(2 * np.pi)

# Step 2: Calculate denominator σ * sqrt(2π)
denominator = sigma * sqrt_part

# Step 3: Calculate first fraction part
fraction_part = 1 / denominator

# Step 4: Calculate exponent numerator (x - μ)^2
power_part = (x - mu) ** 2

# Step 5: Calculate exponent denominator 2σ²
variance_part = 2 * (sigma ** 2)

# Step 6: Calculate exponent value
exponent = - power_part / variance_part

# Step 7: Calculate exponential term e^(...)
exp_part = np.exp(exponent)

# Step 8: Final PDF
pdf = fraction_part * exp_part

# Plot the curve
plt.plot(x, pdf)
plt.title("Normal Distribution PDF")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()



