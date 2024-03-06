from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd


# Incorporate data
df = pd.read_csv('cleaned_air4thai.csv')

# def generate_table(dataframe, max_rows=10):
#     return html.Table([
#         html.Thead(
#             html.Tr([html.Th(col) for col in dataframe.columns])
#         ),
#         html.Tbody([
#             html.Tr([
#                 html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#             ]) for i in range(min(len(dataframe), max_rows))
#         ])
#     ])

# # Initialize the app
# app = Dash(__name__)

# # Check for existence of required columns (optional):
# # print(df.columns)  # Uncomment to check available column names

# app.layout = html.Div([
#     html.Div(children='My Data', style={'textAlign': 'center'}),
#     dcc.Graph(figure=px.histogram(df, x='PM25', y='TEMP', histfunc='avg')),
#     dash_table.DataTable(data=df.to_dict('records'), page_size=10),
#     generate_table(df)
    
# ])


def generate_table(dataframe, max_rows=10):
    return dash_table.DataTable(
        columns=[{'name': col, 'id': col} for col in dataframe.columns],
        data=dataframe.to_dict('records'),
        page_size=max_rows
    )

# Initialize the app
app = Dash(__name__)

# Check for existence of required columns (optional):
# print(df.columns)  # Uncomment to check available column names

app.layout = html.Div([
    html.Div(children='My Data', style={'textAlign': 'center'}),
    dcc.Graph(figure=px.histogram(df, x='PM25', y='TEMP', histfunc='avg')),
    generate_table(df)
])


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
