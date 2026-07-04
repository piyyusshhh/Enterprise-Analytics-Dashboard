"""
ABB Intern Assessment
Task B2 - Workforce Analysis

Objective:
- Calculate department headcount
- Calculate average salary by department
- Calculate average experience by role
- Identify top 3 locations by employee count
- Calculate percentage of employees who are
  On Leave or Resigned in each department

Developed by:
Piyush Jha
"""

# ==========================================================
# ABB Intern Assessment
# Task B2 - Workforce Analysis
# File Name: workflow_analysis.py
# ==========================================================

import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("ABB_Employee_Directory_Cleaned.csv")

print("="*60)
print("ABB WORKFORCE ANALYSIS")
print("="*60)

# -----------------------------
# Dataset Overview
# -----------------------------
print("\nTotal Employees:", len(df))

# -----------------------------
# Headcount by Department
# -----------------------------
print("\n========== HEADCOUNT BY DEPARTMENT ==========\n")

headcount = (
    df.groupby("Department")
    .size()
    .reset_index(name="Headcount")
    .sort_values(by="Headcount", ascending=False)
)

print(headcount)

# -----------------------------
# Average Salary by Department
# -----------------------------
print("\n========== AVERAGE SALARY BY DEPARTMENT ==========\n")

df["Salary"] = (
    df["Salary"]
    .astype(str)
    .str.replace(",", "", regex=False)
    .str.replace("₹", "", regex=False)
    .astype(float)
)

avg_salary = (
    df.groupby("Department")["Salary"]
    .mean()
    .round(2)
    .reset_index(name="Average Salary")
    .sort_values(by="Average Salary", ascending=False)
)

print(avg_salary)

# -----------------------------
# Average Experience by Role
# -----------------------------
print("\n========== AVERAGE EXPERIENCE BY ROLE ==========\n")

avg_exp = (
    df.groupby("Role")["Experience"]
    .mean()
    .round(2)
    .reset_index(name="Average Experience")
    .sort_values(by="Average Experience", ascending=False)
)

print(avg_exp)

# -----------------------------
# Top 3 Locations
# -----------------------------
print("\n========== TOP 3 LOCATIONS ==========\n")

top_locations = (
    df["Location"]
    .value_counts()
    .head(3)
    .reset_index()
)

top_locations.columns = ["Location", "Employee Count"]

print(top_locations)

# -----------------------------
# Percentage of Employees
# On Leave or Resigned
# -----------------------------
print("\n========== STATUS PERCENTAGE ==========\n")

inactive = (
    df[df["Status"].isin(["On Leave", "Resigned"])]
    .groupby("Department")
    .size()
    .reset_index(name="Inactive Employees")
)

department_total = (
    df.groupby("Department")
    .size()
    .reset_index(name="Total Employees")
)

status_analysis = department_total.merge(
    inactive,
    on="Department",
    how="left"
)

status_analysis["Inactive Employees"] = (
    status_analysis["Inactive Employees"]
    .fillna(0)
)

status_analysis["Percentage"] = (
    status_analysis["Inactive Employees"]
    /
    status_analysis["Total Employees"]
    * 100
).round(2)

print(status_analysis)

# -----------------------------
# Save Results
# -----------------------------

headcount.to_csv(
    "Headcount_by_Department.csv",
    index=False
)

avg_salary.to_csv(
    "Average_Salary_by_Department.csv",
    index=False
)

avg_exp.to_csv(
    "Average_Experience_by_Role.csv",
    index=False
)

top_locations.to_csv(
    "Top_3_Locations.csv",
    index=False
)

status_analysis.to_csv(
    "Department_Status_Percentage.csv",
    index=False
)

print("\n===================================")
print("Analysis Completed Successfully")
print("CSV files generated successfully.")
print("===================================")