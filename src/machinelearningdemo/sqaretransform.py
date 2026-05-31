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
X = df[['Age','Fare']]
y = df['Survived']

# Handle missing values
X['Age'] = X['Age'].fillna(X['Age'].mean())

# Square transformation formula
# Y = X^2
X['Fare_square'] = X['Fare'] ** 2

# Use transformed features
X = X[['Age','Fare_square']]

# Split dataset
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

# Visualization
plt.figure(figsize=(12,4))

plt.subplot(121)
plt.hist(df['Fare'])
plt.title("Fare Before Square Transformation")

plt.subplot(122)
plt.hist(df['Fare']**2)
plt.title("Fare After Square Transformation")

plt.show()





# Titanic Dataset
#        ↓
# Select Features (Age, Fare)
#        ↓
# Handle Missing Values
#        ↓
# Square Transformation (Fare²)
#        ↓
# Train Logistic Regression
#        ↓
# Prediction
#        ↓
# Accuracy
#        ↓
# Visualization