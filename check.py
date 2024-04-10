# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import sys

def print_csv(filename):
    try:
        # Read the CSV file
        df = pd.read_csv(filename)
        # Print the DataFrame
        print(df)
    except FileNotFoundError:
        print(f"File {filename} not found.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_csv(sys.argv[1])
    else:
        print("Please provide a CSV file path.")

