import numpy as np
import pandas as pd

# Set the seed for reproducibility
np.random.seed(42)

# Generate logistic data
num_samples = 1000
X = np.random.uniform(low=-5, high=5, size=num_samples)
logistic_prob = 1 / (1 + np.exp(-X))
y = np.random.binomial(n=1, p=logistic_prob)

# Create a DataFrame with two columns
df = pd.DataFrame({'Feature': X, 'Target': y})

# Specify the path to the downloads folder and the filename
download_path = "/Users/yourusername/Downloads/logistic_dataset.xlsx"

# Save the DataFrame to an Excel file
df.to_excel(download_path, index=False, engine="openpyxl")

print(f"Dataset saved to {download_path}")
