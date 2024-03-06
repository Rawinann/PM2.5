from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import numpy as np
from dash.dependencies import Output, Input

# Incorporate data
df = pd.read_csv('predictions.csv')

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

def generate_table(dataframe, max_rows=20):
    return dash_table.DataTable(
        columns=[{'name': col, 'id': col} for col in dataframe.columns],
        data=dataframe.to_dict('records'),
        page_size=max_rows
    )

# Initialize the app
app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.title = "Air Quality Analytics: Understand Your Air Quality!"

app.layout = html.Div(
    children=[
        # ส่วน Header
        html.Div(
            children=[
                html.P(children="🌬️", className="header-emoji"),
                html.H1(
                    children="Air Quality Analytics", className="header-title"
                ),
                html.P(
                    children="Analyze the air quality data"
                    " with various parameters",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        
        # ส่วน Menu
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Station ID", className="menu-title"),
                        dcc.Dropdown(
                            id="station-filter",
                            options=[
                                {"label": station, "value": station}
                                for station in np.sort(df['stationID'].unique())
                            ],
                            value="44t หาดใหญ่",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
            ],
            className="menu",
        ),

        # ส่วน My Data
        html.Div([
            html.Div(children='My Data', style={'textAlign': 'center'}),
            dcc.Graph(figure=px.histogram(df, x='PM25', y='TEMP', histfunc='avg')),
            generate_table(df)
        ])
    ]
)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
