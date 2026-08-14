import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

print("--- Model Building and Validation: Logistic Regression ---")

# Using Pima Indians dataset for Classification (Logistic Regression)
pima_url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigree', 'Age', 'Outcome']

try:
    df_pima = pd.read_csv(pima_url, names=columns)
    
    # Simple data cleaning: Handle missing values (0s in biological data)
    cols_to_replace = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    df_pima[cols_to_replace] = df_pima[cols_to_replace].replace(0, pd.NA)
    # Fill missing with median for simplicity
    df_pima = df_pima.fillna(df_pima.median(numeric_only=True))
    
    X = df_pima.drop('Outcome', axis=1)
    y = df_pima['Outcome']
    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 1. Build Model (Increased max_iter for convergence)
    print("Building Logistic Regression Model on Pima Indians dataset...")
    log_model = LogisticRegression(max_iter=1000)
    log_model.fit(X_train, y_train)
    
    # 2. Validation (Holdout)
    y_pred = log_model.predict(X_test)
    
    print("\n[ 1. Holdout Validation Metrics (20% Test Set) ]")
    print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
    print(f"Precision: {precision_score(y_test, y_pred):.4f}")
    print(f"Recall:    {recall_score(y_test, y_pred):.4f}")
    print(f"F1-Score:  {f1_score(y_test, y_pred):.4f}")
    
    print("\n[ Classification Report ]")
    print(classification_report(y_test, y_pred))
    
    # 3. K-Fold Cross Validation
    print("\n[ 2. 5-Fold Cross Validation (Accuracy) ]")
    cv_scores = cross_val_score(log_model, X, y, cv=5, scoring='accuracy')
    print(f"CV Accuracy scores for each fold: {cv_scores}")
    print(f"Mean CV Accuracy: {cv_scores.mean():.4f}")

except Exception as e:
    print(f"Error processing dataset: {e}")
