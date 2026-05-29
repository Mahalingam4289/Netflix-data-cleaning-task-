# Netflix Dataset - Data Cleaning & Preprocessing

## 📌 Project Overview
This project focuses on cleaning and preprocessing the Netflix Titles dataset using Python and Pandas in PyCharm.

The objective of this task is to prepare raw data for analysis by handling missing values, removing duplicates, standardizing formats, and correcting data types.

---

# 🛠 Tools & Technologies
- Python
- Pandas
- PyCharm

---

# 📂 Dataset
Dataset Used:
- netflix_titles.csv

---

# ✅ Data Cleaning Tasks Performed

## 1. Handling Missing Values
- Identified null values using:
```python
df.isnull().sum()
```

- Filled missing categorical values with:
```python
fillna("Unknown")
```

---

## 2. Removing Duplicate Rows
Removed duplicate records using:
```python
df.drop_duplicates()
```

---

## 3. Standardizing Text Values
- Converted inconsistent text formats
- Removed extra spaces
- Standardized categorical values

Example:
```text
movie → Movie
tv-ma → TV-MA
```

---

## 4. Date Formatting
Converted date formats into:
```text
dd-mm-yyyy
```

Using:
```python
pd.to_datetime()
```

---

## 5. Renaming Column Headers
Cleaned column names by:
- Converting to lowercase
- Replacing spaces with underscores

Example:
```text
Release Year → release_year
```

---

## 6. Fixing Data Types
Corrected datatype inconsistencies:
- `release_year` → Integer
- `date_added` → Datetime

---

# 📊 Output Files
- Cleaned Dataset:
  - `netflix_titles_cleaned.csv`

- Python Script:
  - `task1_data_cleaning.py`

- Summary Report:
  - `data_cleaning_summary.txt`

---

# 💻 Sample Code

```python
import pandas as pd

df = pd.read_csv("netflix_titles.csv")

df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

df = df.drop_duplicates()
```

---

# 🚀 Project Outcome
Successfully cleaned and preprocessed the Netflix dataset for further data analysis and visualization tasks.

This project improved practical skills in:
- Data preprocessing
- Data quality handling
- Pandas operations
- Real-world dataset preparation

---
