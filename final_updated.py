import csv

# Read in the supported_pairs.csv file
with open("supported_pairs.csv", "r") as f:
    reader = csv.DictReader(f)
    supported_pairs = [row for row in reader]

# Read in the mt-defaults.csv file and build a dictionary for O(1) lookups
with open("mt-defaults.csv", "r") as f:
    reader = csv.DictReader(f)
    mt_defaults = {}
    for row in reader:
        key = (row["source language"], row["target language"], row["translation engine"])
        mt_defaults[key] = row

# Loop over each pair in the supported_pairs list
for pair in supported_pairs:
    # Look up the matching pair in the mt_defaults dictionary
    key = (pair["source language"], pair["target language"], pair["translation engine"])
    match = mt_defaults.get(key)
    # If a match is found, update the "is preferred engine?" flag to True
    if match:
        pair["is preferred engine?"] = "True"

# Write the updated supported_pairs list back to the CSV file
with open("supported_pairs.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["source language", "target language", "translation engine", "is preferred engine?"])
    writer.writeheader()
    writer.writerows(supported_pairs)
