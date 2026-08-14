import pandas as pd
from statsmodels.stats.weightstats import ztest
from sklearn.datasets import load_diabetes

print("--- Hypothesis Testing: Z-Test on UCI Diabetes Dataset ---")

diabetes_uci = load_diabetes(as_frame=True)
df_uci = diabetes_uci.frame

# Let's perform a one-sample z-test on 'bmi'
# Null Hypothesis (H0): The population mean of 'bmi' is 0 (Since UCI dataset features are mean-centered)
# Alternative Hypothesis (H1): The population mean is not 0
mean_value = 0
print(f"Null Hypothesis (H0): Population mean of 'bmi' = {mean_value}")
print(f"Alternative Hypothesis (H1): Population mean of 'bmi' != {mean_value}")

# Perform Z-test
z_stat, p_value = ztest(df_uci['bmi'], value=mean_value)

print(f"\nZ-statistic: {z_stat:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"\nConclusion (alpha={alpha}): Reject the Null Hypothesis (H0). The mean is significantly different from {mean_value}.")
else:
    print(f"\nConclusion (alpha={alpha}): Fail to reject the Null Hypothesis (H0). Not enough evidence to say the mean is different from {mean_value}.")
