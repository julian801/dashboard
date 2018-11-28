from django.shortcuts import render
import numpy as np
import plotly
import plotly.plotly as py
import plotly.graph_objs as go


def main(request):
    return render(request, 'main.html',
                  context={'csv_url': '/static/clusters.csv'})

def plot1(request):
    return render(request, 'main.html',
                  context={'csv_url': '/static/clusters2.csv'})

def plot2(request):
    return render(request, 'collision.html')

def plot3(request):
    x = np.arange(1, 100)
    y = x ** 2
    marker_dict = {'size': 5, 'color': 'blue'}
    trace = go.Scatter(x=x, y=y, mode='markers', marker=marker_dict)
    fig = go.Figure(data=[trace])
    plot_html = plotly.offline.plot(fig, output_type='div', include_plotlyjs=True)

    return render(request, 'plotly.html',
                  context={'plot': plot_html})
