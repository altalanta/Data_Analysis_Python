import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

def perform_ridge_regression(data_file, target_column, alpha):
    # Load the data from a CSV file (adjust the file format and loading method as needed)
    data = pd.read_csv(data_file)

    # Extract the target variable (dependent variable)
    y = data[target_column]

    # Extract the independent variables (features)
    X = data.drop(columns=[target_column])

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and fit the Ridge Regression model
    ridge_model = Ridge(alpha=alpha)
    ridge_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = ridge_model.predict(X_test)

    # Calculate the Mean Squared Error (MSE) as a performance metric
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error (MSE): {mse}")

def main():
    # Define command-line arguments
    parser = argparse.ArgumentParser(description="Perform Ridge Regression")
    parser.add_argument("data_file", help="Path to the data file (CSV format)")
    parser.add_argument("target_column", help="Name of the target column")
    parser.add_argument("--alpha", type=float, default=1.0, help="Ridge regularization strength (default: 1.0)")

    # Parse command-line arguments
    args = parser.parse_args()

    # Perform Ridge Regression
    perform_ridge_regression(args.data_file, args.target_column, args.alpha)

if __name__ == "__main__":
    main()
