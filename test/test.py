import filecmp
import os
import csv
import yaml
import unittest


class Testsupportedpairs(unittest.TestCase):

    def test_generate_csv_files(self):
        # Generate the CSV files using the main code
        os.system("python main.py")

        # Read the expected CSV files
        with open("expected_supported_pairs.csv", "r") as f:
            expected_supported_pairs = list(csv.DictReader(f))

        with open("expected_mt-defaults.csv", "r") as f:
            expected_mt_defaults = list(csv.DictReader(f))

        # Read the generated CSV files
        with open("supported_pairs.csv", "r") as f:
            supported_pairs = list(csv.DictReader(f))

        with open("mt-defaults.csv", "r") as f:
            mt_defaults = list(csv.DictReader(f))

        # Check if the generated CSV files match the expected output
        self.assertTrue(supported_pairs == expected_supported_pairs)
        self.assertTrue(mt_defaults == expected_mt_defaults)


if __name__ == '__main__':
    unittest.main()