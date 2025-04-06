from django.shortcuts import render
from .utils import generate_bar_graph, generate_pie_graph, generate_line_graph
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import matplotlib.pyplot as plt

from django.http import JsonResponse

def home(request):
    # Generate the plot image as a Base64 string
    
    return render(request, 'visualizer/home.html')


def pie_graph(request):
    # Default data for the pie chart
    labels = ['JavaScript', 'Python', 'C#', 'Rust']
    sizes = [15, 13, 22, 2]
    headers = ['Fav Programming Lang']
    pie_chart_image = generate_pie_graph(labels, sizes, headers)

    return render(request, 'visualizer/pie_graph.html', {'plot_image': pie_chart_image})


@csrf_exempt
def update_pie_graph(request):
    if request.method == 'POST':
        # Get the new data from the request (labels and sizes)
        data = json.loads(request.body)
        labels = data['labels']
        sizes = data['sizes']
        headers = data['headers']
        pie_chart_image = generate_pie_graph(labels, sizes, headers)
        return JsonResponse({'plot_image': pie_chart_image})

    
# Function to generate the pie chart
def bar_graph(request):
    labels = ['Apples', 'Bananas', 'Oranges']
    values = [30, 50, 20]
    headers = ['Inventory Chart', 'Fruit', 'Count']
    bar_image = generate_bar_graph(labels, values, headers)
    return render(request, 'visualizer/bar_graph.html', {'plot_image': bar_image})


@csrf_exempt
def update_bar_graph(request):
    if request.method == 'POST':
        # Get the new data from the request (labels and sizes)
        data = json.loads(request.body)
        labels = data['labels']
        values = data['values']
        headers = data['headers']
        bar_image = generate_bar_graph(labels, values, headers)
        return JsonResponse({'plot_image': bar_image})


def line_graph(request):
    labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    values = [10, 20, 15, 25, 30]
    headers = ['Monthly Data', 'Months', 'Values']
    line_image = generate_line_graph(labels, values, headers)
    
    return render(request, 'visualizer/line_graph.html', {'plot_image': line_image})

@csrf_exempt
def update_line_graph(request):
    if request.method == 'POST':
        # Get the new data from the request (labels and sizes)
        data = json.loads(request.body)
        labels = data['labels']
        values = data['values']
        headers = data['headers']
        line_image = generate_line_graph(labels, values, headers)
        return JsonResponse({'plot_image': line_image})


