from plotly.offline import plot, iplot
import plotly.graph_objs as go
import quandl
import pandas as pd
import numpy as np 
import plotly.figure_factory as ff
import matplotlib as mpl
import plotly.plotly as py
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

#1
x_values_1 = [17, 50,  17, 20]
x_values_2 = [-15, -50, -5, -37]
y_values_1 = ['X1', 'X2', 'X3', 'X4']
y_values_2=['X5', 'X6', 'X7', 'X8']

trace_1_1 = go.Bar(x=x_values_1, y=y_values_1, orientation='h', name="<b>Positive</b>", 
              marker = dict(
        color = 'rgba(153, 153, 255, 0.5)',
            line=dict(
                color='rgb(102, 102, 255)',
                width=1.3))
              )

trace_1_2 = go.Bar(x=x_values_2, y=y_values_2, orientation='h', name="<b>Negative</b>", 
              marker = dict(
        color = 'rgba(255, 204, 153, 0.5)',
            line=dict(
                color='rgb(255, 102, 102)',
                width=1.3))
              )

layout1 = dict(title="<b>Correlation with employees probability of churn</b>",
                 yaxis=dict(title="Variable"))



data1 = [trace_1_1, trace_1_2]
figure1 = dict(data=data1, layout=layout1)
iplot(figure1)

#2

data_1 = quandl.get("FRED/GDP", authtoken = "4me7eZ2kvgDBUN2hmtYB")

x_values2 = pd.to_datetime(data_1.index.values)
y_values2 = data_1.Value

trace2 = go.Scatter(x=x_values2, y=y_values2,
                      mode="lines", fill= "tozeroy")

layout2 = dict(title="<b>US GDP over time</b>",
              )

data2 = [trace2]
figure2 = dict(data=data2, layout=layout2)
iplot(figure2)

#3

data_2 = quandl.get("WIKI/GOOGL", authtoken = "4me7eZ2kvgDBUN2hmtYB")
data_3 = quandl.get("BCHARTS/ABUCOINSUSD", authtoken = "4me7eZ2kvgDBUN2hmtYB")

x_values3_1 = data_2.Open.pct_change()
x_values3_2 = data_3.Open.pct_change()

trace3_1 = go.Box(x=x_values3_2, name="<b>Bitcoin</b>")
trace3_2 = go.Box(x=x_values3_1, name="<b>Google</b>")


layout3 = dict(title="Distribution of Price changes")

data3 = [trace3_1,trace3_2]
figure3 = dict(data=data3, layout=layout3)
iplot(figure3)

#4
header = dict(values=['Google', 'Bitcoin'],
            align = ["left", "center"],
            font = dict(color="white", size=12),
            fill = dict(color='rgb(0, 128, 255)'),
             )
             
data_2["%C"]=data_2.Open.pct_change()
data_3["%C"]=data_3.Open.pct_change()


data_2_1=data_2.iloc[1:5, -1].round(3)
data_3_1=data_3.iloc[1:5, -1].round(3)

data_2_2=data_2_1.values
data_3_2=data_3_1.values


cells = dict(values=[data_2_2,data_3_2],
             align=["left", "center"],
             fill=dict(color=["yellow", "white"])
            )

trace4 = go.Table(header=header, cells=cells)

data4 = [trace4]
layout4=dict(width=500, height=300)
figure4=dict(data=data4, layout=layout4)
iplot(figure4)

#5

import plotly.figure_factory as ff

trace5=[dict(Task="Task 1", Start="2018-01-01", Finish="2018-01-31", Resource='Idea Validation'),
          dict(Task="Task 2", Start="2018-03-01", Finish="2018-04-15", Resource='Prototyping'),
          dict(Task="Task 3", Start="2018-04-15", Finish="2018-09-30", Resource='Team Formation')]

figure5=ff.create_gantt(trace5, index_col='Resource', title="Startup Roadmap", show_colorbar=True)

iplot(figure5)
