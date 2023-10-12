import pandas as pd

# Replace 'your_excel_file.xlsx' with the path to your Excel file.
excel_file_path = '/Users/artemisfolle/Downloads/linear_dataset.xlsx'

# Replace 'output_csv_file.csv' with the desired name for your CSV file.
csv_file_path = '/Users/artemisfolle/Downloads/linear_dataset.csv'

# Read the Excel file into a DataFrame
df = pd.read_excel(excel_file_path)

# Write the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)  # Set index=False to exclude the index column in the CSV
