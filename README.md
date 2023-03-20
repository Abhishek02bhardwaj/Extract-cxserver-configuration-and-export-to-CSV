# Extract-cxserver-configuration-and-export-to-CSV
This repository is my submission for the task #T331201 in which we were supposed to write a parser for a set of YAML files under  "config/" in the cxserver repository which determines which languages are supported by the service and create a single flat, in-memory structure with all of the supported pairs and export this data as a CSV of all pairs.
 <br>
 The python code I have written parses the YAML files in the cxserver repository and extracts the required information into a list of dictionaries, which can be easily exported as a CSV file.
 <br>
 **Please consider the mt-defaults.wikimedia.yaml file and what its effect might be on the supported translation pairs.**
 <br>
 Regarding the mt-defaults.wikimedia.yaml file, it sets the default translation engines to be used for each language pair if no other engine is specified in the configuration files. This file does not define the language pairs themselves, so it does not affect the supported translation pairs.
<h2>Libraries Utilised</h2>
1. PyYAML<br>
<h2>Integrated the functioning of mt-defaults.wikimedia.yaml</h2>
In the most recent commit I have integrated the functioning of "mt-default.wikimedia.yaml". This file contains the information about the preferred engines for a specific Source Langauge and Target Language pair. To use this file I first converted it into a CSV file named "mt-defaults.csv" with columns named "source language", "target language" and "preferred engine". Then using the "final_updated.py" I compared "mt-defaults.csv" and "supported_pairs.csv" and for the rows in which the value of source language, target language and the preferred engine (in mt-defaults.csv) & translation engine (in supported_pairs.csv) were same, I updated the value of "is preferred engine" to true which was otherwise set to False by default.
<h2>Usage Instruction</h2>
1. First clone the repository.<br>
2. Execute the "main.py".<br>
3. Run the test from test directory by executing "test.py".<br>
<h2>Test Instruction</h2>
Make sure that the main.py file that you wish to test is there in the test directory. In order to avoid any confusions you can delete the "mt-defaults.csv" and "supported_pairs.csv" since these two files are generated during the test by the execution of "main.py".<br>
The "test.py" runs the "main.py" for the test environment created in the test directory for which the expected output is already saved in "expected__supported_pairs.csv" and "expected_mt-defaults.csv". Then the files generated by "main.py" are compared with the expected files and if the outputs match the file will pass the test.
<h2>Final Output File</h2>
<a href = "https://github.com/Abhishek02bhardwaj/Extract-cxserver-configuration-and-export-to-CSV/blob/main/supported_pairs.csv">supported_pairs.csv</a>
