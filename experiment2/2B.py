import pandas as pd

print("--- Working with Pandas DataFrames ---")
# 1. DataFrame creation
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Paris', 'London', 'Tokyo']
}
df = pd.DataFrame(data)
print("Initial DataFrame:\n", df)

# 2. Accessing data
print("\nAccessing 'Name' column:\n", df['Name'])
print("\nAccessing first row (using iloc):\n", df.iloc[0])

# 3. Filtering
filtered_df = df[df['Age'] > 30]
print("\nFiltered DataFrame (Age > 30):\n", filtered_df)

# 4. Adding a new column
df['Salary'] = [50000, 60000, 70000, 80000]
print("\nDataFrame with Salary column:\n", df)

# 5. Descriptive statistics
print("\nDescriptive statistics of the DataFrame:\n", df.describe())
