import pandas as pd
from scipy import stats
from sklearn.datasets import load_diabetes

print("--- Hypothesis Testing: Independent T-Test on UCI Diabetes Dataset ---")

diabetes_uci = load_diabetes(as_frame=True)
df_uci = diabetes_uci.frame

# Perform a two-sample t-test (Independent T-test)
# We will split the dataset into two groups based on 'sex' feature to see if disease progression differs.
unique_sex = df_uci['sex'].unique()

group1 = df_uci[df_uci['sex'] == unique_sex[0]]['target']
group2 = df_uci[df_uci['sex'] == unique_sex[1]]['target']

print("Null Hypothesis (H0): Mean target (disease progression) is equal for both sexes.")
print("Alternative Hypothesis (H1): Mean target is different between the two sexes.")

# Perform independent t-test
t_stat, p_value = stats.ttest_ind(group1, group2)

print(f"\nT-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print(f"\nConclusion (alpha={alpha}): Reject the Null Hypothesis (H0). There is a significant difference in disease progression between sexes.")
else:
    print(f"\nConclusion (alpha={alpha}): Fail to reject the Null Hypothesis (H0). No significant difference in disease progression between sexes.")
