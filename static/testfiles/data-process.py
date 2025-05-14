from datetime import datetime
import csv


input_file = 'datasets/metacritic.csv'
output_file = 'datasets/metacritic-time.csv'

datetime_column = 'releaseDate'
columns_to_keep = ['id','title','releaseDate','rating','genres','description','platforms','metascore','metascore_count','metascore_sentiment','userscore','userscore_count','platform_metascores','developer','publisher']

with open(input_file, newline='') as f:
    reader = csv.DictReader(f)
    data = list(reader)

cleaned_data = []
counter = 0

for row in data:
    date_str = row[datetime_column]
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        if date_obj.year >= 2020:
            row[datetime_column] = date_obj
            cleaned_data.append(row)
    except ValueError:
        counter += 1

cleaned_data.sort(key=lambda r: r[datetime_column])

with open(output_file, 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=columns_to_keep)
    writer.writeheader()
    for row in cleaned_data:
        row[datetime_column] = row[datetime_column].strftime("%Y-%m-%d")  # convert date back to string
        filtered_row = {}
        for key in columns_to_keep:
            filtered_row[key] = row.get(key, '')
        writer.writerow(filtered_row)

print("Dropped", counter, "rows with invalid or empty dates.")