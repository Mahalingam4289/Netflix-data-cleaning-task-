import pandas as pd

# -----------------------------
# STEP 1: LOAD DATASET
# -----------------------------
df = pd.read_csv("netflix_titles.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Dataset shape
print("\nDataset Shape:", df.shape)

# -----------------------------
# STEP 2: CHECK MISSING VALUES
# -----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# STEP 3: RENAME COLUMN HEADERS
# -----------------------------
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(" ", "_")

print("\nUpdated Column Names:")
print(df.columns)

# -----------------------------
# STEP 4: REMOVE DUPLICATES
# -----------------------------
duplicate_count = df.duplicated().sum()

print("\nDuplicate Rows:", duplicate_count)

df = df.drop_duplicates()

# -----------------------------
# STEP 5: HANDLE MISSING VALUES
# -----------------------------

# Fill categorical columns with 'Unknown'
df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")

# Fill date_added with most frequent value
most_common_date = df["date_added"].mode()[0]
df["date_added"] = df["date_added"].fillna(most_common_date)

# -----------------------------
# STEP 6: STANDARDIZE TEXT
# -----------------------------
df["type"] = df["type"].str.title()
df["country"] = df["country"].str.title()
df["rating"] = df["rating"].str.upper()

# Remove extra spaces
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# -----------------------------
# STEP 7: CONVERT DATE FORMAT
# -----------------------------
df["date_added"] = pd.to_datetime(df["date_added"])

# Convert to dd-mm-yyyy format
df["date_added"] = df["date_added"].dt.strftime("%d-%m-%Y")

# -----------------------------
# STEP 8: CHECK DATA TYPES
# -----------------------------
print("\nData Types:")
print(df.dtypes)

# Convert release_year to integer
df["release_year"] = df["release_year"].astype(int)

# -----------------------------
# STEP 9: SAVE CLEANED DATASET
# -----------------------------
df.to_csv("netflix_titles_cleaned.csv", index=False)

print("\nData Cleaning Completed Successfully!")
print("Cleaned dataset saved as netflix_titles_cleaned.csv")