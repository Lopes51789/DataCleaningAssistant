from dash import Dash, html, dcc, Input, Output, State
import cleanData as cd
import json
import base64
import io
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Data Cleaning Assistant", style={'textAlign': 'center', 'margin': '20px'}),
    
    # File Upload Component
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        multiple=False
    ),
    
    # Display the name of uploaded file
    html.Div(id='output-data-upload'),
    
    # Container for buttons that appear after file upload
    html.Div(id='button-container', children=[
        html.Button('Check Data Types', id='check-types-button', n_clicks=0,
                   style={'display': 'none', 'margin': '10px'}),
        html.Button('Handle Missing Values', id='missing-values-button', n_clicks=0,
                   style={'display': 'none', 'margin': '10px'}),
        html.Button('Handle Duplicates', id='duplicates-button', n_clicks=0,
                   style={'display': 'none', 'margin': '10px'}),
        html.Button('Handle Outliers', id='outliers-button', n_clicks=0,
                   style={'display': 'none', 'margin': '10px'})
    ])
])

def parse_contents(contents, filename):
    df = cd.DataFrame(filename)
    return html.Div([
        html.H5(f'File uploaded: {filename}'),
        html.Hr()
    ])


@app.callback(
    [Output('output-data-upload', 'children'),
     Output('check-types-button', 'style'),
     Output('missing-values-button', 'style'),
     Output('duplicates-button', 'style'),
     Output('outliers-button', 'style')],
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def update_output(contents, filename):
    if contents is not None:
        children = parse_contents(contents, filename)
        button_style = {'margin': '10px', 'padding': '10px', 'display': 'inline-block'}
        return (children, button_style, button_style, button_style, button_style)
    
    button_style = {'display': 'none'}
    return (None, button_style, button_style, button_style, button_style)

if __name__ == "__main__":
    app.run_server(debug=True)
