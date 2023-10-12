import random

def monte_carlo_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2

        if distance <= 1:
            inside_circle += 1

    estimated_pi = 4 * inside_circle / num_samples
    return estimated_pi

if __name__ == "__main__":
    num_samples = 1000000  # Number of random samples

    estimated_pi = monte_carlo_pi(num_samples)
    print(f"Estimated π: {estimated_pi}")
