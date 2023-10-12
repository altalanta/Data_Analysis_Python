import sys
import statsmodels.stats.power as smp

def calculate_power(alpha, beta, effect_size, nobs):
    # Calculate statistical power based on alpha, beta, effect size, and sample size
    power = smp.TTestIndPower().solve_power(effect_size=effect_size, nobs1=None, alpha=alpha, power=beta, ratio=nobs/100)
    return power
"""
    Calculate statistical power based on alpha, beta, effect size, and sample size.

    Parameters:
    - alpha (float): Significance level (e.g., 0.05 for 5% significance).
    - beta (float): Desired power (e.g., 0.8 for 80% power).
    - effect_size (float): Effect size (Cohen's d or other relevant measure).
    - nobs (int): Sample size.

    Returns:
    - power (float): Calculated statistical power.
"""
if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python3 power_calc.py alpha beta effect_size nobs")
        sys.exit(1)

    # Get command-line arguments
    alpha = float(sys.argv[1])
    beta = float(sys.argv[2])
    effect_size = float(sys.argv[3])
    nobs = int(sys.argv[4])

    power = calculate_power(alpha, beta, effect_size, nobs)
    print("Statistical Power:", power)
