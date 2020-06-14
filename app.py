## Bootstrap Grid tutorial - adding style to the app

# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import joblib
import pickle
import pandas as pd
import numpy as np
#
test_model_data = pd.read_csv('https://raw.githubusercontent.com/popkdodge/Unit-2-Build/master/Test_Car.csv',index_col=[0])

external_stylesheets = ['https://codepen.io/amyoshino/pen/jzXypZ.css']
# Boostrap CSS.
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    html.Div([
        html.Div(
            [
                html.H1(
                        children='Porsche 911 Carrera',
                        className='nine columns offset-by-four',
                        style={
                        'height': '15%',
                        'width': '30%',
                        'float': 'center',
                        'position': 'center',
                        'margin-top': 30,
                        'text-align': 'center',
                        'background-color': 'white',
                        'font-size': '500%' ,
                        'top-padding': 40
                        },
                        ),    
                html.Img(
                    src="https://di-uploads-pod3.dealerinspire.com/porscheoffremont/uploads/2018/09/porsche-logo.jpg",
                    className='three columns',
                    style={
                        'height': '50%',
                        'width': '20%',
                        'float': 'right',
                        'position': 'right',
                        'margin-top': 10,
                    },
                ),
            ], className="row",
            style={
                'background-color':'white',
            }
            
        ),
        html.Div(
            [
                html.Hr()
            ], className="row",
        ),
        html.Div(
            [
                dcc.Input(
                    id="Milage",
                    type='number',
                    placeholder="Milage",
                    className='one columns offset-by-one',
                    value=30000   
                ),
                dcc.Dropdown(
                    id='condition',
                    placeholder='CPO/Used',
                    options=[
                    {'label': 'Used', 'value': 'Used'},
                    {'label': 'CPO', 'value': 'CPO'},
                            ],
                    className='one columns offset-by-one',
                    value="Used",
                            ), 
                dcc.Dropdown(
                    id='Year',
                    placeholder='Year',
                    options=[
                    {'label': '2012', 'value': 2012},
                    {'label': '2013', 'value': 2013},
                    {'label': '2014', 'value': 2014},
                    {'label': '2015', 'value': 2015},
                    {'label': '2016', 'value': 2016},
                    {'label': '2017', 'value': 2017},
                    {'label': '2018', 'value': 2018},
                    {'label': '2019', 'value': 2019},
                            ],value='2013',
                    className='one columns offset-by-one'
                            ),
                dcc.Dropdown(
                    id='Color',
                    placeholder='Color',
                    options=[
                    {'label': 'Black', 'value': 'Black'},
                    {'label': 'White', 'value': 'White'},
                    {'label': 'Gray', 'value': 'Gray'},
                    {'label': 'Silver', 'value': 'Silver'},
                    {'label': 'Blue', 'value': 'Blue'},
                    {'label': 'Red', 'value': 'Red'},
                    {'label': 'Other', 'value': 'Other'},
                            ],
                    className='one columns offset-by-one',
                    value='Black',
                            ),
                dcc.Dropdown(
                    id='Transmission',
                    placeholder='Transmission',
                    options=[
                    {'label': 'Automatic', 'value': 'Black'},
                    {'label': 'White', 'value': 'White'},
                            ],
                    className='one columns offset-by-one',
                    value='Automatic'
                            ),
                dcc.Dropdown(
                    id='Cabriolet',
                    placeholder='Cabriolet?',
                    options=[
                    {'label': 'Cabriolet', 'value': 'Cabriolet'},
                    {'label': 'Hardtop', 'value': 'Hardtop'},
                            ],
                    value='Cabriolet',
                    className='one columns offset-by-one'
                ),
            ], className="row",
        ),
        html.Div(
            [
                html.Hr()
            ], className="row",
        ),
        html.Div(
            [
                html.Div(id='result')
            ], className="row",
        ),        
    ])
)
@app.callback(
    Output(component_id='result', component_property='children'),
    [Input (component_id='Milage', component_property='value')])
def update_milage_input(Milage):
    if Milage is not None and Milage is not '':
        try:
            price = model.predict([test_model_data])
            return price
        except ValueError:
            return 'Something went wrong.'        

if __name__ == '__main__':
    model = joblib.load('911.pkl')
    app.run_server(debug=True)