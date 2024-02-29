from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd


# Incorporate data
df = pd.read_csv('cleaned_air4thai.csv')

# Initialize the app
app = Dash(__name__)

# Check for existence of required columns (optional):
print(df.columns)  # Uncomment to check available column names

app.layout = html.Div([
    html.Div(children='My First App with Data'),
    dcc.Graph(figure=px.histogram(df, x='PM25', y='TEMP', histfunc='avg')),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True)