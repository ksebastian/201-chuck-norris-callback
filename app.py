######### Import your libraries #######
import dash
#import dash_core_components as dcc
#import dash_html_components as html
import os
from dash import html
from dash import dcc

###### Set up variables
list_of_choices=['Art Blakey', 'Horace Silver', 'Donald Byrd', 'Sonny Rollins']
image_list=['art_blakey.jpeg', 'horace_silver.jpeg', 'donald_byrd.jpeg', 'sonny_rollins.jpeg']
githublink = 'https://github.com/ksebastian/chuck_norris_execution'
image1='blue_note_logo.jpeg'
heading1='Classic Blue Note Jazz Records'

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='Jazz'

####### Layout of the app ########
app.layout = html.Div([
    html.H2(heading1),
    html.Img(id='show-image', src=app.get_asset_url('blue_note_logo.jpeg')),  #, style={'width': 'auto', 'height': '10%'}),
    dcc.Dropdown(id='your-input-here',
                options=[{'label': i, 'value': i} for i in list_of_choices],
                value='punch',
                style={'width': '500px'}),
    html.Br(),
    html.Div(id='your-output-here', children=''),
    html.Br(),
    html.A('Code on Github', href=githublink),

])


######### Interactive callbacks go here #########
@app.callback(dash.dependencies.Output('your-output-here', 'children'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return f'Lets listen to something from {whatever_you_chose}.'


@app.callback(dash.dependencies.Output('show-image', 'src'),
              [dash.dependencies.Input('your-input-here', 'value')])
def display_value(whatever_you_chose):
    return app.get_asset_url(image_list[whatever_you_chose])


######### Run the app #########
if __name__ == '__main__':
    app.run_server(debug=True)
