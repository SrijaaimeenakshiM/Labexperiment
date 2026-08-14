import pandas as pd
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

print("--- Model Building and Validation: Linear Regression ---")

# Load dataset
diabetes_uci = load_diabetes(as_frame=True)
df_uci = diabetes_uci.frame

X = df_uci.drop('target', axis=1)
y = df_uci['target']

# Train-test split for holdout validation
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1. Build Model
print("Building Linear Regression Model on UCI dataset...")
lin_model = LinearRegression()
lin_model.fit(X_train, y_train)

# 2. Validation (Holdout)
y_pred = lin_model.predict(X_test)

print("\n[ 1. Holdout Validation Metrics (20% Test Set) ]")
print(f"Mean Squared Error (MSE): {mean_squared_error(y_test, y_pred):.2f}")
print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred):.2f}")
print(f"R-squared (R2): {r2_score(y_test, y_pred):.4f}")

# 3. K-Fold Cross Validation
print("\n[ 2. 5-Fold Cross Validation ]")
cv_scores = cross_val_score(lin_model, X, y, cv=5, scoring='r2')
print(f"CV R-squared scores for each fold: {cv_scores}")
print(f"Mean CV R-squared: {cv_scores.mean():.4f}")
print(f"Standard Deviation of CV R-squared: {cv_scores.std():.4f}")
