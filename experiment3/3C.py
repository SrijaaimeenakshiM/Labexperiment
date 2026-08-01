import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

print("--- Multiple Regression analysis ---")

# We use the UCI Diabetes Dataset for multiple regression
diabetes_uci = load_diabetes(as_frame=True)
df_uci = diabetes_uci.frame

# Using multiple features to predict target
X = df_uci.drop('target', axis=1)
y = df_uci['target']

print("Dataset: UCI Diabetes Dataset")
print("Features used for Multiple Regression:")
print(list(X.columns))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

multi_reg = LinearRegression()
multi_reg.fit(X_train, y_train)

y_pred = multi_reg.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n--- Multiple Regression Results ---")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared Score: {r2:.4f}")

print("\n--- Coefficients for each feature ---")
for feature, coef in zip(X.columns, multi_reg.coef_):
    print(f"{feature:10}: {coef:>10.2f}")
