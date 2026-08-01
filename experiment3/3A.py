import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_diabetes

print("--- Univariate Analysis: Statistical Analysis Using Diabetes Datasets ---")

# 1. UCI Diabetes Dataset (from sklearn)
diabetes_uci = load_diabetes(as_frame=True)
df_uci = diabetes_uci.frame

print("\n--- 1. UCI Diabetes Dataset ---")
print("Descriptive Statistics:")
print(df_uci.describe().T)

# Univariate analysis on Target variable (Disease progression)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
sns.histplot(df_uci['target'], kde=True, color='blue')
plt.title('UCI Dataset: Target Distribution')
plt.xlabel('Disease Progression Measure')

# 2. Pima Indians Diabetes Dataset
print("\n--- 2. Pima Indians Diabetes Dataset ---")
pima_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigree', 'Age', 'Outcome']

try:
    df_pima = pd.read_csv(pima_url, names=columns)
    print("Descriptive Statistics:")
    print(df_pima.describe().T)
    
    plt.subplot(1, 2, 2)
    sns.histplot(df_pima['Glucose'], kde=True, color='green')
    plt.title('Pima Dataset: Glucose Distribution')
    
    plt.tight_layout()
    # plt.show() # Uncomment this to display plots
    print("\nUnivariate plots generated. Uncomment plt.show() in the script to view them.")
except Exception as e:
    print("\nCould not load Pima Indians dataset:", e)
