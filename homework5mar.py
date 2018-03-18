from plotly.offline import plot, iplot
import plotly.graph_objs as go
import quandl
import pandas as pd
import numpy as np 
import plotly.figure_factory as ff
import matplotlib as mpl
import plotly.plotly as py


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from my_plot import figure1
from my_plot import figure2
from my_plot import figure3
from my_plot import figure4
from my_plot import figure5

s_data = quandl.get("FRED/GDP", authtoken = "4me7eZ2kvgDBUN2hmtYB")

app=dash.Dash()

app.css.append_css({"external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

app.layout=html.Div([

	html.Div([html.H1(children='Homework 3', style={"color":"rgb(150, 20, 20)", "text-align":"center", "font-weight":"bold",})], className="row"),


#Radio Button

html.Div([
			
			html.Div([

			dcc.RadioItems(id="radio", options=[
            {"label": "Employee Churn", "value": figure1}],
            value="show"),

            dcc.RadioItems(id="radio", options=[
            {"label": "Startup RoadMap", "value": figure5}],
            value="show")

            ], className="three columns"),

			
			html.Div([
			dcc.Graph(id="Graph")],
			className="nine columns"),

			], className="row"),

#Dropdown menu

html.Div([
			html.Div([dcc.Dropdown(
				id = 'dropdown',
				options=[
	            {'label': 'Google', 'value': 'GOOGL'},
	            {'label': 'MasterCard', 'value': 'MA'},
	            {'label': 'Microsoft', 'value': 'MSFT'},
	            {'label': 'Nike', 'value': 'NKE'},
	            {'label': 'Procter & Gamble', 'value': 'PG'}
			],
				placeholder='Please, select a stock', multi=True),

				html.Button(id='submit',n_clicks=0, children='Submit'),
			],	className="two columns"),

			html.Div([
			dcc.Graph(id="Boxplot")],
			className="five columns"),

			html.Div([
			dcc.Graph(id="Table")],
			className="five columns"),

			], className="row"),


#slider
   


html.Div([
	html.Div([dcc.RangeSlider(id = 'option_in', min=0, max=len(s_data.index), value= [0, len(s_data.index)])],
	className= 'four columns'),

	html.Div([dcc.Graph(id='GDP')],
		className= 'eight columns'),
	], className= 'row',)


])

#Button

@app.callback(
    Output(component_id="Graph", component_property="figure"),
    [Input(component_id="radio", component_property="value")])
	
def update_graph(Input_value):
	figure=Input_value
	return figure

#Dropdown


@app.callback(
    Output(component_id='Boxplot', component_property='figure'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='dropdown', component_property='value')])

def update_graph(clicks, input_value1):
	quandl_inp1 = "WIKI/"+input_value1[0]
	quandl_inp2 = "WIKI/"+input_value1[1]
	
	stock_dat1 = quandl.get(quandl_inp1, authtoken = "4me7eZ2kvgDBUN2hmtYB")
	stock_dat2 = quandl.get(quandl_inp2, authtoken = "4me7eZ2kvgDBUN2hmtYB")
	
	x_value1 = stock_dat1.Open.pct_change()
	x_value2 = stock_dat2.Open.pct_change()
	
	trace1 = go.Box(x=x_value1, name=input_value1[0])
	trace2 = go.Box(x=x_value2, name=input_value1[1])
	
	layout_f3 = dict(title="<i>Distribution of Price changes</i> "+input_value1[0]+" and "+input_value1[1])
	data_f3 = [trace1,trace2]
	figure = dict(data=data_f3, layout=layout_f3)
	return figure

#Table

@app.callback(
    Output(component_id='Table', component_property='figure'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='dropdown', component_property='value')]
)

def update_table(clicks, input_value2):

	quandl_inp3 ="WIKI/"+input_value2[0]
	quandl_inp4 = "WIKI/"+input_value2[1]
	
	stock_dat3 = quandl.get(quandl_inp3, authtoken = "4me7eZ2kvgDBUN2hmtYB")
	stock_dat4 = quandl.get(quandl_inp4, authtoken = "4me7eZ2kvgDBUN2hmtYB")

	stock_dat3["%C"] = stock_dat3.Open.pct_change()
	stock_dat4["%C"] = stock_dat4.Open.pct_change()
	
	stock_d3=stock_dat3.iloc[1:5,-1:].round(3)
	stock_d4=stock_dat4.iloc[1:5,-1:].round(3)

	header= dict(values=[input_value2[0],input_value2[1]],
				align=["left", "center"],
				font=dict(color="white", size=12),
				fill=dict(color="#2980B9"),
				)


	cells = dict(values=[stock_d3.values, stock_d4.values],
             align=["left", "center"],
             fill=dict(color=["#D4AC0D", "#FBEEE6"]))

	trace_g4 = go.Table(header=header, cells=cells)

	data_g4 = [trace_g4]

	layout_g4=dict(width=500, height=300)

	g4=dict(data=data_g4, layout=layout_g4)

	return g4


#SLider


@app.callback(
    Output(component_id='GDP', component_property='figure'),
    [Input(component_id='option_in', component_property='value')]
)
def update_graph(Input_value):

	slide_ind = s_data.index[Input_value[0]: Input_value[1]]
	slide_val = s_data.Value[Input_value[0]: Input_value[1]]

	data = [go.Scatter(x= slide_ind, y=slide_val, fill='tozeroy')]
	layout = dict (title = 'US GDP')
	figure = dict (data=data, layout= layout)
	return figure




if __name__ == '__main__':
	app.run_server(debug=True)

