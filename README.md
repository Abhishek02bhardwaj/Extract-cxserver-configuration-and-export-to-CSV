# Extract-cxserver-configuration-and-export-to-CSV
This repository is my submission for the task #T331201 in which we were supposed to write a parser for a set of YAML files under  "config/" in the cxserver repository which determines which languages are supported by the service and create a single flat, in-memory structure with all of the supported pairs and export this data as a CSV of all pairs.
 <br>
 The python code I have written parses the YAML files in the cxserver repository and extracts the required information into a list of dictionaries, which can be easily exported as a CSV file.
 <br>
 **Please consider the mt-defaults.wikimedia.yaml file and what its effect might be on the supported translation pairs.**
 <br>
 Regarding the mt-defaults.wikimedia.yaml file, it sets the default translation engines to be used for each language pair if no other engine is specified in the configuration files. This file does not define the language pairs themselves, so it does not affect the supported translation pairs.
<h2>Libraries Utilised</h2>
1. yaml<br>
2. os<br>
3. csv<br>
