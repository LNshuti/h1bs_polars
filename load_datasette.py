import sqlite3
import pandas as pd
from sklearn.impute import SimpleImputer
import os

# Define file paths
COUNTRY_ISO_CODES_PATH = 'data/country_iso_codes.csv'
TRK_FILE_PATH = 'data/TRK_13139_FY2021_2023.csv'
DB_FILE_PATH = 'data/datasette.db'

def remove_columns_with_missing_data(df, threshold=0.3):
    """Removes columns from a DataFrame if they are missing more than a certain percentage of their observations."""
    missing_data_ratio = df.isnull().sum() / len(df)
    columns_to_keep = missing_data_ratio[missing_data_ratio <= threshold].index
    return df[columns_to_keep]

def impute_missing_values(df):
    """Impute missing values in the DataFrame. Numeric columns are imputed with mean, 
    and non-numeric columns are imputed with the most frequent value."""
    # Separate numeric and non-numeric columns
    numeric_cols = df.select_dtypes(include=['number']).columns
    non_numeric_cols = df.select_dtypes(exclude=['number']).columns

    # Impute numeric columns with mean
    if len(numeric_cols) > 0:
        imputer_num = SimpleImputer(strategy='mean')
        df[numeric_cols] = imputer_num.fit_transform(df[numeric_cols])

    # Impute non-numeric columns with most frequent value
    if len(non_numeric_cols) > 0:
        imputer_cat = SimpleImputer(strategy='most_frequent')
        df[non_numeric_cols] = imputer_cat.fit_transform(df[non_numeric_cols])
    
    return df

def clean_column_names(df):
    """Clean column names by converting them to lowercase and replacing spaces with underscores."""
    return df.rename(columns=lambda x: str(x).lower().replace(' ', '_'))

def load_country_iso_codes_to_sqlite(csv_file_path, db_file_path):
    """Loads the country ISO codes CSV file into a SQLite database."""
    try:
        df = pd.read_csv(csv_file_path)
        
        # Clean column names using the new function
        df = clean_column_names(df)
        
        # Remove columns with more than 30% missing data
        df = remove_columns_with_missing_data(df, threshold=0.3)

        # Impute missing values
        df = impute_missing_values(df)

        with sqlite3.connect(db_file_path) as conn:
            df.to_sql('country_iso_codes', conn, if_exists='replace', index=False)
    except Exception as e:
        print(f"Error loading country ISO codes into SQLite: {e}")

def load_trk_data_to_sqlite(csv_file_path, db_file_path):
    """Loads the TRK CSV file into a SQLite database."""
    try:
        df = pd.read_csv(csv_file_path)
        
        # Clean column names using the new function
        df = clean_column_names(df)
        
        # Print initial data shape
        print(f"Initial data shape: {df.shape}")
        
        # Verify wage_amt column exists
        if 'wage_amt' not in df.columns:
            raise ValueError("wage_amt column not found in the dataset")
            
        # Remove columns with more than 10% missing data
        df = remove_columns_with_missing_data(df, threshold=0.99)
        print(f"Shape after removing sparse columns: {df.shape}")
        
        # Convert wage_amt to numeric, replacing non-numeric values with NaN
        df['wage_amt'] = pd.to_numeric(df['wage_amt'], errors='coerce')
        
        # Filter for wage_amt > 5000
        df = df[df['wage_amt'] > 5000]
        print(f"Shape after wage filtering: {df.shape}")
        
        # Print remaining columns
        print("Remaining columns:", list(df.columns))

        # Impute missing values
        df = impute_missing_values(df)

        with sqlite3.connect(db_file_path) as conn:
            df.to_sql('trk_data', conn, if_exists='replace', index=False)
            
        print(f"Successfully loaded {df.shape[0]} records into SQLite")
            
    except Exception as e:
        print(f"Error loading TRK data into SQLite: {str(e)}")
        raise

# Create the data directory if it doesn't exist
os.makedirs('data', exist_ok=True)

# Load the country ISO codes into SQLite
load_country_iso_codes_to_sqlite(COUNTRY_ISO_CODES_PATH, DB_FILE_PATH)

# Load the TRK CSV file into SQLite
load_trk_data_to_sqlite(TRK_FILE_PATH, DB_FILE_PATH)

print("Data has been successfully loaded into the SQLite database.")