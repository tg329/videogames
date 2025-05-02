import pandas as pd

# Load the CSV and parse the date column
df = pd.read_csv('metacritic.csv', parse_dates=['releaseDate'])  # Replace 'date' with the actual column name

# Filter out rows before a certain year
year_threshold = 2020
df = df[df['releaseDate'].dt.year >= year_threshold]

# Save the result
df.to_csv('filtered_file.csv', index=False)
