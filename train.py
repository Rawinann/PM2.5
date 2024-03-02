import pandas as pd
from pycaret.regression import *

# Load your cleaned data
data = pd.read_csv('cleaned_air4thai.csv')

# Check for missing values in the target column
missing_values = data['PM25'].isnull().sum()

if missing_values > 0:
    # If there are missing values, remove the respective rows
    data = data.dropna(subset=['PM25'])
    print(f"Removed {missing_values} rows with missing values in the target column 'PM25'.")

# Set up the PyCaret environment
s = setup(data, target='PM25', session_id=123)

# Continue with the rest of your PyCaret workflow
best_model = compare_models()
tuned_model = tune_model(best_model)
evaluate_model(tuned_model)
