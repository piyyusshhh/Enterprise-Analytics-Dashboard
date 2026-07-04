import pandas as pd

# 1. Load Datasets
employee_df = pd.read_csv("../Data/ABB_Employee_Directory 1.csv")
system_df = pd.read_csv("../Data/ABB_System_Architecture 1.csv")
access_df = pd.read_csv("../Data/ABB_Access_Control_Matrix 1.csv")

# 2. Create Working Copies
employee_clean = employee_df.copy()
system_clean = system_df.copy()
access_clean = access_df.copy()

# 3. Handle Missing Values in Employee Directory
# Replace missing phone numbers with 'Not Available'
employee_clean["Phone"] = employee_clean["Phone"].fillna("Not Available")

# Replace missing locations with 'Unknown'
employee_clean["Location"] = employee_clean["Location"].fillna("Unknown")

# Replace missing access levels with 'Unknown' (security-sensitive)
employee_clean["Access_Level"] = employee_clean["Access_Level"].fillna("Unknown")

# Preserving missing Manager_ID values (9 records) as they represent top-level executives

# 4. Convert Date Columns to Datetime Format
employee_clean["Date_of_Birth"] = pd.to_datetime(
    employee_clean["Date_of_Birth"],
    format="mixed",
    dayfirst=True
)

employee_clean["Join_Date"] = pd.to_datetime(
    employee_clean["Join_Date"],
    format="mixed",
    dayfirst=True
)

# 5. Correct Invalid Numerical Data (Negative Experience)
employee_clean.loc[
    employee_clean["Experience_Years"] < 0,
    "Experience_Years"
] = 0

# 6. Verify Data Quality
print("Duplicate records count:", employee_clean.duplicated().sum())
print("\nFinal missing values verification:")
print(employee_clean.isnull().sum())

# 7. Export Clean Datasets to CSV
employee_clean.to_csv("../Data/Clean/Employee_Directory_Clean.csv", index=False)
system_clean.to_csv("../Data/Clean/System_Architecture_Clean.csv", index=False)
access_clean.to_csv("../Data/Clean/Access_Control_Matrix_Clean.csv", index=False)
