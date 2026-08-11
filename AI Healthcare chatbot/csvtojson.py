import csv
import json

# Specify the CSV input file and JSON output file
csv_file = 'transformed_data.csv'
json_file = 'csvtojson.json'

# Read data from CSV and convert it to a list of dictionaries
data = []
with open(csv_file, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        data.append(row)

# Write data to JSON file
with open(json_file, 'w') as json_file:
    json.dump(data, json_file, indent=4)

print(f'CSV file "{csv_file}" has been converted to JSON file "{json_file}"')
