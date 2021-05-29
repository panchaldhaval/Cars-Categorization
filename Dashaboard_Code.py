# -*- coding: utf-8 -*-
"""
Created on Fri May 29 15:34:21 2021

@author: Dhaval Panchal
"""

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input, State
import plotly.express as px 
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv(r"C:\Users\dhaval.panchal\Pictures\cars_categorization\Training_CSV_File/Training_Data.csv",encoding= 'unicode_escape')

df.columns = [column.replace(" ", "_") for column in df.columns]

df.query("climate_control == True", inplace = True)
climate_control = df["car_model"]

df.query("roof == True", inplace = True)
sunroof = df["car_model"]

df.query("petrol == True", inplace = True)
petrol = df["car_model"]

df.query("cng == True", inplace = True)
cng = df["car_model"]

df.query("diesel == True", inplace = True)
diesel = df["car_model"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='demo-dropdown',
        options=[
            {'label': 'petrol', 'value': '{}'.format(petrol)},
            {'label': 'cng', 'value': '{}'.format(cng)},
            {'label': 'diesel', 'value': '{}'.format(diesel)},
            {'label': 'sunroof', 'value': '{}'.format(sunroof)},
            {'label': 'climate_control', 'value': '{}'.format(climate_control)}
        ],
        value='{}'.format(petrol)
    ),
    html.Div(id='dd-output-container')
])

@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
    [dash.dependencies.Input('demo-dropdown', 'value')])
def update_output(value):
    return 'You have selected "{}"'.format(value)

if __name__ == '__main__':
    app.run_server(host='172.28.11.251',port='49766',debug=True, use_reloader=False) 
