import numpy as np
import matplotlib.pyplot as plt

# Create x values
x = np.linspace(-10, 10, 1000)

# Parameters of normal distribution
mu = 0
sigma = 1

# -----------------------------------
# Normal Distribution PDF
#
# f(x) = (1 / (σ√2π)) * e^(-(x-μ)^2 / (2σ²))
# -----------------------------------

sqrt_part = np.sqrt(2 * np.pi)
denominator = sigma * sqrt_part
fraction_part = 1 / denominator

power_part = (x - mu) ** 2
variance_part = 2 * (sigma ** 2)

exponent = - power_part / variance_part
exp_part = np.exp(exponent)

pdf = fraction_part * exp_part

# -----------------------------------
# CDF Formula
#
# F(x) = ∫(-∞ to x) f(t) dt
#
# We approximate using cumulative sum
# -----------------------------------

dx = x[1] - x[0]      # small step size
cdf = np.cumsum(pdf) * dx

# Plot PDF and CDF
plt.figure(figsize=(8,4))

plt.subplot(1,2,1)
plt.plot(x, pdf)
plt.title("PDF")

plt.subplot(1,2,2)
plt.plot(x, cdf)
plt.title("CDF")

plt.show()