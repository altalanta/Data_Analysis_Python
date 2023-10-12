import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/artemisfolle/Downloads/logarithmic_dataset.xlsx'

# Read data from Excel file
df = pd.read_excel(file_path)


# Create a scatter plot
plt.scatter(df['X'], df['Y'])
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Scatter Plot of Data')
plt.show()
