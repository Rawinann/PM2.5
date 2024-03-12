from dash import Dash, html, dash_table, dcc
import plotly.express as px
import pandas as pd
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import numpy as np

# Incorporate data
df = pd.read_csv('PM2.5/data/Daily_predict.csv')

external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
        "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

def generate_table(dataframe, max_rows=30):
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
                        html.Div(children="predict-selector", className="menu-title"),
                        dcc.Dropdown(
                            id="file-selector",
                            options=[
                                {'label': 'Daily Predict', 'value': 'daily'},
                                {'label': 'Hourly Predict', 'value': 'hourly'},
                            ],
                            value='daily', 
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
            html.Div(children='Data in HatYai', style={'textAlign': 'center', 'font-weight': 'bold', 'font-size': '24px'}),
            
            # เพิ่มปุ่มเลือกกราฟ
            html.Div([
                dcc.RadioItems(
                    id='graph-selector',
                    options=[
                        {'label': 'Scatter Plot', 'value': 'scatter'},
                        {'label': 'Bar Chart', 'value': 'bar'},
                        # เพิ่มตัวเลือกกราฟเพิ่มเติมตามต้องการ
                    ],
                    value='scatter',  # ตั้งค่าค่าเริ่มต้น
                    labelStyle={'display': 'block'}
                ),
            ]),
            
            # ให้กราฟแสดงตามที่ผู้ใช้เลือก
            dcc.Graph(id='selected-graph'),
            
            # แสดงตาราง
            generate_table(df)
        ]) 
    ])

# เพิ่ม callback function สำหรับอัปเดตกราฟ
@app.callback(
    Output('selected-graph', 'figure'),
    [Input('graph-selector', 'value'),
     Input('file-selector', 'value')]
)
def update_graph(selected_graph, selected_file):
    if selected_file == 'daily':
        df = pd.read_csv('PM2.5/data/Daily_predict.csv')
    else:
        df = pd.read_csv('PM2.5/data/Hourly_predict.csv')
        
    if selected_graph == 'scatter':
        # สร้าง Scatter Plot
        fig = px.scatter(df, x='DATETIMEDATA', y='prediction_label', color='prediction_label')
        fig.update_layout(
            title='Scatter Plot of Temperature over Time',
            xaxis_title='Date and Time',
            yaxis_title='Temperature',
            legend_title='Prediction Label'
        )
    # เพิ่มกราฟเพิ่มเติมตามต้องการ
    elif selected_graph == 'bar':
        # สร้าง Bar Chart
        fig = px.bar(df, x='DATETIMEDATA', y='prediction_label', color='prediction_label')
        fig.update_layout(
            title='Bar Chart of Temperature over Time',
            xaxis_title='Date and Time',
            yaxis_title='Temperature',
            legend_title='Prediction Label'
        )
    # เพิ่มกราฟเพิ่มเติมตามต้องการ
    else:
        # กรณีที่ไม่ตรงกับทางเลือกที่กำหนดไว้
        fig = px.scatter(df, x='DATETIMEDATA', y='prediction_label', color='prediction_label')
        fig.update_layout(
            title='Scatter Plot of Temperature over Time',
            xaxis_title='Date and Time',
            yaxis_title='Temperature',
            legend_title='Prediction Label'
        )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
