import numpy as np


# generate the samples of standard disyributio 

# That means:

# Mean (μ) = 0

# Standard deviation (σ) = 1

# Values can be positive or negative

sample=np.random.randn(10)   #randn() generates numbers from a normal (Gaussian) distribution.

print(sample)

sample2 = np.random.randn(10).astype(int)
print(sample2)



# 👉 randn() is commonly used for neural network weight initialization.
# 👉 It helps break symmetry during training.


sample4 = np.random.randint(-10, 10, size=10) #it is uniform distribution
print(sample4)