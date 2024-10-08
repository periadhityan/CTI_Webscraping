import pandas as pd
import glob

# Define general column names
general_column_names = ["Date", "Domain", "Group"]
play_column_names = ["Date", "Domain", "Country", "Group"]

# Load the CSV files without headers
file_paths = glob.glob("./Activity_CSV_files/*.csv")  
dataframes = []

# Manually load each file with specific headers
for file_path in file_paths:
    if "PLAY" in file_path:
        # Load PLAY.csv with the extra column
        df = pd.read_csv(file_path, header=None, names=play_column_names)
    else:
        # Load the other files without extra column
        df = pd.read_csv(file_path, header=None, names=general_column_names)
        df['Country'] = 'N.A'  # Add a Country column with None to match PLAY format

    # Append each dataframe to the list
    dataframes.append(df)

# Concatenate all dataframes into one
combined_df = pd.concat(dataframes)

# Convert the 'Date' column to datetime
combined_df['Date'] = pd.to_datetime(combined_df['Date'], errors='coerce')

# Drop rows where date conversion failed
combined_df = combined_df.dropna(subset=['Date'])

# Save the combined data to a new CSV
combined_df.to_csv("./Activity_CSV_files/combined_ransomware_activity_data.csv", index=False)
