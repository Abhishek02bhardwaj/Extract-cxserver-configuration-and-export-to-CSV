import csv

# Read in the supported_pairs.csv file
with open("supported_pairs.csv", "r") as f:
    reader = csv.DictReader(f)
    supported_pairs = [row for row in reader]

# Read in the mt-defaults.csv file
with open("mt-defaults.csv", "r") as f:
    reader = csv.DictReader(f)
    mt_defaults = [row for row in reader]

# Loop over each pair in the supported_pairs list
for pair in supported_pairs:
    # Find the matching pair in the mt_defaults list
    match = next((p for p in mt_defaults if p["source language"] == pair["source language"] and p["target language"] == pair["target language"] and p["translation engine"] == pair["translation engine"]), None)
    # If a match is found, update the "is preferred engine?" flag to True
    if match:
        pair["is preferred engine?"] = "True"

# Write the updated supported_pairs list back to the CSV file
with open("supported_pairs.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["source language", "target language", "translation engine", "is preferred engine?"])
    writer.writeheader()
    writer.writerows(supported_pairs)
