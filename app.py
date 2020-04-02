import dash
import dash_core_components as dcc
import dash_html_components as html    
from dash.dependencies import Input,Output
import pandas as pd
import plotly.offline   as pyo 
import plotly.graph_objs as go 

data = pd.read_csv("mpg.csv")

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

# dashboard:
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([ #input-1:
                       html.H1('Mileage Per Gallon Performances of Various Cars',style=dict(fontSize=57,textAlign="center",color="blue")),
                       html.Div([html.H3('Select a Feature:',style=dict(fontSize=27,paddingRight="30px")),
                           dropdown_1],style=dict(width="48%",display="inline-block",paddingUp="30px")),
                       #input-2:
                       html.Div([html.H3('Select a Feature:',style=dict(fontSize=27,paddingRight="30px")),
                           dropdown_2],style=dict(width="48%",float="right",display="inline-block",paddingUp="30px")),
                       #graph:
                       dcc.Graph(id="my-graph")],style=dict(padding=10))# output

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
                                    size=10,
                                    color="blue",
                                    opacity=0.5,
                                    symbol="circle",
                                    line=dict(width=2) #çevre çizgileri
                                    ))]
    
    layout = go.Layout(title="My Dashboard for MPG",
                   xaxis=dict(title=selected_column_1),
                   yaxis=dict(title=selected_column_2),
                   #margin=dict(l=40,b=40,t=10,r=0),#'l':   40,   'b':   40,   't':   10,   'r':   0}, 
                   hovermode="closest")                                     
        
    return dict(data=trace,layout=layout)

if __name__ == "__main__":
    app.run_server()