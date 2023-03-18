import os
import yaml
import csv


supported_pairs = []
# Loop through all the YAML files in the config directory
for filename in os.listdir("config"):
    if filename.endswith('.yaml') and filename not in ['MWPageLoader.yaml', 'languages.yaml', 'JsonDict.yaml',
                                                       'Dictd.yaml', 'mt-defaults.wikimedia.yaml']:
        with open(os.path.join("config", filename), "r") as f:
            config = yaml.safe_load(f)

            # Check if the YAML file has a "handler" key
            if "handler" in config:
                handler = config["handler"]
                if handler == "transform.js":
                    lst = config["languages"]
                    target_langs = []
                    source_lang = []
                    # Handle transform.js based configuration files
                    for j in lst:
                        source_lang.append(j)
                        target_lang = []
                        for k in lst:
                            if(j != k and not ((j == "simple" and k == "en") or (k == "simple" and j == "en"))):
                                target_lang.append(k)
                        target_langs.append(target_lang)
                    engine = filename[:-5]
                    preferred_engine = config.get("preferred_engine", False)
            else:
                # # Handle standard configuration files
                # Handle dictionary-based configuration files
                source_lang = list(config.keys())
                target_langs = []
                for j in source_lang:
                    target_langs.append(config[j])
                    engine = filename[:-5]
                    preferred_engine = config.get("preferred_engine", False)

            # Add the supported pairs to the list
            for k in range(len(source_lang)):
                for i in target_langs[k]:
                    supported_pairs.append({
                        "source language": source_lang[k],
                        "target language": i,
                        "translation engine": engine,
                        "is preferred engine?": preferred_engine
                    })

# Export the list as a CSV file
with open("supported_pairs.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["source language", "target language", "translation engine", "is preferred engine?"])
    writer.writeheader()
    writer.writerows(supported_pairs)