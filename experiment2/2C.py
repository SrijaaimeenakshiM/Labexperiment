import pandas as pd

print("--- Reading Data from Various Sources ---")

# 1. Reading from text file (CSV)
# Creating a dummy csv file first for demonstration
csv_filename = "dummy.csv"
csv_content = "id,value,category\n1,10,A\n2,20,B\n3,30,C"
with open(csv_filename, "w") as f:
    f.write(csv_content)

df_csv = pd.read_csv(csv_filename)
print("Data from CSV:\n", df_csv)

# 2. Reading from Excel
# Requires 'openpyxl' to be installed. We will create a dummy excel first using pandas.
excel_filename = "dummy.xlsx"
df_csv.to_excel(excel_filename, index=False)
try:
    df_excel = pd.read_excel(excel_filename)
    print("\nData from Excel:\n", df_excel)
except ImportError:
    print("\nFailed to read Excel. Please install openpyxl: pip install openpyxl")

# 3. Reading from Web
# We'll read a publicly available CSV dataset from a URL
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
try:
    print("\nReading data from web (URL):", url)
    df_web = pd.read_csv(url)
    print("Data from Web (first 5 rows):\n", df_web.head())
except Exception as e:
    print("\nFailed to read from web:", e)
