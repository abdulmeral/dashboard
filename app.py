import dash
import dash_core_components as dcc
import dash_html_components as html    
from dash.dependencies import Input,Output
import pandas as pd
import plotly.offline   as pyo 
import plotly.graph_objs as go 
import plotly.figure_factory as ff # dist bunun içinde

# https://dash.plotly.com/deployment
# .\venv\Scripts\activate
data = pd.read_csv("mpg.csv")

def generate_table(dataframe, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
# items: Dropdown-1
items_1 = []
for item_1 in data.columns:
    items_1.append({"label":item_1,"value":item_1})

# items: Dropdownv-2
items_2 = []
for item_2 in data.columns:
    items_2.append({"label":item_2,"value":item_2})

dropdown_1 = dcc.Dropdown(id="my-drop-1",options=items_1,value=item_1)
dropdown_2 = dcc.Dropdown(id="my-drop-2",options=items_2,value=item_2)

#test_2
data_test_2 = [go.Scatter(x=data["horsepower"], y=data["mpg"],
                   text=data["name"],
                   mode="markers",
                   marker=dict(size=2*data["cylinders"],
                               color=data["cylinders"],
                               showscale=True)# yandaki renk barı
                   )]
 
layout_test_2 = go.Layout(title="Horse Power & MPG & Clinders",
                          plot_bgcolor="#F5FFFA",
                          paper_bgcolor="#F5FFFA",
                          font=dict(color="black"),    
                          xaxis=dict(title="Horse Power"),
                          yaxis=dict(title="MPG"),
                          hovermode="closest")#hovermode:üstüne gelince eksen bilgilerini görstriyor.
#
#test_3
data_test_3 = [go.Box(y=data.mpg,name=data.columns[0]),
                go.Box(y=data.cylinders,name=data.columns[1]),
                go.Box(y=data.cylinders,name=data.columns[2]),
                go.Box(y=data.cylinders,name=data.columns[3]),
                go.Box(y=data.cylinders,name=data.columns[4]),
                go.Box(y=data.cylinders,name=data.columns[5]),
                go.Box(y=data.cylinders,name=data.columns[6])]
layout_test_3 = go.Layout(title="Box Plots of Features",
                          plot_bgcolor="#F5FFFA",
                          paper_bgcolor="#F5FFFA",                          
                          hovermode="closest")#hovermode:üstüne gelince eksen bilgilerini görstriyor.
#
#test_5
data_test_5 = [go.Histogram(x=data.mpg,
                         xbins=dict(start=0,end=50))]

layout_test_5 = go.Layout(title="MPG",
                          plot_bgcolor="#F5FFFA",
                          paper_bgcolor="#F5FFFA",
                          font=dict(color="black"),    
                          hovermode="closest")#hovermode:üstüne gelince eksen bilgilerini görstriyor.
#test_4

data_test_4 = pd.read_csv("avocado.csv")

data_con_test_4 = data_test_4[data_test_4.type == "conventional"]
data_org_test_4 = data_test_4[data_test_4.type == "organic"]

hist_data = [data_con_test_4.AveragePrice,data_org_test_4.AveragePrice]
group_labels = ["Con Average Price","Org Average Price"]

#fig = ff.create_distplot(hist_data,group_labels) 
layout_test_4 = go.Layout(title="Average Price",
                          plot_bgcolor="#F5FFFA",
                          paper_bgcolor="#F5FFFA",
                          font=dict(color="black"),
                          hovermode="closest")#hovermode:üstüne gelince eksen bilgilerini görstriyor.

#
# dashboard:
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([ 
    html.Div([
        html.H4("By Abdül MERAL",style=dict(fontSize=15,textAlign="right",color="#A9A9A9")),
        html.H1('Plotly Dashboard',style=dict(fontSize=60,textAlign="left",color="#A9A9A9")),
        html.Hr(style=dict(color="white"))
        ]),
    
                       
    #input-1:
    html.H1('Mileage Per Gallon Performances of Various Cars',style=dict(fontSize=50,textAlign="center",color="#A9A9A9")),
    html.Div([html.H3('Select a Feature:',style=dict(fontSize=27,paddingRight="30px",color="#A9A9A9")),
        dropdown_1],style=dict(width="48%",display="inline-block",paddingBottom="20px")),
    #input-2:
    html.Div([html.H3('Select a Feature:',style=dict(fontSize=27,paddingRight="30px",color="#A9A9A9")),
        dropdown_2],style=dict(width="48%",float="right",display="inline-block",paddingBottom="20px")),
    #graphs:
    dcc.Graph(id="my-graph",style=dict(paddingBottom="30px")),
    html.Hr(style=dict(color="white")),
    
    html.Div([
        html.H1('Bubble Plot',style=dict(fontSize=50,textAlign="left",color="#A9A9A9")),
        dcc.Graph(id="test_2",style=dict(paddingBottom="30px"),
             figure=dict(data=data_test_2,layout=layout_test_2)),
        html.Hr(style=dict(color="white"))
        ],style=dict(paddingTop="50px")),
    
    html.Div([
        html.H1('Box Plot',style=dict(fontSize=50,textAlign="left",color="#A9A9A9")),
        dcc.Graph(id="test_3",style=dict(paddingBottom="30px"),
             figure=dict(data=data_test_3,layout=layout_test_3)),
        html.Hr(style=dict(color="white"))
        ],style=dict(paddingTop="50px")),
    
    html.Div([
        html.H1('Histogram',style=dict(fontSize=50,textAlign="left",color="#A9A9A9")),
        dcc.Graph(id="test_5",style=dict(paddingBottom="30px"),
             figure=dict(data=data_test_5,layout=layout_test_5)),
        html.Hr(style=dict(color="white"))
        ],style=dict(paddingTop="50px")),
    
    html.Div([
        html.H1('Distribution Plot',style=dict(fontSize=50,textAlign="left",color="#A9A9A9")),
        html.H3("Compare Avocado Prices",style=dict(textAlign="left",color="#A9A9A9")),
        dcc.Graph(id="test_4",style=dict(paddingBottom="30px"),
             figure=ff.create_distplot(hist_data,group_labels)),
        html.Hr(style=dict(color="white"))
        ],style=dict(paddingTop="50px"))

    ],style=dict(backgroundColor="#404040",padding=100))# output

@app.callback(Output(component_id="my-graph", component_property="figure"),
              [Input(component_id="my-drop-1", component_property="value"),
               Input(component_id="my-drop-2", component_property="value")])
# 1 1 e, 2 2 ye
def update_graph(selected_column_1,selected_column_2):
    
    trace = [go.Scatter( x = data[selected_column_1],
                         y = data[selected_column_2],
                         text = data["name"],
                         mode = 'markers',
                         marker=dict(
                                    size=7,
                                    color="blue",
                                    opacity=0.7,
                                    symbol="circle",
                                    line=dict(width=2) #çevre çizgileri
                                    ))]
    
    layout = go.Layout(title="My Dashboard for MPG",
                   plot_bgcolor="#F5FFFA",
                   paper_bgcolor="#F5FFFA",
                   font=dict(color="black"),    
                   xaxis=dict(title=selected_column_1),
                   yaxis=dict(title=selected_column_2),
                   #margin=dict(l=40,b=40,t=10,r=0),#'l':   40,   'b':   40,   't':   10,   'r':   0}, 
                   hovermode="closest")                                     
        
    return dict(data=trace,layout=layout)

if __name__ == "__main__":
    app.run_server()