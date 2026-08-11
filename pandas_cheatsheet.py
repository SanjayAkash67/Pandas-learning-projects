
"""=========================================="""
""" USE ONLY FOR REFERENCE NOT FOR EXECUTION """
"""=========================================="""


"""
PANDAS CHEAT SHEET
==================

Purpose:
    A syntax-first reference for the Pandas operations covered in the
    Pandas Learning by Projects series.

Important:
    - This file contains syntax and explanations only.
    - No dataset is required.
    - Examples use generic DataFrame/Series names.
    - Replace column names such as "Name", "Salary", "Revenue", etc.
      with the columns in your own dataset.

Series = one-dimensional labeled data
DataFrame = two-dimensional labeled tabular data

"""

import pandas as pd
import numpy as np


# ============================================================
# 1. IMPORT
# ============================================================

import pandas as pd

# Import NumPy when Pandas operations need numerical utilities.
import numpy as np


# ============================================================
# 2. CREATE SERIES AND DATAFRAMES
# ============================================================

# Create a Series
s = pd.Series([10, 20, 30])

# Create a Series with custom index
s = pd.Series([10, 20, 30], index=["a", "b", "c"])

# Create a DataFrame from a dictionary
df = pd.DataFrame({
    "Name": [],
    "Age": [],
    "Salary": []
})

# Create an empty DataFrame
df = pd.DataFrame()


# ============================================================
# 3. READ DATA
# ============================================================

# Read CSV
df = pd.read_csv("file.csv")

# Read CSV with selected columns
df = pd.read_csv(
    "file.csv",
    usecols=["Name", "Salary"]
)

# Read CSV with explicit data types
df = pd.read_csv(
    "file.csv",
    dtype={"EmployeeID": "int32"}
)

# Read CSV in chunks for large datasets
chunks = pd.read_csv(
    "file.csv",
    chunksize=10000
)

# Read Excel
df = pd.read_excel(
    "file.xlsx",
    sheet_name="Sheet1"
)

# Read all Excel sheets into a dictionary of DataFrames
all_sheets = pd.read_excel(
    "file.xlsx",
    sheet_name=None
)

# Work with an Excel workbook
excel_file = pd.ExcelFile("file.xlsx")

# List sheet names
excel_file.sheet_names

# Read a sheet from an ExcelFile object
df = pd.read_excel(
    excel_file,
    sheet_name="Sheet1"
)

# Read only selected Excel columns
df = pd.read_excel(
    "file.xlsx",
    usecols=["Name", "Salary"]
)

# Skip rows while reading
df = pd.read_excel(
    "file.xlsx",
    skiprows=2
)

# Read only a limited number of rows
df = pd.read_excel(
    "file.xlsx",
    nrows=100
)

# Treat custom values as missing values
df = pd.read_excel(
    "file.xlsx",
    na_values=["N/A", "NA", "-", "Unknown"]
)


# ============================================================
# 4. WRITE / EXPORT DATA
# ============================================================

# Write DataFrame to CSV
df.to_csv(
    "output.csv",
    index=False
)

# Write DataFrame to Excel
df.to_excel(
    "output.xlsx",
    index=False
)

# Write multiple DataFrames to multiple Excel sheets
with pd.ExcelWriter("report.xlsx") as writer:
    df.to_excel(
        writer,
        sheet_name="Data",
        index=False
    )

# Example of multiple sheets
with pd.ExcelWriter("report.xlsx") as writer:
    summary.to_excel(
        writer,
        sheet_name="Summary",
        index=False
    )

    report.to_excel(
        writer,
        sheet_name="Report",
        index=False
    )


# ============================================================
# 5. INSPECT DATA
# ============================================================

# First rows
df.head()

# First N rows
df.head(10)

# Last rows
df.tail()

# Last N rows
df.tail(10)

# Random rows
df.sample(5)

# Number of rows and columns
df.shape

# Number of dimensions
df.ndim

# Number of elements
df.size

# Column names
df.columns

# Row index
df.index

# Data types
df.dtypes

# DataFrame information
df.info()

# Statistical summary for numerical columns
df.describe()

# Statistical summary including non-numerical columns
df.describe(include="all")


# ============================================================
# 6. SELECT COLUMNS
# ============================================================

# Select one column
df["Name"]

# Select multiple columns
df[["Name", "Age", "Salary"]]

# Select using attribute syntax
df.Salary

# Note:
# df["Salary"] is preferred because it works reliably with all
# valid column names.


# ============================================================
# 7. SELECT ROWS
# ============================================================

# Select by integer position
df.iloc[0]

# Select multiple rows by position
df.iloc[0:5]

# Select specific rows
df.iloc[[0, 2, 5]]

# Select specific rows and columns by position
df.iloc[0:5, 0:3]

# Select by label
df.loc[0]

# Select rows using a label condition
df.loc[df["Salary"] > 50000]

# Select specific rows and columns by labels
df.loc[
    df["Salary"] > 50000,
    ["Name", "Salary"]
]


# ============================================================
# 8. INDEX OPERATIONS
# ============================================================

# Set a column as the index
df = df.set_index("EmployeeID")

# Reset index
df = df.reset_index()

# Reset index without keeping old index
df = df.reset_index(drop=True)

# Rename index
df.index.name = "ID"


# ============================================================
# 9. RENAME COLUMNS
# ============================================================

# Rename selected columns
df = df.rename(
    columns={
        "old_name": "new_name"
    }
)

# Rename all columns
df.columns = [
    "Column1",
    "Column2",
    "Column3"
]

# Convert column names to lowercase
df.columns = df.columns.str.lower()

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()


# ============================================================
# 10. DATA TYPES
# ============================================================

# Check data types
df.dtypes

# Convert a column
df["Age"] = df["Age"].astype("int64")

# Convert to string
df["Name"] = df["Name"].astype("string")

# Convert to category
df["Department"] = df["Department"].astype("category")

# Convert to numeric safely
df["Salary"] = pd.to_numeric(
    df["Salary"],
    errors="coerce"
)

# Convert to datetime
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)


# ============================================================
# 11. MISSING VALUES
# ============================================================

# Detect missing values
df.isna()

# Count missing values by column
df.isna().sum()

# Alternative
df.isnull().sum()

# Check whether any value is missing in each column
df.isna().any()

# Check whether the entire DataFrame contains missing values
df.isna().any().any()

# Select rows containing missing values
df[df["Salary"].isna()]

# Select rows where values are NOT missing
df[df["Salary"].notna()]

# Drop rows containing any missing value
df = df.dropna()

# Drop rows only when specific columns are missing
df = df.dropna(
    subset=["Salary", "Department"]
)

# Drop columns containing missing values
df = df.dropna(axis=1)

# Fill missing values with a constant
df["Salary"] = df["Salary"].fillna(0)

# Fill with mean
df["Salary"] = df["Salary"].fillna(
    df["Salary"].mean()
)

# Fill with median
df["Salary"] = df["Salary"].fillna(
    df["Salary"].median()
)

# Fill with mode
df["Department"] = df["Department"].fillna(
    df["Department"].mode()[0]
)

# Forward fill
df = df.ffill()

# Backward fill
df = df.bfill()


# ============================================================
# 12. DUPLICATES
# ============================================================

# Detect duplicate rows
df.duplicated()

# Count duplicate rows
df.duplicated().sum()

# Remove duplicate rows
df = df.drop_duplicates()

# Detect duplicates based on selected columns
df.duplicated(
    subset=["Email"]
)

# Remove duplicates based on selected columns
df = df.drop_duplicates(
    subset=["Email"]
)

# Keep the last duplicate instead of the first
df = df.drop_duplicates(
    subset=["Email"],
    keep="last"
)


# ============================================================
# 13. FILTERING
# ============================================================

# One condition
df[df["Salary"] > 50000]

# Equal to
df[df["Department"] == "IT"]

# Not equal to
df[df["Department"] != "IT"]

# Greater than or equal
df[df["Age"] >= 18]

# Less than or equal
df[df["Salary"] <= 100000]

# Multiple conditions: AND
df[
    (df["Salary"] > 50000) &
    (df["Age"] > 25)
]

# Multiple conditions: OR
df[
    (df["Department"] == "IT") |
    (df["Department"] == "HR")
]

# NOT
df[
    ~(df["Department"] == "IT")
]

# Membership filtering
df[df["Department"].isin(["IT", "HR"])]

# Exclude values using ~
df[
    ~df["Department"].isin(["IT", "HR"])
]

# Range filtering
df[
    df["Salary"].between(50000, 100000)
]

# Query syntax
df.query("Salary > 50000")

# Multiple query conditions
df.query(
    "Salary > 50000 and Age >= 25"
)


# ============================================================
# 14. SORTING
# ============================================================

# Sort ascending
df = df.sort_values("Salary")

# Sort descending
df = df.sort_values(
    "Salary",
    ascending=False
)

# Sort by multiple columns
df = df.sort_values(
    ["Department", "Salary"],
    ascending=[True, False]
)

# Sort by index
df = df.sort_index()

# Smallest N values
df.nsmallest(
    5,
    "Salary"
)

# Largest N values
df.nlargest(
    5,
    "Salary"
)


# ============================================================
# 15. VALUE COUNTS
# ============================================================

# Count unique values
df["Department"].value_counts()

# Include missing values
df["Department"].value_counts(
    dropna=False
)

# Normalize into proportions
df["Department"].value_counts(
    normalize=True
)

# Sort by index
df["Department"].value_counts().sort_index()


# ============================================================
# 16. UNIQUE VALUES
# ============================================================

# Unique values
df["Department"].unique()

# Number of unique values
df["Department"].nunique()

# Include missing values in count
df["Department"].nunique(
    dropna=False
)


# ============================================================
# 17. BASIC STATISTICS
# ============================================================

df["Salary"].sum()
df["Salary"].mean()
df["Salary"].median()
df["Salary"].min()
df["Salary"].max()
df["Salary"].std()
df["Salary"].var()

# Count non-missing values
df["Salary"].count()

# Quantile
df["Salary"].quantile(0.25)
df["Salary"].quantile(0.50)
df["Salary"].quantile(0.75)

# Multiple quantiles
df["Salary"].quantile(
    [0.25, 0.50, 0.75]
)


# ============================================================
# 18. CREATE / MODIFY COLUMNS
# ============================================================

# Create a calculated column
df["Revenue"] = (
    df["Quantity"] *
    df["Price"]
)

# Create a column using a condition
df["Status"] = (
    df["Salary"] > 50000
).map({
    True: "High",
    False: "Low"
})

# Modify an existing column
df["Salary"] = df["Salary"] * 1.10

# Drop a column
df = df.drop(
    columns=["Status"]
)

# Drop multiple columns
df = df.drop(
    columns=["Status", "TemporaryColumn"]
)


# ============================================================
# 19. APPLY
# ============================================================

# Apply a function to a Series
df["Salary"] = df["Salary"].apply(
    lambda x: x * 1.10
)

# Apply a function row-wise
def classify(row):
    if row["Salary"] > 50000:
        return "High"
    return "Low"

df["SalaryLevel"] = df.apply(
    classify,
    axis=1
)

# axis=0 -> operate column-wise
# axis=1 -> operate row-wise


# ============================================================
# 20. MAP
# ============================================================

# Replace values using a dictionary
df["Department"] = df["Department"].map({
    "IT": "Technology",
    "HR": "Human Resources"
})

# Boolean mapping
df["Status"] = df["Status"].map({
    True: "Yes",
    False: "No"
})


# ============================================================
# 21. GROUPBY
# ============================================================

# Group by one column
df.groupby("Department")

# Group and calculate sum
df.groupby("Department")["Salary"].sum()

# Group and calculate mean
df.groupby("Department")["Salary"].mean()

# Group and calculate multiple statistics
df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "min", "max"]
)

# Group by multiple columns
df.groupby(
    ["Department", "City"]
)["Salary"].sum()

# Return group keys as normal columns
df.groupby(
    "Department",
    as_index=False
)["Salary"].sum()


# ============================================================
# 22. AGGREGATION WITH NAMED OUTPUTS
# ============================================================

report = (
    df.groupby("Department")
    .agg(
        TotalSalary=("Salary", "sum"),
        AverageSalary=("Salary", "mean"),
        EmployeeCount=("EmployeeID", "count"),
        MaximumSalary=("Salary", "max"),
        MinimumSalary=("Salary", "min")
    )
    .reset_index()
)


# ============================================================
# 23. MULTIPLE AGGREGATIONS
# ============================================================

report = (
    df.groupby("Category")
    .agg({
        "Revenue": ["sum", "mean", "max"],
        "Quantity": ["sum", "mean"]
    })
)


# ============================================================
# 24. MERGE / JOIN
# ============================================================

# Inner join
merged = pd.merge(
    df1,
    df2,
    on="EmployeeID",
    how="inner"
)

# Left join
merged = pd.merge(
    df1,
    df2,
    on="EmployeeID",
    how="left"
)

# Right join
merged = pd.merge(
    df1,
    df2,
    on="EmployeeID",
    how="right"
)

# Outer join
merged = pd.merge(
    df1,
    df2,
    on="EmployeeID",
    how="outer"
)

# Different column names
merged = pd.merge(
    df1,
    df2,
    left_on="EmployeeID",
    right_on="ID",
    how="left"
)

# Merge using multiple columns
merged = pd.merge(
    df1,
    df2,
    on=["EmployeeID", "Department"],
    how="left"
)

# Add merge indicator
merged = pd.merge(
    df1,
    df2,
    on="EmployeeID",
    how="outer",
    indicator=True
)

# Control overlapping column names
merged = pd.merge(
    df1,
    df2,
    on="EmployeeID",
    suffixes=("_employee", "_sales")
)


# ============================================================
# 25. CONCAT
# ============================================================

# Stack DataFrames vertically
combined = pd.concat(
    [df1, df2],
    axis=0
)

# Combine side-by-side
combined = pd.concat(
    [df1, df2],
    axis=1
)

# Reset the index after vertical concatenation
combined = pd.concat(
    [df1, df2],
    ignore_index=True
)


# ============================================================
# 26. PIVOT TABLES
# ============================================================

# Basic pivot table
pivot = pd.pivot_table(
    df,
    values="Revenue",
    index="Department",
    aggfunc="sum"
)

# Add columns dimension
pivot = pd.pivot_table(
    df,
    values="Revenue",
    index="Department",
    columns="City",
    aggfunc="sum"
)

# Fill missing combinations
pivot = pd.pivot_table(
    df,
    values="Revenue",
    index="Department",
    columns="City",
    aggfunc="sum",
    fill_value=0
)

# Multiple aggregation functions
pivot = pd.pivot_table(
    df,
    values="Revenue",
    index="Department",
    aggfunc=["sum", "mean", "max"]
)

# Multiple values
pivot = pd.pivot_table(
    df,
    values=["Revenue", "Quantity"],
    index="Department",
    aggfunc="sum"
)

# Add grand totals
pivot = pd.pivot_table(
    df,
    values="Revenue",
    index="Department",
    columns="City",
    aggfunc="sum",
    fill_value=0,
    margins=True
)

# Convert pivot index back to columns
pivot = pivot.reset_index()


# ============================================================
# 27. CROSSTAB
# ============================================================

# Frequency table
cross = pd.crosstab(
    df["Department"],
    df["City"]
)

# Normalize by row
cross = pd.crosstab(
    df["Department"],
    df["City"],
    normalize="index"
)

# Normalize by column
cross = pd.crosstab(
    df["Department"],
    df["City"],
    normalize="columns"
)

# Normalize over entire table
cross = pd.crosstab(
    df["Department"],
    df["City"],
    normalize="all"
)

# Crosstab with values and aggregation
cross = pd.crosstab(
    df["Department"],
    df["City"],
    values=df["Revenue"],
    aggfunc="sum"
)


# ============================================================
# 28. DATETIME / TIME SERIES
# ============================================================

# Convert to datetime
df["Date"] = pd.to_datetime(
    df["Date"]
)

# Extract year
df["Year"] = df["Date"].dt.year

# Extract month number
df["Month"] = df["Date"].dt.month

# Extract month name
df["MonthName"] = df["Date"].dt.month_name()

# Extract day
df["Day"] = df["Date"].dt.day

# Extract day name
df["DayName"] = df["Date"].dt.day_name()

# Extract weekday number
df["Weekday"] = df["Date"].dt.weekday

# Extract quarter
df["Quarter"] = df["Date"].dt.quarter

# Extract hour
df["Hour"] = df["Date"].dt.hour

# Extract minute
df["Minute"] = df["Date"].dt.minute

# Start/end of month
df["MonthStart"] = df["Date"].dt.to_period("M").dt.start_time
df["MonthEnd"] = df["Date"].dt.to_period("M").dt.end_time


# ============================================================
# 29. DATE FILTERING
# ============================================================

# Filter after a date
df[df["Date"] >= "2025-01-01"]

# Filter before a date
df[df["Date"] < "2025-12-31"]

# Filter between dates
df[
    df["Date"].between(
        "2025-01-01",
        "2025-03-31"
    )
]

# Sort by date
df = df.sort_values("Date")


# ============================================================
# 30. TIME SERIES INDEX
# ============================================================

# Set datetime column as index
df = df.set_index("Date")

# Restore normal index
df = df.reset_index()


# ============================================================
# 31. RESAMPLING
# ============================================================

# Daily sum
daily = df["Revenue"].resample("D").sum()

# Weekly sum
weekly = df["Revenue"].resample("W").sum()

# Monthly sum
monthly = df["Revenue"].resample("ME").sum()

# Quarterly sum
quarterly = df["Revenue"].resample("QE").sum()

# Yearly sum
yearly = df["Revenue"].resample("YE").sum()

# Monthly average
monthly_average = (
    df["Revenue"]
    .resample("ME")
    .mean()
)


# ============================================================
# 32. ROLLING WINDOWS / MOVING AVERAGE
# ============================================================

# 7-period rolling mean
df["RollingMean"] = (
    df["Revenue"]
    .rolling(7)
    .mean()
)

# 7-period rolling sum
df["RollingSum"] = (
    df["Revenue"]
    .rolling(7)
    .sum()
)

# Rolling maximum
df["RollingMax"] = (
    df["Revenue"]
    .rolling(7)
    .max()
)


# ============================================================
# 33. CUMULATIVE OPERATIONS
# ============================================================

# Cumulative sum
df["CumulativeRevenue"] = (
    df["Revenue"].cumsum()
)

# Cumulative maximum
df["CumulativeMax"] = (
    df["Revenue"].cummax()
)

# Cumulative minimum
df["CumulativeMin"] = (
    df["Revenue"].cummin()
)

# Cumulative product
df["CumulativeProduct"] = (
    df["Revenue"].cumprod()
)


# ============================================================
# 34. DIFFERENCE / LAG / LEAD
# ============================================================

# Difference from previous row
df["Difference"] = (
    df["Revenue"].diff()
)

# Previous value
df["PreviousRevenue"] = (
    df["Revenue"].shift(1)
)

# Next value
df["NextRevenue"] = (
    df["Revenue"].shift(-1)
)

# Percentage change
df["Growth"] = (
    df["Revenue"].pct_change()
)

# Percentage change expressed as percentage
df["GrowthPercent"] = (
    df["Revenue"].pct_change() * 100
)


# ============================================================
# 35. STRING OPERATIONS
# ============================================================

# Remove leading/trailing whitespace
df["Name"] = df["Name"].str.strip()

# Convert to lowercase
df["Name"] = df["Name"].str.lower()

# Convert to uppercase
df["Name"] = df["Name"].str.upper()

# Convert to title case
df["Name"] = df["Name"].str.title()

# String length
df["NameLength"] = df["Name"].str.len()

# Contains substring
df["Name"].str.contains(
    "john",
    case=False,
    na=False
)

# Starts with
df["Name"].str.startswith(
    "A",
    na=False
)

# Ends with
df["Name"].str.endswith(
    "n",
    na=False
)

# Exact regex match
df["Name"].str.match(
    r"^[A-Z]",
    na=False
)

# Replace text
df["Name"] = df["Name"].str.replace(
    "old",
    "new",
    regex=False
)

# Replace using regex
df["Phone"] = df["Phone"].str.replace(
    r"\D",
    "",
    regex=True
)

# Split string
df["FullName"].str.split()

# Split into separate columns
df[["FirstName", "LastName"]] = (
    df["FullName"]
    .str.split(
        " ",
        n=1,
        expand=True
    )
)

# Extract using regex
df["EmailDomain"] = (
    df["Email"]
    .str.extract(
        r"@(.+)$"
    )
)

# Extract a phone number
df["PhoneNumber"] = (
    df["Text"]
    .str.extract(
        r"(\d{10})"
    )
)


# ============================================================
# 36. STRING CLEANING PIPELINE
# ============================================================

df["Name"] = (
    df["Name"]
    .astype("string")
    .str.strip()
    .str.lower()
    .str.title()
)


# ============================================================
# 37. MEMORY USAGE
# ============================================================

# Memory usage of each column
df.memory_usage()

# Include deep memory usage for object/string data
df.memory_usage(
    deep=True
)

# Total memory usage
df.memory_usage(
    deep=True
).sum()

# Convert bytes to MB
memory_mb = (
    df.memory_usage(deep=True).sum()
    / (1024 ** 2)
)


# ============================================================
# 38. MEMORY OPTIMIZATION
# ============================================================

# Convert repeated strings to category
df["Department"] = (
    df["Department"]
    .astype("category")
)

# Use smaller integer type when values fit
df["Quantity"] = (
    df["Quantity"]
    .astype("int8")
)

# Use smaller integer type
df["EmployeeID"] = (
    df["EmployeeID"]
    .astype("int32")
)

# Specify only required columns while reading
df = pd.read_csv(
    "large_file.csv",
    usecols=[
        "EmployeeID",
        "Department",
        "Revenue"
    ]
)


# ============================================================
# 39. LARGE DATASET CHUNK PROCESSING
# ============================================================

# Read a large CSV in chunks
for chunk in pd.read_csv(
    "large_file.csv",
    chunksize=10000
):
    # Process one chunk at a time
    pass

# Count rows incrementally
total_rows = 0

for chunk in pd.read_csv(
    "large_file.csv",
    chunksize=10000
):
    total_rows += len(chunk)


# Incremental sum
total_revenue = 0

for chunk in pd.read_csv(
    "large_file.csv",
    chunksize=10000
):
    total_revenue += (
        chunk["Revenue"].sum()
    )


# Chunk-level groupby results
results = []

for chunk in pd.read_csv(
    "large_file.csv",
    chunksize=10000
):
    result = (
        chunk
        .groupby("Category")["Revenue"]
        .sum()
    )

    results.append(result)

# Combine chunk results
combined = pd.concat(results)

# Aggregate again because the same group may occur
# in multiple chunks
final_result = (
    combined
    .groupby(level=0)
    .sum()
)


# ============================================================
# 40. CHUNK PROCESSING WITH DATAFRAME OUTPUT
# ============================================================

results = []

for chunk in pd.read_csv(
    "large_file.csv",
    chunksize=10000
):
    result = (
        chunk
        .groupby("Category")["Revenue"]
        .sum()
        .reset_index()
    )

    results.append(result)

combined = pd.concat(
    results,
    ignore_index=True
)

final_result = (
    combined
    .groupby("Category", as_index=False)["Revenue"]
    .sum()
)


# ============================================================
# 41. CONDITIONAL COLUMNS
# ============================================================

# Boolean condition
df["HighValue"] = (
    df["Revenue"] > 100000
)

# Multiple conditions with np.select
conditions = [
    df["Revenue"] >= 100000,
    df["Revenue"] >= 50000,
    df["Revenue"] < 50000
]

choices = [
    "High",
    "Medium",
    "Low"
]

df["RevenueLevel"] = np.select(
    conditions,
    choices,
    default="Unknown"
)


# ============================================================
# 42. REPLACE VALUES
# ============================================================

# Replace one value
df["Department"] = (
    df["Department"]
    .replace(
        "IT",
        "Technology"
    )
)

# Replace multiple values
df["Department"] = (
    df["Department"]
    .replace({
        "IT": "Technology",
        "HR": "Human Resources"
    })
)


# ============================================================
# 43. DROP ROWS / COLUMNS
# ============================================================

# Drop a row by index
df = df.drop(index=0)

# Drop multiple rows
df = df.drop(
    index=[0, 1, 2]
)

# Drop a column
df = df.drop(
    columns="Salary"
)

# Drop multiple columns
df = df.drop(
    columns=["Salary", "Age"]
)


# ============================================================
# 44. INSERT / REORDER COLUMNS
# ============================================================

# Insert a column at a specific position
df.insert(
    1,
    "NewColumn",
    values=None
)

# Reorder columns
df = df[
    [
        "EmployeeID",
        "Name",
        "Department",
        "Salary"
    ]
]


# ============================================================
# 45. COPY
# ============================================================

# Independent copy
df_copy = df.copy()

# Avoid accidentally modifying the original DataFrame
# when performing transformations on a separate object.


# ============================================================
# 46. RESETTING / IGNORING INDEX AFTER OPERATIONS
# ============================================================

df = df.reset_index(drop=True)

combined = pd.concat(
    [df1, df2],
    ignore_index=True
)


# ============================================================
# 47. DATA VALIDATION PATTERNS
# ============================================================

# Check duplicate IDs
df["EmployeeID"].duplicated().sum()

# Check missing IDs
df["EmployeeID"].isna().sum()

# Check whether a calculated column is correct
calculated_revenue = (
    df["Quantity"] *
    df["Price"]
)

df["Revenue"].equals(
    calculated_revenue
)

# Raise an error if validation fails
if not df["Revenue"].equals(
    calculated_revenue
):
    raise ValueError(
        "Revenue calculation mismatch."
    )


# ============================================================
# 48. FIND ROWS WITH MAX / MIN VALUES
# ============================================================

# Index of maximum value
idx = df["Revenue"].idxmax()

# Row containing maximum value
best_row = df.loc[idx]

# Index of minimum value
idx = df["Revenue"].idxmin()

# Row containing minimum value
lowest_row = df.loc[idx]

# Top N rows
top_rows = df.nlargest(
    10,
    "Revenue"
)


# ============================================================
# 49. RESET / RENAME AFTER GROUPBY
# ============================================================

report = (
    df.groupby("Department")["Salary"]
    .sum()
    .reset_index()
)

report.columns = [
    "Department",
    "TotalSalary"
]


# ============================================================
# 50. COMMON PIPELINE PATTERN
# ============================================================

# A common Pandas analysis workflow:
#
# 1. Load
# 2. Inspect
# 3. Clean
# 4. Transform
# 5. Filter
# 6. Combine
# 7. Aggregate
# 8. Analyze
# 9. Export

df = pd.read_csv("data.csv")

df.info()

df = df.drop_duplicates()

df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce"
)

df["Revenue"] = (
    df["Quantity"] *
    df["Price"]
)

report = (
    df[df["Revenue"] > 50000]
    .groupby("Category")
    .agg(
        Orders=("OrderID", "count"),
        Revenue=("Revenue", "sum"),
        AverageRevenue=("Revenue", "mean")
    )
    .reset_index()
    .sort_values(
        "Revenue",
        ascending=False
    )
)

report.to_csv(
    "output/report.csv",
    index=False
)


# ============================================================
# 51. QUICK REFERENCE — MOST USED OPERATIONS
# ============================================================

# Loading
pd.read_csv(...)
pd.read_excel(...)

# Inspection
df.head()
df.tail()
df.shape
df.info()
df.describe()
df.dtypes

# Selection
df["Column"]
df[["A", "B"]]
df.loc[...]
df.iloc[...]

# Cleaning
df.isna()
df.dropna()
df.fillna(...)
df.duplicated()
df.drop_duplicates()

# Filtering
df[df["Column"] > value]
df["Column"].isin([...])
df["Column"].between(a, b)
df.query("Column > value")

# Sorting
df.sort_values(...)
df.sort_index()
df.nlargest(...)
df.nsmallest()

# Transformation
df["New"] = ...
df.apply(...)
df.map(...)
df.astype(...)

# Grouping
df.groupby(...)
df.agg(...)

# Combining
pd.merge(...)
pd.concat(...)

# Pivoting
pd.pivot_table(...)
pd.crosstab(...)

# Datetime
pd.to_datetime(...)
df["Date"].dt.year
df["Date"].dt.month
df.resample(...)
df.rolling(...)
df.diff()
df.shift()
df.pct_change()

# Strings
df["Column"].str.strip()
df["Column"].str.lower()
df["Column"].str.upper()
df["Column"].str.contains(...)
df["Column"].str.replace(...)
df["Column"].str.split(...)
df["Column"].str.extract(...)

# Large datasets
df.memory_usage(deep=True)
pd.read_csv(..., usecols=...)
pd.read_csv(..., chunksize=...)

# Export
df.to_csv(...)
df.to_excel(...)


# ============================================================
# 52. END-TO-END REVISION CHECKLIST
# ============================================================

"""
Before starting the large-scale Pandas project, make sure you can
recognize and use these categories:

[ ] Create DataFrame / Series
[ ] Read CSV
[ ] Read Excel
[ ] Inspect Data
[ ] Select Rows / Columns
[ ] loc / iloc
[ ] Index Management
[ ] Rename Columns
[ ] Change Data Types
[ ] Handle Missing Values
[ ] Handle Duplicates
[ ] Filter Data
[ ] Sort Data
[ ] value_counts
[ ] unique / nunique
[ ] Statistics
[ ] Create Calculated Columns
[ ] apply / map
[ ] groupby
[ ] agg
[ ] merge / joins
[ ] concat
[ ] pivot_table
[ ] crosstab
[ ] Datetime Operations
[ ] Resampling
[ ] Rolling Windows
[ ] diff / shift / pct_change
[ ] String Operations
[ ] Regex Extraction
[ ] Memory Usage
[ ] dtype Optimization
[ ] Chunk Processing
[ ] CSV Export
[ ] Excel Export
[ ] ExcelWriter
[ ] Data Validation

The purpose of this file is revision. The large-scale project will
require combining these operations rather than using them in isolation.
"""
