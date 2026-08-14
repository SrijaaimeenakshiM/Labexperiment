import pandas as pd
from scipy import stats
from sklearn.datasets import load_diabetes

print("--- Hypothesis Testing: ANOVA on UCI Diabetes Dataset ---")

diabetes_uci = load_diabetes(as_frame=True)
df_uci = diabetes_uci.frame

# For ANOVA, we need a categorical variable with 3 or more groups.
# We will create categories from the continuous variable 'bmi' by binning it.
print("Binning 'bmi' into 3 categories (Low, Medium, High) for One-Way ANOVA test...\n")
df_uci['bmi_group'] = pd.qcut(df_uci['bmi'], q=3, labels=['Low', 'Medium', 'High'])

group_low = df_uci[df_uci['bmi_group'] == 'Low']['target']
group_medium = df_uci[df_uci['bmi_group'] == 'Medium']['target']
group_high = df_uci[df_uci['bmi_group'] == 'High']['target']

print("Null Hypothesis (H0): Mean disease progression is the same across all three BMI groups.")
print("Alternative Hypothesis (H1): At least one group mean is different.")

# Perform One-way ANOVA
f_stat, p_value = stats.f_oneway(group_low, group_medium, group_high)

print(f"\nF-statistic: {f_stat:.4f}")
print(f"P-value: {p_value:.4e}")

alpha = 0.05
if p_value < alpha:
    print(f"\nConclusion (alpha={alpha}): Reject the Null Hypothesis (H0). There is a significant difference in disease progression between the BMI groups.")
else:
    print(f"\nConclusion (alpha={alpha}): Fail to reject the Null Hypothesis (H0).")
