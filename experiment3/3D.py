import pandas as pd
from sklearn.datasets import load_diabetes

print("--- Comparison of analysis results between the two datasets ---")

print("\n[ Dataset 1: UCI Diabetes Dataset ]")
print("- Type: Regression Problem")
print("- Target Variable: Quantitative measure of disease progression one year after baseline.")
print("- Key Characteristics: Features (like bmi, age, bp) are continuous and mean centered / scaled. Target is a continuous numerical value.")
print("- Primary Models Used: Linear Regression, Multiple Regression, Ridge, Lasso.")

print("\n[ Dataset 2: Pima Indians Diabetes Dataset ]")
print("- Type: Classification Problem")
print("- Target Variable: Outcome (0 = Non-diabetic, 1 = Diabetic).")
print("- Key Characteristics: Features (like pregnancies, glucose, insulin) are raw clinical observations. Target is a categorical binary value.")
print("- Primary Models Used: Logistic Regression, Decision Trees, Random Forest, SVM.")

print("\n[ Key Differences & Analysis Comparison ]")
print("1. Objective:")
print("   - UCI: Predicts *how far* the disease has progressed.")
print("   - Pima: Diagnoses *whether* the patient has the disease or not.")
print("2. Evaluation Metrics:")
print("   - UCI: Evaluated using Mean Squared Error (MSE), R-squared.")
print("   - Pima: Evaluated using Accuracy, Precision, Recall, F1-Score, ROC-AUC.")
print("3. Preprocessing Needs:")
print("   - UCI (via sklearn): Comes pre-scaled and ready for regression modeling.")
print("   - Pima: Requires handling of missing values (e.g., zeroes for blood pressure/BMI) and explicit feature scaling.")

# Quick statistical comparison
print("\n[ Quick Data Dimensions ]")
uci_data = load_diabetes()
print(f"UCI Dataset shape: {uci_data.data.shape} (Features), {uci_data.target.shape} (Target)")

pima_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
try:
    df_pima = pd.read_csv(pima_url, header=None)
    print(f"Pima Indians Dataset shape: {df_pima.shape}")
except:
    print("Could not load Pima Indians dataset shape.")
