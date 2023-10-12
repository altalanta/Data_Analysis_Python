import sys
import statsmodels.stats.power as smp

def calculate_sample_size(alpha, beta, effect_size, power):
    # Calculate sample size based on alpha, beta, effect size, and statistical power
    nobs1 = smp.TTestIndPower().solve_power(effect_size=effect_size, nobs1=None, alpha=alpha, power=power, ratio=1)
    return int(nobs1)

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python3 sample_size_calc.py alpha beta effect_size power")
        sys.exit(1)

    # Get command-line arguments
    alpha = float(sys.argv[1])
    beta = float(sys.argv[2])
    effect_size = float(sys.argv[3])
    power = float(sys.argv[4])

    sample_size = calculate_sample_size(alpha, beta, effect_size, power)
    print("Required Sample Size:", sample_size)
