# 🐼 Pandas Learning by Projects

A hands-on collection of **Pandas projects** designed to learn data manipulation, cleaning, analysis, time-series processing, text processing, large-dataset handling, Excel automation, and real-world data analysis through practical implementation.

Instead of learning Pandas through isolated syntax and theory, each topic is learned by **building projects and applying the concepts to real or realistic datasets**.

---

# 🎯 Goal

Build a strong practical foundation in **Pandas** that can be used for:

- Data Analysis
- Data Science
- Data Cleaning
- Feature Engineering
- Machine Learning
- Data Preprocessing
- Business Analytics

The ultimate goal is to become comfortable taking raw data and performing a complete:

```text
Load
 ↓
Inspect
 ↓
Clean
 ↓
Transform
 ↓
Combine
 ↓
Analyze
 ↓
Report
 ↓
Export
```

workflow using Pandas.

---

# 📚 Learning Approach

This repository follows a simple approach:

```text
One Topic
    ↓
One Practical Project
    ↓
Learn Required Concepts
    ↓
Implement
    ↓
Analyze Results
    ↓
Complete Project
    ↓
Move to Next Topic
```

The focus is on:

> **Learn by building, not by memorizing.**

After completing the project series, the complete Pandas workflow is revised again through a larger real-world dataset.

---

# 🛠 Technologies

- Python 3.x
- Pandas
- NumPy
- Jupyter Notebook
- OpenPyXL
- Kaggle / Public Datasets

---

# 📂 Repository Structure

```text
pandas-learning-projects/
│
├── 01_Student_Marks_Analyzer/
│
├── 02_Data_Cleaning/
│
├── 03_Sales_Data_Analysis/
│
├── 04_Merge_and_Join/
│
├── 05_Pivot_Tables/
│
├── 06_Time_Series/
│
├── 07_String_Operations/
│
├── 08_Large_Dataset_Analysis/
│
├── 09_Excel_Data_Processing/
│
├── 10_Final_Pandas_Analysis_Project/
│   ├── data/
│   ├── output/
│   ├── notebook.ipynb
│   └── README.md
│
├── pandas_cheatsheet.py
├── requirements.txt
└── README.md
```

---

# 📈 Project Progress

## 🟢 Pandas Series — 10/10 Complete

| # | Project | Main Concepts | Status |
|---|---|---|:---:|
| 01 | Student Marks Analyzer | DataFrames, Series, Selection, Filtering, Statistics | ✅ |
| 02 | Data Cleaning & Missing Values | Missing Values, Duplicates, Cleaning, Validation | ✅ |
| 03 | Sales Data Analysis | Filtering, Sorting, GroupBy, Aggregation | ✅ |
| 04 | Merge & Join | Merge, Joins, Combining DataFrames | ✅ |
| 05 | Pivot Tables & Crosstabs | Pivot Tables, Crosstabs, MultiIndex | ✅ |
| 06 | Time Series Analysis | Datetime, Resampling, Rolling, Time Features | ✅ |
| 07 | String Operations | String Processing, Regex, Text Cleaning | ✅ |
| 08 | Large Dataset Analysis | Chunking, Memory Optimization, Large CSVs | ✅ |
| 09 | Excel Data Processing | Excel I/O, Multi-Sheet Reports, Automation | ✅ |
| 10 | Final Pandas Analysis Project | Complete Pandas Workflow, Real Dataset, Business Analysis | ✅ |

---

# 📖 Projects

## 01 — Student Marks Analyzer

A beginner-friendly project designed to learn the fundamentals of Pandas using student performance data.

### Concepts

- Reading CSV files
- DataFrames
- Series
- Selecting rows and columns
- Filtering
- Sorting
- Creating new columns
- Statistical analysis
- GroupBy
- Exporting results

**Status:** ✅ Completed

---

## 02 — Data Cleaning & Missing Values

A practical employee dataset cleaning project involving messy and incomplete data.

### Concepts

- Detecting missing values
- `isna()`
- `isnull()`
- `fillna()`
- `dropna()`
- Duplicate detection
- `drop_duplicates()`
- Data type conversion
- String cleaning
- Data validation

**Status:** ✅ Completed

---

## 03 — Sales Data Analysis

A sales analytics project focused on extracting business insights from transaction data.

### Concepts

- Conditional filtering
- Multiple conditions
- `isin()`
- `between()`
- Sorting
- `nlargest()`
- `nsmallest()`
- Calculated columns
- Revenue analysis
- GroupBy
- Aggregation
- Business-oriented analysis

**Status:** ✅ Completed

---

## 04 — Merge & Join

A project focused on combining information from multiple DataFrames.

### Concepts

- `merge()`
- Inner Join
- Left Join
- Right Join
- Outer Join
- `left_on`
- `right_on`
- `suffixes`
- `indicator`
- Multiple DataFrame merging

**Status:** ✅ Completed

---

## 05 — Pivot Tables & Crosstabs

An employee performance analysis project using Pivot Tables and Crosstabs to create management-style reports.

### Concepts

- `pivot_table()`
- `values`
- `index`
- `columns`
- `aggfunc`
- `fill_value`
- `margins`
- Multiple aggregation functions
- Multiple values
- MultiIndex
- `crosstab()`
- Crosstab normalization
- Summary reports

**Status:** ✅ Completed

---

## 06 — Time Series Analysis

A sales trend analysis project focused on working with dates and time-based data.

### Concepts

- `pd.to_datetime()`
- Datetime columns
- `.dt` accessor
- Year / Month / Day extraction
- Day names
- Date filtering
- Date indexing
- `set_index()`
- `resample()`
- Daily / Weekly / Monthly analysis
- `rolling()`
- Moving averages
- `cumsum()`
- `diff()`
- `shift()`
- Lag features
- `pct_change()`
- Growth analysis

**Status:** ✅ Completed

---

## 07 — String Operations

A text-processing project focused on cleaning and analyzing text using Pandas.

### Concepts

- `str.strip()`
- `str.lower()`
- `str.upper()`
- `str.title()`
- `str.len()`
- `str.contains()`
- `str.startswith()`
- `str.endswith()`
- `str.match()`
- `str.replace()`
- `str.split()`
- `str.extract()`
- Regular expressions
- Text cleaning
- Keyword analysis
- `apply()`
- `value_counts()`

**Status:** ✅ Completed

---

## 08 — Large Dataset Analysis

An e-commerce transaction analysis project designed to understand how Pandas can process larger datasets efficiently.

### Concepts

- Large CSV processing
- `memory_usage()`
- `usecols`
- `dtype`
- Categorical data
- `category` dtype
- `query()`
- `chunksize`
- Chunk processing
- Incremental aggregation
- `pd.concat()`
- Memory optimization
- Large-scale GroupBy
- Top-N analysis
- Incremental calculations

### Processing Pattern

```text
Large CSV
    ↓
Read Chunk
    ↓
Process Chunk
    ↓
Store Result
    ↓
Read Next Chunk
    ↓
Process
    ↓
Combine Results
    ↓
Generate Final Report
```

**Status:** ✅ Completed

---

## 09 — Excel Data Processing & Automation

An automated business reporting project using Excel workbooks containing multiple sheets.

### Concepts

- `read_excel()`
- `sheet_name`
- Reading multiple sheets
- `sheet_name=None`
- `ExcelFile()`
- `usecols`
- `skiprows`
- `nrows`
- `na_values`
- Excel validation
- `to_excel()`
- `ExcelWriter`
- Multiple Excel worksheets
- Data merging
- GroupBy
- Aggregation
- Business reports
- Automated report generation
- Reusable Python functions
- Data validation pipeline

### Automated Workflow

```text
Excel Workbook
      ↓
Load Data
      ↓
Validate Data
      ↓
Merge Data
      ↓
Analyze
      ↓
Generate Reports
      ↓
Export Excel Workbook
```

### Generated Reports

```text
Executive Summary
Department Report
Employee Report
Product Report
City Report
Category Report
Sales Details
```

**Status:** ✅ Completed

---

# 10 — Final Pandas Analysis Project

The final project is a **large-scale Pandas revision project** using the **Brazilian Olist E-Commerce dataset**.

The purpose of this project is different from the previous mini projects.

Instead of learning one new Pandas topic, this project combines the concepts learned throughout the entire Pandas series and applies them to a real-world multi-table dataset.

### Dataset

The project uses multiple Olist datasets:

```text
olist_customers_dataset.csv
olist_geolocation_dataset.csv
olist_order_items_dataset.csv
olist_order_payments_dataset.csv
olist_order_reviews_dataset.csv
olist_orders_dataset.csv
olist_products_dataset.csv
olist_sellers_dataset.csv
product_category_name_translation.csv
```

### Concepts Revised

- Loading multiple CSV datasets
- Dataset inspection
- `shape`
- `columns`
- `dtypes`
- `info()`
- `describe()`
- Missing-value analysis
- Duplicate analysis
- Datetime conversion
- Key integrity analysis
- Filtering
- Sorting
- `value_counts()`
- `unique()`
- `nunique()`
- Calculated columns
- `groupby()`
- Aggregation
- `merge()`
- Multiple DataFrame joins
- Pivot tables
- Crosstabs
- String operations
- Datetime analysis
- Resampling
- Delivery-time analysis
- Business metrics
- CSV export
- Excel report generation

### Main Analytical Workflow

```text
Olist Raw Datasets
        ↓
Dataset Inspection
        ↓
Data Cleaning
        ↓
Missing Value Analysis
        ↓
Duplicate Analysis
        ↓
Datetime Conversion
        ↓
Key Integrity Checks
        ↓
Merge Multiple Tables
        ↓
Master Analytical Dataset
        ↓
Business Analysis
        ↓
Time-Series Analysis
        ↓
Category Analysis
        ↓
Seller Analysis
        ↓
Customer Analysis
        ↓
Pivot / Crosstab Analysis
        ↓
Final Reports
```

### Business Analysis Performed

- Order status analysis
- Payment analysis
- Revenue analysis
- Product analysis
- Customer state analysis
- Customer city analysis
- Category revenue analysis
- Seller performance analysis
- Monthly revenue analysis
- Monthly order analysis
- State × Category analysis
- Payment × Order Status analysis
- Delivery-time analysis
- Average order value
- Top categories
- Top sellers
- Top states
- Payment-type analysis
- Delivered-order percentage
- Cancelled-order percentage

### Final Outputs

```text
output/
│
├── category_sales.csv
├── seller_sales.csv
├── monthly_sales.csv
├── monthly_orders.csv
├── state_revenue.csv
└── olist_analysis_report.xlsx
```

**Status:** ✅ Completed

---

# 📖 Pandas Cheat Sheet

The repository also contains:

```text
pandas_cheatsheet.py
```

This is a **self-contained, runnable Pandas reference file**.

Unlike a syntax-only cheat sheet, it contains a small built-in demonstration dataset so the examples can be executed at any time without requiring an external dataset.

### The cheat sheet covers

- Series
- DataFrames
- CSV I/O
- Excel I/O
- Data inspection
- Selection
- `loc`
- `iloc`
- Indexing
- Renaming
- Data types
- Missing values
- Duplicates
- Filtering
- Sorting
- `value_counts()`
- Statistics
- Calculated columns
- `apply()`
- `map()`
- GroupBy
- Aggregation
- Merge / Join
- Concatenation
- Pivot Tables
- Crosstabs
- Datetime
- Date filtering
- Resampling
- Rolling windows
- Cumulative calculations
- `diff()`
- `shift()`
- `pct_change()`
- String operations
- Regex
- Memory usage
- Memory optimization
- Chunk processing
- Conditional columns
- Data validation
- CSV / Excel export

### Running the Cheat Sheet

```bash
python pandas_cheatsheet.py
```

The file is designed to run independently using its built-in demonstration data.

---

# 🧠 Pandas Skills Covered

## Data Loading

- CSV files
- Excel files
- Multiple Excel sheets
- Large CSV files
- Chunked data loading

## DataFrame Fundamentals

- DataFrames
- Series
- Rows
- Columns
- Indexing
- Selection
- Inspection
- Data types

## Data Cleaning

- Missing values
- Duplicate records
- Data type conversion
- String cleaning
- Data validation
- Inconsistent data

## Data Manipulation

- Filtering
- Sorting
- Conditional operations
- Creating columns
- Calculated columns
- `apply()`
- `map()`
- `replace()`

## Data Analysis

- Descriptive statistics
- GroupBy
- Aggregation
- Business metrics
- Top-N analysis

## Combining Data

- Merge
- Inner Join
- Left Join
- Right Join
- Outer Join
- Multiple DataFrame joins
- Concatenation

## Pivot Analysis

- Pivot Tables
- Crosstabs
- MultiIndex
- Multiple aggregations
- Grand totals
- Percentage analysis

## Time Series

- Datetime conversion
- Date extraction
- Date filtering
- Date indexing
- Resampling
- Rolling windows
- Moving averages
- Cumulative calculations
- Lag features
- Percentage change

## Text Processing

- String cleaning
- Searching
- Replacement
- Splitting
- Extraction
- Regex
- Keyword analysis
- Basic text processing

## Large Dataset Processing

- Memory measurement
- Data type optimization
- Categorical data
- Column selection
- Chunk processing
- Incremental aggregation

## Excel Automation

- Reading Excel
- Writing Excel
- Multiple worksheets
- Excel reporting
- Automated report generation
- Reusable analysis functions

---

# 📊 Repository Statistics

| Metric | Value |
|---|---:|
| Mini Projects | **9** |
| Final Project | **1** |
| Total Projects | **10** |
| Completed | **10** |
| Completion | **100%** |
| Primary Library | **Pandas** |
| Language | **Python** |
| Runnable Cheat Sheet | **1** |
| Major Project Areas | **10** |

---

# 📦 Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd pandas-learning-projects
```

Create a virtual environment:

```bash
python -m venv .venv
```

### Linux / Ubuntu

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ▶️ Running the Projects

Most projects contain a Jupyter Notebook.

Start Jupyter:

```bash
jupyter notebook
```

Then open:

```text
notebook.ipynb
```

Projects containing Python scripts can also be executed directly:

```bash
python script.py
```

The Pandas cheat sheet can be run directly:

```bash
python pandas_cheatsheet.py
```

---

# 📁 Dataset Organization

Datasets are stored within their respective project directories or common dataset locations.

The projects use:

- Real-world datasets
- Public datasets
- Realistic synthetic datasets created specifically for learning

The focus is on learning the **Pandas workflow**, not simply working with large datasets.

---

# 🎯 Learning Outcomes

After completing this repository, I can practically work with Pandas through the complete data-analysis workflow:

```text
Load Data
   ↓
Inspect Data
   ↓
Clean Data
   ↓
Transform Data
   ↓
Filter Data
   ↓
Combine Data
   ↓
Analyze Data
   ↓
Create Reports
   ↓
Export Results
```

I have also practiced working with:

```text
CSV
Excel
Multiple DataFrames
Time Series
Text Data
Large Datasets
Business Data
Real-World Multi-Table Data
```

---

# 🏆 Pandas Completion

```text
██████████████████████████████████ 100%
```

## 🐼 10 / 10 Projects Completed

```text
9 Mini Projects
        +
1 Final Large-Scale Project
        +
Runnable Pandas Cheat Sheet
        ↓
PANDAS COMPLETE ✅
```

---

# 🚀 What's Next?

Pandas is the first major data-processing foundation in the larger project-based AI and Data Science roadmap.

The next repository will focus on **NumPy**.

```text
Pandas
   ↓
NumPy
   ↓
Data Visualization
   ↓
Feature Engineering
   ↓
Exploratory Data Analysis
   ↓
Machine Learning
   ↓
Deep Learning
   ↓
Computer Vision
   ↓
NLP
   ↓
LLM Engineering
   ↓
MLOps
   ↓
End-to-End AI Systems
```

The same philosophy will continue:

```text
Learn Concept
      ↓
Build Mini Project
      ↓
Practice
      ↓
Complete Project
      ↓
Move Forward
```

---

# 🗺️ Overall Learning Philosophy

> **Learn by building, not by memorizing.**

For every technology:

```text
Concept
  ↓
Mini Project
  ↓
Implementation
  ↓
Experiment
  ↓
Understanding
  ↓
Next Concept
```

After completing a technology's project series, the technology can be studied separately in greater depth to fill remaining gaps.

---

# 🏁 Pandas Complete

The Pandas project series is now complete.

The next step is:

```text
🐼 Pandas
   ✅ COMPLETE

      ↓

🔢 NumPy
   🚀 NEXT
```

---

# 📜 License

This repository is created for educational purposes and continuous learning.