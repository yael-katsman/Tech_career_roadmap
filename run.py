import argparse
import pandas as pd
import papermill as pm

# Set up argument parser
parser = argparse.ArgumentParser(description='Process a user CSV with a Jupyter Notebook.')
parser.add_argument('csv_file', type=str, help='Path to the CSV file containing user data.')
parser.add_argument('notebook_path', type=str, help='Path to the Jupyter Notebook to be executed.')

# Parse arguments from the command line
args = parser.parse_args()

# Read the CSV file specified by the user
df = pd.read_csv(args.csv_file)

# Loop through each row in the dataframe (assuming each row represents a user)
for index, row in df.iterrows():
    # Extract the user information from the current row
    user_data = row['user_column_name']  # Replace 'user_column_name' with the actual column name

    # Execute the notebook with the current user's data
    pm.execute_notebook(
       args.notebook_path,
       '/dev/null',  # Or use f'output_{index}.ipynb' to save each execution's output
       parameters=dict(user=user_data)
    )
