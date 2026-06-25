import pandas as pd
import os

RAW_PATH = "data/raw"

 
#Now we load all the CSV files and check their structure 

csv_files = [f for f in os.listdir(RAW_PATH) if f.endswith(".csv")]

for file in csv_files:
    print(f"\nReading file: {file}")
    
    df = pd.read_csv(os.path.join(RAW_PATH, file))
    
    print("Shape:", df.shape)
    print("\nColumn Types:\n", df.dtypes)
    print("\nTop Rows:\n", df.head())
    
    print("\nMissing Values:\n", df.isnull().sum())
    print("-" * 40)

 
# Fund Master Exploration
 
fund_master = pd.read_csv("data/raw/fund_master.csv")

print("\nUnique Fund Houses:\n", fund_master["fund_house"].unique())
print("\nCategories:\n", fund_master["category"].unique())
print("\nSub-Categories:\n", fund_master["subcategory"].unique())
print("\nRisk Grades:\n", fund_master["risk_grade"].unique())
 
# AMFI Code Validation
 
nav_history = pd.read_csv("data/raw/nav_history.csv")

missing = set(fund_master["amfi_code"]) - set(nav_history["amfi_code"])

print("\nMissing AMFI Codes:", missing)

print("\nData Quality Summary")
print("Total codes in fund_master:", len(fund_master))
print("Unique codes in nav_history:", nav_history["amfi_code"].nunique())
print("Missing codes count:", len(missing))