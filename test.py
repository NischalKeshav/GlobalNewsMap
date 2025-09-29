import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
from datetime import datetime
import pandas as pd

df = px.data.gapminder().query("year == 2007")

# Create a choropleth map
fig = px.choropleth(
    df,
    locations="iso_alpha",        
    color="country",              
    hover_name="country",         
    scope="world",
    title="News around the World"
)

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Top Global News Dashboard", style = {'textAlign': 'center'}),
    html.P("Please click on a country in the map to get the top headlines for the last 24 hours in that country.", 
       style={'textAlign': 'center', 'fontSize': '20px'}),
    dcc.Graph(id='choropleth-map', figure=fig),
    html.Div(id='click-output', style={'padding': '20px', 'fontSize': '20px','background-color':'white'}),
    html.Footer("Made by Arjun, Nischal, Kanishk", style={'textAlign': 'center', 'marginTop': '50px', 'fontSize': '12px', 'color': 'black'}),
    html.Div(f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", style = {
        'textAlign': 'right',
        'fontSize': '10px',
        'color': 'black'
    })
])


@app.callback(
    Output('click-output', 'children'),
    Input('choropleth-map', 'clickData')
)
def display_click_data(clickData):
    if clickData and 'points' in clickData:
        point = clickData['points'][0]
        iso_code = point.get('location', 'N/A')  # ISO alpha-3 code
        country = point.get('hovertext', 'Unknown Country')  # Country name from hover
        return html.Div (id ='country clicked' ,children=f"You clicked on: {country} (ISO: {iso_code})")
    else:
        return "Click on a region to see its data."

# Run the app

app.run(debug=True)