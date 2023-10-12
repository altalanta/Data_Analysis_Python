import numpy as np
import pandas as pd
import os

# Set a random seed for reproducibility
np.random.seed(0)

# Generate X values
X = np.random.rand(100, 1) * 10

# Generate Y values with a linear relationship
Y = 3 * X + np.random.randn(100, 1)

# Create a DataFrame to store the dataset
df = pd.DataFrame({'X': X.flatten(), 'Y': Y.flatten()})

# Calculate the R-squared coefficient
correlation_matrix = np.corrcoef(X.flatten(), Y.flatten())
r_squared = correlation_matrix[0, 1] ** 2

print(f"R-squared coefficient: {r_squared:.2f}")

# Get the path to the "Downloads" folder
downloads_folder = os.path.expanduser('~') + '/Downloads/'

# Save the dataset to an Excel spreadsheet in the "Downloads" folder
# Replace 'linear_dataset.xlsx' with the desired file name
excel_file_path = os.path.join(downloads_folder, 'linear_dataset.xlsx')
df.to_excel(excel_file_path, index=False)

print(f"File saved to {excel_file_path}")
