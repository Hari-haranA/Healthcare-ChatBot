import pandas as pd

# Load your dataset (replace 'your_dataset.csv' with your dataset's filename)
df = pd.read_csv('DiseasesWithSymptoms.csv')

# Step 1: Identify Missing Data
# Identify and count missing values in each column
missing_values = df.isnull().sum()

# Display columns with missing values and their respective counts
columns_with_missing_values = missing_values[missing_values > 0]
if not columns_with_missing_values.empty:
    print("Columns with missing values:")
    print(columns_with_missing_values)

# Ask the user if they want to remove rows with missing data
remove_missing_data = input("Do you want to remove rows with missing data? (yes/no): ").strip().lower()
if remove_missing_data == "yes":
    # Remove rows with missing values
    df.dropna(inplace=True)
    print("Rows with missing data have been removed.")
else:
    print("No rows with missing data were removed.")

# Step 2: Identify Duplicate Data
# Identify duplicate rows based on all columns
duplicate_rows = df[df.duplicated()]

# Display the number of duplicate rows
if not duplicate_rows.empty:
    print("Number of duplicate rows:", len(duplicate_rows))
    print("Sample duplicate rows:")
    print(duplicate_rows.head())

# Ask the user if they want to remove duplicate rows
remove_duplicates = input("Do you want to remove duplicate rows? (yes/no): ").strip().lower()
if remove_duplicates == "yes":
    # Remove duplicate rows
    df.drop_duplicates(inplace=True)
    print("Duplicate rows have been removed.")
else:
    print("No duplicate rows were removed.")

# Save the cleaned DataFrame to a new CSV file (optional)
df.to_csv('DatasetWithSymptomsCleaned.csv', index=False)
