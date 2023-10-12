import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

file_path = '/Users/your_username/Downloads/linear_dataset.xlsx'

# Load the data from the Excel spreadsheet
excel_file = pd.ExcelFile(file_path)
df = excel_file.parse(excel_file.sheet_names[0])

# Prepare the data
X = df['X'].values.reshape(-1, 1)
Y = df['Y'].values

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, Y)

# Get the coefficients of the linear regression equation
slope = model.coef_[0]
intercept = model.intercept_

# Make predictions using the model
Y_pred = model.predict(X)

# Calculate the R-squared value
r_squared = r2_score(Y, Y_pred)

# Visualize the data and the regression line
plt.scatter(X, Y, label='Data')
plt.plot(X, Y_pred, color='red', label='Linear Regression')
plt.xlabel('Independent Variable')
plt.ylabel('Dependent Variable')
plt.legend()
plt.title(f'Linear Regression\nEquation: Y = {slope:.2f} * X + {intercept:.2f}\nR-squared: {r_squared:.2f}')

# Add text annotations for the equation and R-squared value
plt.text(0.5, 10, f'Y = {slope:.2f} * X + {intercept:.2f}', color='red', fontsize=12)
plt.text(0.5, 8, f'R-squared: {r_squared:.2f}', color='red', fontsize=12)

plt.show()
