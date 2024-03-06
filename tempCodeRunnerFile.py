        # html.Div(
        #     children=[
        #         html.Div(
        #             children=[
        #                 html.Div(children="Station ID", className="menu-title"),
        #                 dcc.Dropdown(
        #                     id="station-filter",
        #                     options=[
        #                         {"label": station, "value": station}
        #                         for station in np.sort(df['stationID'].unique())
        #                     ],
        #                     value="44t หาดใหญ่",
        #                     clearable=False,
        #                     className="dropdown",
        #                 ),
        #             ]
        #         ),
        #     ],
        #     className="menu",
        # ),