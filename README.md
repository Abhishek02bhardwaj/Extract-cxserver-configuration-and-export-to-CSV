# Extract cxserver configuration and export to CSV

## Overview
This repository serves as a comprehensive tool for extracting language pairs supported by the cxserver service and exporting them to a CSV file. The extraction process involves parsing YAML files within the `config/` directory of the cxserver repository. The primary aim is to create an in-memory structure with information on supported language pairs and export this data into a CSV file.

## Installation:
1. Clone the repository to your local machine.
2. Execute main.py to extract information from the YAML files and generate the CSV files.
3. To run tests, execute test.py after deleting `mt-defaults.csv` and `supported_pairs.csv` to ensure accurate testing.

## Project Structure:
* `config/`: Contains YAML files with configuration information.
* `test/`: Directory for testing purposes.
* `main.py`: Main Python script for parsing YAML files, extracting information, and exporting to CSV.
* `test.py`: Python script for testing the functionality of main.py.
* `supported_pairs.csv`: Output CSV file containing information on supported language pairs.
* `mt-defaults.csv`: Output CSV file containing information from the "mt-defaults.wikimedia.yaml" file.
* `LICENSE.md`: MIT License file.
* `README.md`: Project documentation.

## Libraries Utilised:
1. PyYAML: Used for parsing YAML files.
2. CSV: Python's built-in library for handling CSV operations.

## Explanation of mt-defaults.wikimedia.yaml:
The `mt-defaults.wikimedia.yaml` file sets the default translation engines for each language pair. However, it does not define the language pairs themselves. Its role is to specify the preferred engines to be used if no other engine is specified in the configuration files. This file does not directly affect the supported translation pairs but influences the default engines used.

## Changes in the Latest Commit:
The most recent commit integrates the functioning of `mt-defaults.wikimedia.yaml`. The file is converted into a CSV file named `mt-defaults.csv`, containing columns: "source language," "target language," and "preferred engine." The final_updated.py script compares `mt-defaults.csv` and `supported_pairs.csv` For matching rows, it updates the "is preferred engine" value to true, enhancing the accuracy of the supported pairs.

## License:
This project is licensed under the MIT License. Please refer to the LICENSE.md file for details.

Feel free to reach out if you have any questions or require further clarification.

**Happy coding!**
