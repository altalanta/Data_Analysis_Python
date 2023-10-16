from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

def perform_lasso_regression(X, y, alpha=1.0, test_size=0.2, random_state=None):
    """
    Perform Lasso regression.

    Parameters:
        X (array-like): The feature matrix.
        y (array-like): The target variable.
        alpha (float): L1 regularization strength (default=1.0).
        test_size (float): Fraction of the data to be used as the test set (default=0.2).
        random_state (int or None): Seed for random number generation (default=None).

    Returns:
        float: Mean squared error on the test set.
    """
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Create a Lasso regression model
    lasso_model = Lasso(alpha=alpha)

    # Fit the model to the training data
    lasso_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = lasso_model.predict(X_test)

    # Calculate the mean squared error
    mse = mean_squared_error(y_test, y_pred)
    return mse

# Example usage:
if __name__ == "__main__":
    # Generate some example data
    np.random.seed(0)
    X = np.random.rand(100, 2)
    y = 2 * X[:, 0] + 3 * X[:, 1] + 0.5 * np.random.randn(100)

    # Call the Lasso regression function
    mse = perform_lasso_regression(X, y, alpha=0.01)

    print(f"Mean Squared Error: {mse}")
