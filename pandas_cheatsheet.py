"""
🐼 PANDAS CHEAT SHEET — RUNNABLE LEARNING REFERENCE
===================================================

This is a SELF-CONTAINED, executable Pandas reference file.

Unlike a syntax-only cheat sheet:
    • It contains a small built-in demo dataset.
    • Every section can be executed safely.
    • Examples show BOTH code and what the operation means.
    • No external dataset is required.
    • No undefined df1 / df2 / summary / report variables.
    • No file needs to exist before running the script.

Run:
    python pandas_cheatsheet.py

The examples are intentionally small so this file is useful for
learning and revision rather than benchmarking.

Requirements:
    pandas
    numpy

Excel examples use openpyxl when available. If it is not installed,
the script skips only the Excel demonstration instead of crashing.

Use this file as a reference:
    1. Run it once to see the operations.
    2. Find the section you need.
    3. Copy/adapt the example for your own project.
"""

import os
import tempfile
from io import StringIO, BytesIO

import pandas as pd
import numpy as np


# ================================================================
# 0. DEMO DATA
# ================================================================

def make_demo_data():
    """Create small DataFrames used throughout the cheat sheet."""

    employees = pd.DataFrame({
        "EmployeeID": [101, 102, 103, 104, 105, 106],
        "Name": ["Alice", "Bob", "Charlie", "Diana", "Evan", "Fiona"],
        "Department": ["IT", "HR", "IT", "Sales", "Sales", "HR"],
        "City": ["Chennai", "Coimbatore", "Chennai", "Bengaluru", "Chennai", "Coimbatore"],
        "Age": [24, 31, 27, 35, 29, 42],
        "Salary": [55000, 48000, 72000, 65000, 58000, 52000],
        "JoinDate": pd.to_datetime([
            "2023-01-10", "2022-05-15", "2021-08-20",
            "2020-03-12", "2024-02-01", "2019-11-25"
        ]),
    })

    sales = pd.DataFrame({
        "OrderID": [1, 2, 3, 4, 5, 6, 7, 8],
        "EmployeeID": [101, 102, 101, 104, 105, 103, 104, 106],
        "Category": ["Laptop", "Phone", "Laptop", "Monitor", "Phone", "Keyboard", "Monitor", "Phone"],
        "Quantity": [2, 3, 1, 2, 4, 5, 1, 2],
        "Price": [70000, 25000, 70000, 18000, 25000, 3000, 18000, 25000],
        "OrderDate": pd.to_datetime([
            "2025-01-05", "2025-01-08", "2025-01-15", "2025-02-02",
            "2025-02-10", "2025-03-01", "2025-03-12", "2025-03-20"
        ])
    })

    dirty = pd.DataFrame({
        "Name": [" Alice ", "Bob", "Bob", None, "Diana"],
        "Department": ["IT", "HR", "HR", "Sales", None],
        "Salary": [55000, 48000, 48000, np.nan, 65000],
        "Email": ["alice@example.com", "bob@example.com", "bob@example.com",
                  "charlie@example.com", None]
    })

    return employees, sales, dirty


def section(title):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


employees, sales, dirty = make_demo_data()
sales["Revenue"] = sales["Quantity"] * sales["Price"]


# ================================================================
# 1. SERIES AND DATAFRAME
# ================================================================

section("1. CREATE SERIES AND DATAFRAMES")

numbers = pd.Series([10, 20, 30])
print("\nSeries:")
print(numbers)

named_numbers = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("\nSeries with custom index:")
print(named_numbers)

print("\nDataFrame:")
print(employees.head())


# ================================================================
# 2. READ DATA
# ================================================================

section("2. READ CSV AND EXCEL")

csv_text = """Name,Department,Salary
Alice,IT,55000
Bob,HR,48000
Charlie,Sales,65000
"""

csv_df = pd.read_csv(StringIO(csv_text))
print("\nReading CSV from an in-memory string:")
print(csv_df)

print("\nReading selected CSV columns:")
print(pd.read_csv(StringIO(csv_text), usecols=["Name", "Salary"]))

print("\nReading CSV with dtype:")
typed = pd.read_csv(StringIO(csv_text), dtype={"Salary": "int64"})
print(typed.dtypes)

print("\nReading CSV in chunks:")
for chunk in pd.read_csv(StringIO(csv_text), chunksize=2):
    print(chunk)

# Excel is demonstrated safely in memory when openpyxl is available.
try:
    excel_buffer = BytesIO()
    with pd.ExcelWriter(excel_buffer, engine="openpyxl") as writer:
        csv_df.to_excel(writer, sheet_name="Employees", index=False)
    excel_buffer.seek(0)

    excel_df = pd.read_excel(excel_buffer, sheet_name="Employees")
    print("\nReading Excel:")
    print(excel_df)
except (ImportError, ModuleNotFoundError):
    print("\nExcel demo skipped: install openpyxl to enable it.")


# ================================================================
# 3. WRITE / EXPORT
# ================================================================

section("3. WRITE / EXPORT DATA")

with tempfile.TemporaryDirectory() as temp_dir:
    csv_path = os.path.join(temp_dir, "demo.csv")
    xlsx_path = os.path.join(temp_dir, "demo.xlsx")

    employees.to_csv(csv_path, index=False)
    print("\nCSV exported successfully:", csv_path)

    try:
        employees.to_excel(xlsx_path, index=False, engine="openpyxl")
        print("Excel exported successfully:", xlsx_path)
    except (ImportError, ModuleNotFoundError):
        print("Excel export skipped: install openpyxl to enable it.")

    # Multiple Excel sheets
    try:
        report_path = os.path.join(temp_dir, "report.xlsx")
        with pd.ExcelWriter(report_path, engine="openpyxl") as writer:
            employees.to_excel(writer, sheet_name="Employees", index=False)
            sales.to_excel(writer, sheet_name="Sales", index=False)
        print("Multi-sheet Excel report created:", report_path)
    except (ImportError, ModuleNotFoundError):
        print("Multi-sheet Excel demo skipped: install openpyxl.")


# ================================================================
# 4. INSPECT DATA
# ================================================================

section("4. INSPECT DATA")

print("\nhead():")
print(employees.head(3))

print("\ntail():")
print(employees.tail(2))

print("\nsample():")
print(employees.sample(2, random_state=42))

print("\nshape:", employees.shape)
print("ndim:", employees.ndim)
print("size:", employees.size)
print("\ncolumns:")
print(employees.columns.tolist())

print("\nindex:")
print(employees.index)

print("\ndtypes:")
print(employees.dtypes)

print("\ninfo():")
employees.info()

print("\ndescribe():")
print(employees.describe())

print("\ndescribe(include='all'):")
print(employees.describe(include="all"))


# ================================================================
# 5. SELECT COLUMNS
# ================================================================

section("5. SELECT COLUMNS")

print("\nOne column:")
print(employees["Name"])

print("\nMultiple columns:")
print(employees[["Name", "Department", "Salary"]])

print("\nAttribute syntax:")
print(employees.Salary)


# ================================================================
# 6. SELECT ROWS — iloc / loc
# ================================================================

section("6. SELECT ROWS — iloc AND loc")

print("\niloc[0]:")
print(employees.iloc[0])

print("\niloc[0:3]:")
print(employees.iloc[0:3])

print("\niloc[[0, 2, 4]]:")
print(employees.iloc[[0, 2, 4]])

print("\niloc rows and columns:")
print(employees.iloc[0:3, 0:3])

print("\nloc by label:")
print(employees.loc[0])

print("\nloc with condition:")
print(employees.loc[employees["Salary"] > 60000])

print("\nloc with rows and selected columns:")
print(employees.loc[
    employees["Salary"] > 60000,
    ["Name", "Department", "Salary"]
])


# ================================================================
# 7. INDEX OPERATIONS
# ================================================================

section("7. INDEX OPERATIONS")

indexed = employees.set_index("EmployeeID")
print("\nset_index():")
print(indexed)

reset = indexed.reset_index()
print("\nreset_index():")
print(reset)

reset_drop = indexed.reset_index(drop=True)
print("\nreset_index(drop=True):")
print(reset_drop)

named_index = employees.copy()
named_index.index.name = "RowNumber"
print("\nNamed index:")
print(named_index.index)


# ================================================================
# 8. RENAME COLUMNS
# ================================================================

section("8. RENAME COLUMNS")

renamed = employees.rename(columns={
    "Name": "EmployeeName",
    "Salary": "AnnualSalary"
})
print("\nSelected columns renamed:")
print(renamed.head())

lowercase = employees.copy()
lowercase.columns = lowercase.columns.str.lower()
print("\nLowercase column names:")
print(lowercase.columns.tolist())

spaced = employees.copy()
spaced.columns = [" EmployeeID ", " Name ", " Department ",
                  " City ", " Age ", " Salary ", " JoinDate "]
spaced.columns = spaced.columns.str.strip()
print("\nStripped column names:")
print(spaced.columns.tolist())


# ================================================================
# 9. DATA TYPES
# ================================================================

section("9. DATA TYPES")

print("\nCurrent dtypes:")
print(employees.dtypes)

typed = employees.copy()
typed["Age"] = typed["Age"].astype("int64")
typed["Name"] = typed["Name"].astype("string")
typed["Department"] = typed["Department"].astype("category")
typed["Salary"] = pd.to_numeric(typed["Salary"], errors="coerce")
typed["JoinDate"] = pd.to_datetime(typed["JoinDate"], errors="coerce")

print("\nAfter conversions:")
print(typed.dtypes)


# ================================================================
# 10. MISSING VALUES
# ================================================================

section("10. MISSING VALUES")

print("\nisna():")
print(dirty.isna())

print("\nMissing count:")
print(dirty.isna().sum())

print("\nMissing percentage:")
print((dirty.isna().mean() * 100).round(2))

print("\nAny missing in each column:")
print(dirty.isna().any())

print("\nAny missing anywhere:")
print(dirty.isna().any().any())

print("\nRows where Salary is missing:")
print(dirty[dirty["Salary"].isna()])

print("\nRows where Salary is not missing:")
print(dirty[dirty["Salary"].notna()])

print("\nFill Salary with 0:")
print(dirty["Salary"].fillna(0))

print("\nFill Salary with mean:")
print(dirty["Salary"].fillna(dirty["Salary"].mean()))

print("\nFill Salary with median:")
print(dirty["Salary"].fillna(dirty["Salary"].median()))

print("\nFill Department with mode:")
print(dirty["Department"].fillna(dirty["Department"].mode()[0]))

print("\nForward fill:")
print(dirty.ffill())

print("\nBackward fill:")
print(dirty.bfill())

print("\nDrop rows containing missing values:")
print(dirty.dropna())

print("\nDrop rows missing Salary or Department:")
print(dirty.dropna(subset=["Salary", "Department"]))


# ================================================================
# 11. DUPLICATES
# ================================================================

section("11. DUPLICATES")

print("\nDuplicate mask:")
print(dirty.duplicated())

print("\nDuplicate count:")
print(dirty.duplicated().sum())

print("\nDuplicate rows:")
print(dirty[dirty.duplicated()])

print("\nAfter removing duplicates:")
print(dirty.drop_duplicates())

print("\nDuplicates based on Email:")
print(dirty.duplicated(subset=["Email"]))

print("\nKeep last duplicate:")
print(dirty.drop_duplicates(subset=["Email"], keep="last"))


# ================================================================
# 12. FILTERING
# ================================================================

section("12. FILTERING")

print("\nSalary > 50000:")
print(employees[employees["Salary"] > 50000])

print("\nDepartment == IT:")
print(employees[employees["Department"] == "IT"])

print("\nDepartment != IT:")
print(employees[employees["Department"] != "IT"])

print("\nAge >= 30:")
print(employees[employees["Age"] >= 30])

print("\nSalary <= 60000:")
print(employees[employees["Salary"] <= 60000])

print("\nAND condition:")
print(employees[
    (employees["Salary"] > 50000) &
    (employees["Age"] > 25)
])

print("\nOR condition:")
print(employees[
    (employees["Department"] == "IT") |
    (employees["Department"] == "HR")
])

print("\nNOT condition:")
print(employees[~(employees["Department"] == "IT")])

print("\nisin():")
print(employees[employees["Department"].isin(["IT", "HR"])])

print("\nExclude using ~isin():")
print(employees[~employees["Department"].isin(["IT", "HR"])])

print("\nbetween():")
print(employees[employees["Salary"].between(50000, 70000)])

print("\nquery():")
print(employees.query("Salary > 50000"))

print("\nquery() with multiple conditions:")
print(employees.query("Salary > 50000 and Age >= 25"))


# ================================================================
# 13. SORTING
# ================================================================

section("13. SORTING")

print("\nAscending:")
print(employees.sort_values("Salary"))

print("\nDescending:")
print(employees.sort_values("Salary", ascending=False))

print("\nMultiple columns:")
print(employees.sort_values(
    ["Department", "Salary"],
    ascending=[True, False]
))

print("\nSort by index:")
print(employees.sort_index())

print("\nSmallest 3 salaries:")
print(employees.nsmallest(3, "Salary"))

print("\nLargest 3 salaries:")
print(employees.nlargest(3, "Salary"))


# ================================================================
# 14. VALUE COUNTS / UNIQUE
# ================================================================

section("14. VALUE COUNTS / UNIQUE VALUES")

print("\nvalue_counts():")
print(employees["Department"].value_counts())

print("\nInclude missing values:")
print(dirty["Department"].value_counts(dropna=False))

print("\nNormalized value_counts():")
print(employees["Department"].value_counts(normalize=True).round(3))

print("\nSorted by index:")
print(employees["Department"].value_counts().sort_index())

print("\nunique():")
print(employees["Department"].unique())

print("\nnunique():")
print(employees["Department"].nunique())

print("\nnunique(dropna=False):")
print(dirty["Department"].nunique(dropna=False))


# ================================================================
# 15. BASIC STATISTICS
# ================================================================

section("15. BASIC STATISTICS")

salary = employees["Salary"]

print("sum:", salary.sum())
print("mean:", salary.mean())
print("median:", salary.median())
print("min:", salary.min())
print("max:", salary.max())
print("std:", salary.std())
print("variance:", salary.var())
print("count:", salary.count())

print("\nQuantiles:")
print(salary.quantile([0.25, 0.50, 0.75]))


# ================================================================
# 16. CREATE / MODIFY COLUMNS
# ================================================================

section("16. CREATE / MODIFY COLUMNS")

work = employees.copy()

work["AnnualBonus"] = work["Salary"] * 0.10
print("\nCalculated column:")
print(work[["Name", "Salary", "AnnualBonus"]])

work["SalaryLevel"] = (
    work["Salary"] > 60000
).map({
    True: "High",
    False: "Standard"
})
print("\nConditional column:")
print(work[["Name", "Salary", "SalaryLevel"]])

work["Salary"] = work["Salary"] * 1.05
print("\nModified salary:")
print(work[["Name", "Salary"]])

work = work.drop(columns=["SalaryLevel"])
print("\nAfter dropping a column:")
print(work.columns.tolist())


# ================================================================
# 17. APPLY
# ================================================================

section("17. APPLY")

apply_demo = employees.copy()

apply_demo["SalaryWithBonus"] = apply_demo["Salary"].apply(
    lambda x: x * 1.10
)

print("\nSeries apply:")
print(apply_demo[["Name", "Salary", "SalaryWithBonus"]])


def classify_employee(row):
    if row["Salary"] >= 60000:
        return "High"
    return "Standard"


apply_demo["SalaryLevel"] = apply_demo.apply(
    classify_employee,
    axis=1
)

print("\nRow-wise apply:")
print(apply_demo[["Name", "Salary", "SalaryLevel"]])

print("\naxis=0 -> column-wise")
print("axis=1 -> row-wise")


# ================================================================
# 18. MAP
# ================================================================

section("18. MAP")

mapped = employees.copy()

mapped["Department"] = mapped["Department"].map({
    "IT": "Technology",
    "HR": "Human Resources",
    "Sales": "Sales"
})

print("\nDictionary mapping:")
print(mapped[["Name", "Department"]])

boolean_series = pd.Series([True, False, True, False])
print("\nBoolean mapping:")
print(boolean_series.map({
    True: "Yes",
    False: "No"
}))


# ================================================================
# 19. GROUPBY
# ================================================================

section("19. GROUPBY")

print("\nGroupBy object:")
print(employees.groupby("Department"))

print("\nSum:")
print(employees.groupby("Department")["Salary"].sum())

print("\nMean:")
print(employees.groupby("Department")["Salary"].mean())

print("\nMultiple statistics:")
print(
    employees.groupby("Department")["Salary"]
    .agg(["sum", "mean", "min", "max"])
)

print("\nMultiple grouping columns:")
print(
    employees.groupby(["Department", "City"])["Salary"].sum()
)

print("\nas_index=False:")
print(
    employees.groupby("Department", as_index=False)["Salary"].sum()
)


# ================================================================
# 20. AGGREGATION WITH NAMED OUTPUTS
# ================================================================

section("20. NAMED AGGREGATION")

employee_report = (
    employees
    .groupby("Department")
    .agg(
        TotalSalary=("Salary", "sum"),
        AverageSalary=("Salary", "mean"),
        EmployeeCount=("EmployeeID", "count"),
        MaximumSalary=("Salary", "max"),
        MinimumSalary=("Salary", "min")
    )
    .reset_index()
)

print(employee_report)


# ================================================================
# 21. MULTIPLE AGGREGATIONS
# ================================================================

section("21. MULTIPLE AGGREGATIONS")

sales_report = (
    sales
    .groupby("Category")
    .agg({
        "Revenue": ["sum", "mean", "max"],
        "Quantity": ["sum", "mean"]
    })
)

print(sales_report)


# ================================================================
# 22. MERGE / JOIN
# ================================================================

section("22. MERGE / JOIN")

departments = pd.DataFrame({
    "Department": ["IT", "HR", "Sales"],
    "Manager": ["Kumar", "Priya", "Arun"]
})

print("\nInner merge:")
print(pd.merge(employees, departments, on="Department", how="inner"))

print("\nLeft merge:")
print(pd.merge(employees, departments, on="Department", how="left"))

print("\nRight merge:")
print(pd.merge(employees, departments, on="Department", how="right"))

print("\nOuter merge:")
print(pd.merge(employees, departments, on="Department", how="outer"))

different_key = departments.rename(columns={"Department": "Dept"})
print("\nDifferent key names:")
print(pd.merge(
    employees,
    different_key,
    left_on="Department",
    right_on="Dept",
    how="left"
))

print("\nMerge using indicator:")
print(pd.merge(
    employees,
    departments,
    on="Department",
    how="outer",
    indicator=True
))


# ================================================================
# 23. CONCAT
# ================================================================

section("23. CONCAT")

part1 = employees.iloc[:3]
part2 = employees.iloc[3:]

print("\nVertical concat:")
print(pd.concat([part1, part2], axis=0, ignore_index=True))

print("\nHorizontal concat:")
small_left = employees[["EmployeeID", "Name"]].reset_index(drop=True)
small_right = employees[["Department", "Salary"]].reset_index(drop=True)
print(pd.concat([small_left, small_right], axis=1))


# ================================================================
# 24. PIVOT TABLE
# ================================================================

section("24. PIVOT TABLES")

print("\nBasic pivot:")
print(pd.pivot_table(
    sales,
    values="Revenue",
    index="Category",
    aggfunc="sum"
))

print("\nPivot with columns:")
sales_with_dept = sales.merge(
    employees[["EmployeeID", "Department"]],
    on="EmployeeID",
    how="left"
)

print(pd.pivot_table(
    sales_with_dept,
    values="Revenue",
    index="Department",
    columns="Category",
    aggfunc="sum",
    fill_value=0
))

print("\nMultiple aggregation functions:")
print(pd.pivot_table(
    sales_with_dept,
    values="Revenue",
    index="Department",
    aggfunc=["sum", "mean", "max"]
))

print("\nMultiple values:")
print(pd.pivot_table(
    sales_with_dept,
    values=["Revenue", "Quantity"],
    index="Department",
    aggfunc="sum"
))

print("\nGrand totals:")
print(pd.pivot_table(
    sales_with_dept,
    values="Revenue",
    index="Department",
    columns="Category",
    aggfunc="sum",
    fill_value=0,
    margins=True
))


# ================================================================
# 25. CROSSTAB
# ================================================================

section("25. CROSSTAB")

print("\nFrequency table:")
print(pd.crosstab(
    employees["Department"],
    employees["City"]
))

print("\nNormalize by row:")
print(pd.crosstab(
    employees["Department"],
    employees["City"],
    normalize="index"
))

print("\nNormalize by column:")
print(pd.crosstab(
    employees["Department"],
    employees["City"],
    normalize="columns"
))

print("\nNormalize overall:")
print(pd.crosstab(
    employees["Department"],
    employees["City"],
    normalize="all"
))


# ================================================================
# 26. DATETIME
# ================================================================

section("26. DATETIME OPERATIONS")

dates = pd.DataFrame({
    "Date": pd.to_datetime([
        "2025-01-05 10:30",
        "2025-02-15 14:45",
        "2025-03-20 09:15",
        "2025-04-25 18:00"
    ]),
    "Revenue": [10000, 15000, 12000, 18000]
})

dates["Year"] = dates["Date"].dt.year
dates["Month"] = dates["Date"].dt.month
dates["MonthName"] = dates["Date"].dt.month_name()
dates["Day"] = dates["Date"].dt.day
dates["DayName"] = dates["Date"].dt.day_name()
dates["Weekday"] = dates["Date"].dt.weekday
dates["Quarter"] = dates["Date"].dt.quarter
dates["Hour"] = dates["Date"].dt.hour
dates["Minute"] = dates["Date"].dt.minute

dates["MonthStart"] = (
    dates["Date"].dt.to_period("M").dt.start_time
)
dates["MonthEnd"] = (
    dates["Date"].dt.to_period("M").dt.end_time
)

print(dates)


# ================================================================
# 27. DATE FILTERING
# ================================================================

section("27. DATE FILTERING")

print("\nAfter date:")
print(dates[dates["Date"] >= "2025-02-01"])

print("\nBefore date:")
print(dates[dates["Date"] < "2025-04-01"])

print("\nBetween dates:")
print(dates[
    dates["Date"].between(
        "2025-02-01",
        "2025-03-31"
    )
])

print("\nSorted by date:")
print(dates.sort_values("Date"))


# ================================================================
# 28. RESAMPLING
# ================================================================

section("28. RESAMPLING")

time_series = dates.set_index("Date")

print("\nDaily:")
print(time_series["Revenue"].resample("D").sum())

print("\nWeekly:")
print(time_series["Revenue"].resample("W").sum())

print("\nMonthly:")
print(time_series["Revenue"].resample("ME").sum())

print("\nQuarterly:")
print(time_series["Revenue"].resample("QE").sum())

print("\nYearly:")
print(time_series["Revenue"].resample("YE").sum())

print("\nMonthly average:")
print(time_series["Revenue"].resample("ME").mean())


# ================================================================
# 29. ROLLING WINDOWS
# ================================================================

section("29. ROLLING WINDOWS")

rolling = pd.DataFrame({
    "Revenue": [100, 150, 120, 180, 200, 170, 220]
})

rolling["RollingMean"] = rolling["Revenue"].rolling(3).mean()
rolling["RollingSum"] = rolling["Revenue"].rolling(3).sum()
rolling["RollingMax"] = rolling["Revenue"].rolling(3).max()

print(rolling)


# ================================================================
# 30. CUMULATIVE OPERATIONS
# ================================================================

section("30. CUMULATIVE OPERATIONS")

cumulative = pd.DataFrame({
    "Revenue": [100, 150, 120, 180, 200]
})

cumulative["CumulativeSum"] = cumulative["Revenue"].cumsum()
cumulative["CumulativeMax"] = cumulative["Revenue"].cummax()
cumulative["CumulativeMin"] = cumulative["Revenue"].cummin()
cumulative["CumulativeProduct"] = cumulative["Revenue"].cumprod()

print(cumulative)


# ================================================================
# 31. DIFFERENCE / SHIFT / PERCENTAGE CHANGE
# ================================================================

section("31. DIFF / SHIFT / PCT_CHANGE")

changes = pd.DataFrame({
    "Revenue": [100, 150, 120, 180, 200]
})

changes["Difference"] = changes["Revenue"].diff()
changes["PreviousRevenue"] = changes["Revenue"].shift(1)
changes["NextRevenue"] = changes["Revenue"].shift(-1)
changes["Growth"] = changes["Revenue"].pct_change()
changes["GrowthPercent"] = changes["Revenue"].pct_change() * 100

print(changes)


# ================================================================
# 32. STRING OPERATIONS
# ================================================================

section("32. STRING OPERATIONS")

names = pd.DataFrame({
    "Name": [" Alice ", "BOB", "Charlie", "Diana", "Evan"],
    "Email": [
        "alice@example.com",
        "bob@example.com",
        "charlie@test.com",
        "diana@example.com",
        "evan@test.com"
    ]
})

names["Stripped"] = names["Name"].str.strip()
names["Lower"] = names["Name"].str.lower()
names["Upper"] = names["Name"].str.upper()
names["Title"] = names["Name"].str.title()
names["NameLength"] = names["Name"].str.len()

print(names)

print("\nContains 'a':")
print(names[names["Name"].str.contains("a", case=False, na=False)])

print("\nStarts with A:")
print(names[names["Name"].str.startswith("A", na=False)])

print("\nEnds with n:")
print(names[names["Name"].str.endswith("n", na=False)])

print("\nRegex match — starts with capital:")
print(names["Name"].str.match(r"^[A-Z]", na=False))

names["CleanName"] = names["Name"].str.replace(
    " ",
    "",
    regex=False
)

print("\nReplace:")
print(names[["Name", "CleanName"]])

print("\nSplit:")
print(names["Name"].str.split())

split_names = pd.DataFrame({
    "FullName": ["Alice Kumar", "Bob Raj", "Charlie Das"]
})
split_names[["FirstName", "LastName"]] = (
    split_names["FullName"]
    .str.split(" ", n=1, expand=True)
)
print(split_names)

names["EmailDomain"] = names["Email"].str.extract(r"@(.+)$")
print("\nEmail domain extraction:")
print(names[["Email", "EmailDomain"]])


# ================================================================
# 33. STRING CLEANING PIPELINE
# ================================================================

section("33. STRING CLEANING PIPELINE")

cleaning = pd.DataFrame({
    "Name": [" alice ", "BOB", " charlie ", "DIANA"]
})

cleaning["Name"] = (
    cleaning["Name"]
    .astype("string")
    .str.strip()
    .str.lower()
    .str.title()
)

print(cleaning)


# ================================================================
# 34. MEMORY USAGE
# ================================================================

section("34. MEMORY USAGE")

print("\nPer-column memory:")
print(employees.memory_usage())

print("\nDeep memory usage:")
print(employees.memory_usage(deep=True))

memory_bytes = employees.memory_usage(deep=True).sum()
memory_mb = memory_bytes / (1024 ** 2)

print("\nTotal bytes:", memory_bytes)
print("Total MB:", round(memory_mb, 4))


# ================================================================
# 35. MEMORY OPTIMIZATION
# ================================================================

section("35. MEMORY OPTIMIZATION")

optimized = employees.copy()

optimized["Department"] = optimized["Department"].astype("category")
optimized["Age"] = optimized["Age"].astype("int8")
optimized["EmployeeID"] = optimized["EmployeeID"].astype("int32")

print("Optimized dtypes:")
print(optimized.dtypes)

print("\nMemory before:")
print(round(employees.memory_usage(deep=True).sum() / (1024 ** 2), 4), "MB")

print("Memory after:")
print(round(optimized.memory_usage(deep=True).sum() / (1024 ** 2), 4), "MB")


# ================================================================
# 36. CHUNK PROCESSING
# ================================================================

section("36. CHUNK PROCESSING")

large_csv = StringIO()
sales.to_csv(large_csv, index=False)
large_csv.seek(0)

total_rows = 0
total_revenue = 0

for chunk in pd.read_csv(large_csv, chunksize=3):
    total_rows += len(chunk)
    total_revenue += chunk["Revenue"].sum()

print("Rows processed:", total_rows)
print("Revenue processed:", total_revenue)

# Chunk-level groupby
large_csv.seek(0)
results = []

for chunk in pd.read_csv(large_csv, chunksize=3):
    result = (
        chunk.groupby("Category")["Revenue"]
        .sum()
    )
    results.append(result)

combined = pd.concat(results)

final_result = (
    combined
    .groupby(level=0)
    .sum()
    .sort_values(ascending=False)
)

print("\nFinal chunk-level category revenue:")
print(final_result)


# ================================================================
# 37. CONDITIONAL COLUMNS
# ================================================================

section("37. CONDITIONAL COLUMNS")

conditions_demo = sales.copy()

conditions_demo["HighValue"] = (
    conditions_demo["Revenue"] > 100000
)

conditions = [
    conditions_demo["Revenue"] >= 100000,
    conditions_demo["Revenue"] >= 50000,
    conditions_demo["Revenue"] < 50000
]

choices = ["High", "Medium", "Low"]

conditions_demo["RevenueLevel"] = np.select(
    conditions,
    choices,
    default="Unknown"
)

print(conditions_demo[
    ["OrderID", "Revenue", "HighValue", "RevenueLevel"]
])


# ================================================================
# 38. REPLACE VALUES
# ================================================================

section("38. REPLACE VALUES")

replace_demo = employees.copy()

replace_demo["Department"] = replace_demo["Department"].replace(
    "IT",
    "Technology"
)

print("\nReplace one value:")
print(replace_demo[["Name", "Department"]])

replace_demo["Department"] = replace_demo["Department"].replace({
    "HR": "Human Resources",
    "Sales": "Sales & Marketing"
})

print("\nReplace multiple values:")
print(replace_demo[["Name", "Department"]])


# ================================================================
# 39. DROP ROWS / COLUMNS
# ================================================================

section("39. DROP ROWS / COLUMNS")

print("\nDrop row by index:")
print(employees.drop(index=0))

print("\nDrop multiple rows:")
print(employees.drop(index=[0, 1]))

print("\nDrop column:")
print(employees.drop(columns="Age").head())

print("\nDrop multiple columns:")
print(employees.drop(columns=["Age", "City"]).head())


# ================================================================
# 40. INSERT / REORDER COLUMNS
# ================================================================

section("40. INSERT / REORDER COLUMNS")

insert_demo = employees.copy()
insert_demo.insert(
    1,
    "EmployeeType",
    ["Full-Time"] * len(insert_demo)
)

print("\nInserted column:")
print(insert_demo.head())

reordered = insert_demo[
    [
        "EmployeeID",
        "Name",
        "EmployeeType",
        "Department",
        "City",
        "Age",
        "Salary",
        "JoinDate"
    ]
]

print("\nReordered columns:")
print(reordered.head())


# ================================================================
# 41. COPY
# ================================================================

section("41. COPY")

df_copy = employees.copy()

print("Original and copy are separate objects:")
print("Same object:", employees is df_copy)
print("Same values:")
print(employees.equals(df_copy))


# ================================================================
# 42. DATA VALIDATION
# ================================================================

section("42. DATA VALIDATION")

print("Duplicate EmployeeIDs:", employees["EmployeeID"].duplicated().sum())
print("Missing EmployeeIDs:", employees["EmployeeID"].isna().sum())

calculated_revenue = sales["Quantity"] * sales["Price"]

print(
    "Revenue calculation is correct:",
    sales["Revenue"].equals(calculated_revenue)
)


# ================================================================
# 43. FIND MAX / MIN ROWS
# ================================================================

section("43. FIND MAX / MIN ROWS")

max_index = sales["Revenue"].idxmax()
min_index = sales["Revenue"].idxmin()

print("\nHighest revenue row:")
print(sales.loc[max_index])

print("\nLowest revenue row:")
print(sales.loc[min_index])

print("\nTop 5 revenue rows:")
print(sales.nlargest(5, "Revenue"))


# ================================================================
# 44. RESET / RENAME AFTER GROUPBY
# ================================================================

section("44. GROUPBY → RESET INDEX → RENAME")

report = (
    employees
    .groupby("Department")["Salary"]
    .sum()
    .reset_index()
)

report.columns = [
    "Department",
    "TotalSalary"
]

print(report)


# ================================================================
# 45. COMMON END-TO-END PIPELINE
# ================================================================

section("45. COMMON PANDAS ANALYSIS PIPELINE")

pipeline_report = (
    sales[
        sales["Revenue"] > 20000
    ]
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

print("""
Typical Pandas workflow:

1. LOAD
2. INSPECT
3. CLEAN
4. TRANSFORM
5. FILTER
6. COMBINE
7. AGGREGATE
8. ANALYZE
9. EXPORT
""")

print("Example final report:")
print(pipeline_report)


# ================================================================
# 46. QUICK REFERENCE
# ================================================================

section("46. QUICK REFERENCE")

quick_reference = {
    "Load CSV": 'pd.read_csv("file.csv")',
    "Load Excel": 'pd.read_excel("file.xlsx")',
    "Inspect": "df.head(), df.info(), df.describe()",
    "Shape": "df.shape",
    "Columns": "df.columns",
    "Types": "df.dtypes",
    "Select column": 'df["Column"]',
    "Select rows": "df.loc[...] / df.iloc[...]",
    "Missing": "df.isna().sum()",
    "Duplicates": "df.duplicated().sum()",
    "Filter": 'df[df["Column"] > value]',
    "Sort": 'df.sort_values("Column")',
    "Unique": 'df["Column"].unique()',
    "Count unique": 'df["Column"].nunique()',
    "Statistics": 'df["Column"].mean() / sum() / min() / max()',
    "GroupBy": 'df.groupby("Column")["Value"].sum()',
    "Aggregation": 'df.groupby(...).agg(...)',
    "Merge": "pd.merge(df1, df2, ...)",
    "Concat": "pd.concat([df1, df2])",
    "Pivot": "pd.pivot_table(...)",
    "Crosstab": "pd.crosstab(...)",
    "Datetime": 'pd.to_datetime(df["Date"])',
    "Resample": 'df.resample("ME").sum()',
    "Rolling": 'df["Value"].rolling(7).mean()',
    "Shift": 'df["Value"].shift(1)',
    "Difference": 'df["Value"].diff()',
    "Growth": 'df["Value"].pct_change()',
    "Strings": 'df["Column"].str.strip()',
    "Memory": "df.memory_usage(deep=True)",
    "Chunks": 'pd.read_csv(..., chunksize=10000)',
    "Export CSV": 'df.to_csv("output.csv", index=False)',
    "Export Excel": 'df.to_excel("output.xlsx", index=False)',
}

for operation, syntax in quick_reference.items():
    print(f"{operation:<18} → {syntax}")


# ================================================================
# 47. REVISION CHECKLIST
# ================================================================

section("47. PANDAS REVISION CHECKLIST")

checklist = [
    "Create Series / DataFrame",
    "Read CSV",
    "Read Excel",
    "Write CSV / Excel",
    "Inspect data",
    "Select rows / columns",
    "loc / iloc",
    "Index management",
    "Rename columns",
    "Change data types",
    "Missing values",
    "Duplicates",
    "Filtering",
    "Sorting",
    "value_counts",
    "unique / nunique",
    "Statistics",
    "Calculated columns",
    "apply / map",
    "groupby",
    "agg",
    "merge / joins",
    "concat",
    "pivot_table",
    "crosstab",
    "Datetime",
    "Date filtering",
    "Resampling",
    "Rolling windows",
    "diff / shift / pct_change",
    "String operations",
    "Regex extraction",
    "Memory usage",
    "dtype optimization",
    "Chunk processing",
    "Conditional columns",
    "Replace values",
    "Data validation",
    "CSV / Excel export",
]

for i, item in enumerate(checklist, start=1):
    print(f"[ ] {i:02d}. {item}")


print("\n" + "=" * 72)
print("✅ PANDAS CHEAT SHEET COMPLETED SUCCESSFULLY")
print("=" * 72)
print("This file ran entirely from its built-in demo data.")
print("No external dataset was required.")
