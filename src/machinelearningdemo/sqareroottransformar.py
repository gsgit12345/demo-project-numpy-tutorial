# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load Titanic dataset
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

# Select features and target
X = df[['Age', 'Fare']]
y = df['Survived']

# Handle missing values
X['Age'] = X['Age'].fillna(X['Age'].mean())

# Apply Square Root Transformation
X['Fare_sqrt'] = np.sqrt(X['Fare'])

# Use transformed feature
X = X[['Age', 'Fare_sqrt']]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Model Accuracy:", accuracy_score(y_test, y_pred))

plt.figure(figsize=(12,4))

# Before transformation
plt.subplot(121)
plt.hist(df['Fare'])
plt.title("Fare Before √ Transformation")

# After transformation
plt.subplot(122)
plt.hist(np.sqrt(df['Fare']))
plt.title("Fare After √ Transformation")

plt.show()