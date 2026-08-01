import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score

print("--- Bivariate analysis: Linear and Logistic Regression modeling ---")

# 1. Linear Regression (UCI Diabetes Dataset - Regression problem)
print("\n--- 1. Linear Regression on UCI Dataset ---")
uci_data = load_diabetes(as_frame=True)
df_uci = uci_data.frame

# Using 'bmi' to predict 'target' (Bivariate: 1 independent, 1 dependent)
X_lin = df_uci[['bmi']]
y_lin = df_uci['target']

X_train_lin, X_test_lin, y_train_lin, y_test_lin = train_test_split(X_lin, y_lin, test_size=0.2, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train_lin, y_train_lin)
y_pred_lin = lin_reg.predict(X_test_lin)

mse = mean_squared_error(y_test_lin, y_pred_lin)
print(f"Goal: Predict Disease Progression (Target) based on BMI")
print(f"Linear Regression MSE: {mse:.2f}")
print(f"Coefficient for BMI: {lin_reg.coef_[0]:.2f}")


# 2. Logistic Regression (Pima Indians Diabetes Dataset - Classification problem)
print("\n--- 2. Logistic Regression on Pima Indians Dataset ---")
pima_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigree', 'Age', 'Outcome']

try:
    df_pima = pd.read_csv(pima_url, names=columns)
    # Using 'Glucose' to predict 'Outcome' (Bivariate: 1 independent, 1 dependent)
    X_log = df_pima[['Glucose']]
    y_log = df_pima['Outcome']
    
    X_train_log, X_test_log, y_train_log, y_test_log = train_test_split(X_log, y_log, test_size=0.2, random_state=42)
    
    log_reg = LogisticRegression()
    log_reg.fit(X_train_log, y_train_log)
    y_pred_log = log_reg.predict(X_test_log)
    
    acc = accuracy_score(y_test_log, y_pred_log)
    print(f"Goal: Predict Diabetes Outcome (0 or 1) based on Glucose level")
    print(f"Logistic Regression Accuracy: {acc:.2f}")
    print(f"Coefficient for Glucose: {log_reg.coef_[0][0]:.4f}")
except Exception as e:
    print("Could not load Pima Indians dataset:", e)
