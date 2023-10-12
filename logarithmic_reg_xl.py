import os
import pandas as pd
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the path to the Excel file in the Downloads folder
downloads_folder = os.path.expanduser("~/Downloads")
excel_file_path = os.path.join(downloads_folder, "logarithmic_dataset.xlsx")

# Load the Excel data into a DataFrame
try:
    df = pd.read_excel(excel_file_path)
except FileNotFoundError:
    print(f"Excel file '{excel_file_path}' not found. Please make sure it exists.")
    exit(1)

# Extract 'X' and 'Y' columns from the DataFrame
x = df['X'].values
y = df['Y'].values

# Define the logarithmic function to fit
def logarithmic_function(x, a, b):
    return a * np.log(x) + b

# Fit the curve to the data
params, covariance = curve_fit(logarithmic_function, x, y)

# Extract the parameters
a, b = params

# Generate points for the fitted curve
x_fit = np.linspace(min(x), max(x), 100)
y_fit = logarithmic_function(x_fit, a, b)

# Plot the original data and the fitted curve
plt.scatter(x, y, label="Original Data")
plt.plot(x_fit, y_fit, label="Fitted Curve", color="red")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
