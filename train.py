import pandas as pd
from pycaret.regression import *

data = pd.read_csv('cleaned_air4thai.csv')

s = setup(data, target='PM25', session_id=123)

best_model = compare_models()

tuned_model = tune_model(best_model)

evaluate_model(tuned_model)

predictions = predict_model(tuned_model, data=new_data)
