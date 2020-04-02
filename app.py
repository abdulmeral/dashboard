import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd 
import   plotly.offline   as pyo 
import plotly.graph_objs as go 

df = pd.read_csv('OldFaithful.csv') 
#scatter plot:
data = [go.Scatter(x = df.X,
                   y = df.Y,
                   mode = 'markers',
                   marker=dict(
                           size=7,
                           color="rgb(17,77,117)",
                           symbol="pentagon",
                           line=dict(width=2) #çevre çizgileri
                           ))]  
                            
layout = go.Layout(title="Old Faithful",
                   xaxis=dict(title="Duration of Eruption"),
                   yaxis=dict(title="Next eruption"),
                   hovermode="x")

# dashboard:

app = dash.Dash(__name__)
server = app.server
colors = dict(background="#777777",text="#7FDBFF")
app.layout = html.Div(children=[
                                dcc.Graph(id="test_1",
                                          figure=dict(data=data,layout=layout))],
                                # "for big-div" / "for children"
                                style=dict(backgroundColor=colors["background"]))

if __name__ == "__main__":
    app.run_server()