import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import numpy as np

file_path = '/Users/yourusername/Downloads/logistic_dataset.xlsx'

# Load the data from the Excel spreadsheet
excel_file = pd.ExcelFile(file_path)
df = excel_file.parse(excel_file.sheet_names[0])
# Assuming your Excel file has two columns: 'X' and 'Y'
X = df['Feature'].values.reshape(-1, 1)
y = df['Target'].values

# Create and fit the logistic regression model
model = LogisticRegression()
model.fit(X, y)

# Make predictions using the model
y_pred = model.predict(X)

# Calculate accuracy
accuracy = accuracy_score(y, y_pred)

# Create a scatter plot of the original data
plt.scatter(X, y, label="Original Data", color="blue")

# Create a logistic regression curve based on the model
X_range = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)
y_prob = model.predict_proba(X_range)[:, 1]
plt.plot(X_range, y_prob, label="Logistic Regression Curve", color="red")

# Display the accuracy on the plot
plt.text(0.8, 0.1, f"Accuracy: {accuracy:.2f}", transform=plt.gca().transAxes)

# Add labels and legend
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# Show the plot
plt.show()
