# 🐼 Pandas Learning by Projects

A hands-on collection of **Pandas mini projects** created to learn data manipulation, cleaning, analysis, time-series processing, text processing, large-dataset handling, and Excel automation through practical implementation.

Instead of learning Pandas through isolated syntax and theory, each topic is learned by building a small real-world project.

---

## 🎯 Goal

Build a strong practical foundation in **Pandas** that can be used for:

- Data Analysis
- Data Science
- Data Cleaning
- Feature Engineering
- Machine Learning
- Data Preprocessing
- Business Analytics

---

## 📚 Learning Approach

The repository follows a simple approach:

```text
One Topic
    ↓
One Practical Project
    ↓
Learn the Required Pandas Concepts
    ↓
Implement
    ↓
Analyze the Results
    ↓
Complete the Project
    ↓
Move to the Next Topic
```

The focus is on **learning by building** rather than memorizing Pandas functions individually.

---

# 🛠 Technologies

- Python 3.x
- Pandas
- Jupyter Notebook
- NumPy
- OpenPyXL

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
├── requirements.txt
└── README.md
```

---

# 📈 Project Progress

## 🟢 Pandas Series — 9/9 Complete

| # | Project | Main Concepts | Status |
|---|---|---|:---:|
| 01 | Student Marks Analyzer | DataFrames, Selection, Filtering, Statistics       | ✅ |
| 02 | Data Cleaning & Missing Values | Missing Values, Duplicates, Data Cleaning  | ✅ |
| 03 | Sales Data Analysis | Filtering, Sorting, GroupBy, Aggregation              | ✅ |
| 04 | Merge & Join | Merge, Joins, Combining DataFrames                           | ✅ |
| 05 | Pivot Tables & Crosstabs | Pivot Tables, Crosstabs, MultiIndex              | ✅ |
| 06 | Time Series Analysis | Datetime, Resampling, Rolling, Time Features         | ✅ |
| 07 | Customer Reviews Analysis | String Operations, Regex, Text Processing       | ✅ |
| 08 | Large Dataset Analysis | Chunking, Memory Optimization, Large CSVs          | ✅ |
| 09 | Excel Data Processing | Excel I/O, Multi-Sheet Reports, Automation          | ✅ |

---

# 📖 Projects

## 01 — Student Marks Analyzer

A basic student performance analysis project designed to learn the fundamentals of Pandas.

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
- Dashboard-style summaries

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

---

## 07 — Customer Reviews Analysis

A text-processing project using Pandas string operations to clean and analyze customer reviews.

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
- Email extraction
- Phone number cleaning
- Text validation
- Word counting
- Keyword analysis
- Sentiment classification
- `apply()`
- `value_counts()`

---

## 08 — Large Dataset Analysis

An e-commerce transaction analysis project designed to understand how Pandas can process datasets that are too large to comfortably load into memory at once.

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

---

## 09 — Excel Data Processing & Automation

An automated business reporting project using Excel workbooks containing multiple sheets.

### Concepts

- `read_excel()`
- `sheet_name`
- Reading multiple sheets
- `sheet_name=None`
- `ExcelFile()`
- `sheet_names`
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

Generated reports include:

```text
Executive Summary
Department Report
Employee Report
Product Report
City Report
Category Report
Sales Details
```

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
- Multiple DataFrames

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
- Basic text classification

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

---

# 📊 Repository Statistics

| Metric | Value |
|---|---:|
| Projects | **9** |
| Completed | **9** |
| Completion | **100%** |
| Primary Library | **Pandas** |
| Language | **Python** |
| Notebook Projects | **9** |
| Major Topics | **9** |

---

# 📦 Installation

Clone the repository and install the required dependencies.

```bash
git clone <your-repository-url>
cd pandas-learning-projects
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it.

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

Then open the project's:

```text
notebook.ipynb
```

Projects that contain Python scripts can also be executed directly:

```bash
python script.py
```

For example, the Excel automation project:

```bash
cd 09_Excel_Data_Processing
python excel_report_generator.py
```

---

# 📁 Dataset Organization

Datasets used throughout the projects are stored within their respective project directories or the common dataset directory.

The datasets are either:

- Real-world datasets
- Public datasets
- Realistic synthetic datasets created specifically for learning

The goal is to focus on the **Pandas workflow**, not merely dataset size or complexity.

---

# 🎯 Learning Outcomes

After completing these projects, I can practically work with Pandas for:

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

I also gained experience handling:

```text
CSV
Excel
Time Series
Text Data
Large Datasets
Business Reports
```

---

# 🚀 What's Next?

This repository is the **Pandas foundation** of a larger project-based AI and Data Science learning roadmap.

The next technologies/topics will build on the skills learned here.

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

---

# 🗺️ Overall Learning Philosophy

This repository follows a broader principle:

> **Learn by building, not by memorizing.**

For each technology:

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

# 🏆 Completion

## 🐼 Pandas Learning Series

```text
██████████████████████████████████ 100%
```

**9 / 9 Projects Completed**

---

# 📜 License

This repository is created for educational purposes and continuous learning.