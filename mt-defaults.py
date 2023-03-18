import yaml
import csv

# Load YAML file
with open('config/mt-defaults.wikimedia.yaml') as file:
    data = yaml.load(file, Loader=yaml.FullLoader)

# Write CSV file
with open('mt-defaults.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["source language", "target language", "translation engine"])
    for key, value in data.items():
        if len(key.split("-")) == 2:
            source, target = key.split("-")
            writer.writerow([source, target, value])
