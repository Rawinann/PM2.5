import pandas as pd
from pycaret.regression import *

data = pd.read_csv('cleaned_air4thai.csv')
data = data.dropna(subset=['PM25'])


s = setup(data, target='PM25', session_id=123)

best = compare_models()

# tuned = tune_model(best)

# evaluate_model(tuned)

plot_model(best, plot = 'residuals')