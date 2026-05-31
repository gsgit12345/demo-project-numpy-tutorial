# Step 1: Import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 2: Load Titanic dataset
df = sns.load_dataset('titanic')

# Step 3: Check basic info
print(df[['fare']].head())
print(df['fare'].describe())

# Step 4: Handle zero or missing values
# (Reciprocal cannot handle 0, so we add small epsilon)
df['fare'] = df['fare'].fillna(0)
df['fare'] = df['fare'] + 1e-6   # avoid division by zero

# Step 5: Apply Reciprocal Transformation
df['fare_reciprocal'] = 1 / df['fare']

# Step 6: Compare distributions
plt.figure(figsize=(12,5))

# Original Fare
plt.subplot(1,2,1)
sns.histplot(df['fare'], kde=True)
plt.title("Original Fare Distribution")

# Transformed Fare
plt.subplot(1,2,2)
sns.histplot(df['fare_reciprocal'], kde=True)
plt.title("Reciprocal Transformed Fare")

plt.show()

# Step 7: Compare few values
print(df[['fare', 'fare_reciprocal']].head(10))