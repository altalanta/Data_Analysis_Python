import numpy as np

def batch_gradient_descent(X, y, learning_rate, num_iterations):
    """
    Perform batch gradient descent for linear regression.

    Parameters:
    - X: Feature matrix (m x n)
    - y: Target variable (m x 1)
    - learning_rate: Learning rate for gradient descent
    - num_iterations: Number of iterations

    Returns:
    - theta: Optimized model parameters (n x 1)
    - cost_history: List of cost values during optimization
    """

    m, n = X.shape  # Number of training examples (m) and features (n)
    theta = np.zeros((n, 1) ) # Initialize model parameters to zeros
    cost_history = []

    for _ in range(num_iterations):
        # Calculate predictions
        predictions = np.dot(X, theta)

        # Calculate the error (the difference between predictions and actual values)
        error = predictions - y

        # Calculate the gradient of the cost function
        gradient = (1/m) * np.dot(X.T, error)

        # Update model parameters using the gradient
        theta -= learning_rate * gradient

        # Calculate the cost (mean squared error)
        cost = (1/(2*m)) * np.sum(error ** 2)
        cost_history.append(cost)

    return theta, cost_history

# Example usage:
if __name__ == "__main__":
    # Generate some example data
    np.random.seed(0)
    X = 2 * np.random.rand(100, 1)
    y = 4 + 3 * X + np.random.randn(100, 1)

    # Add a bias term (x0) to the feature matrix
    X_b = np.c_[np.ones((100, 1)), X]

    learning_rate = 0.1
    num_iterations = 1000

    # Perform batch gradient descent
    optimized_theta, cost_history = batch_gradient_descent(X_b, y, learning_rate, num_iterations)
    print("Optimized theta:", optimized_theta)
