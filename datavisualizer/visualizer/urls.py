from django.urls import path
from .views import home, pie_graph, bar_graph, line_graph, update_pie_graph, update_bar_graph, update_line_graph

urlpatterns = [
    path('', home, name='home'),
    path('pie-chart', pie_graph, name='pie_graph'),
    path('bar-chart', bar_graph, name='bar_graph'),
    path('line-chart', line_graph, name='line_graph'),
    path('update_pie_graph/', update_pie_graph, name='update_pie_graph'),
    path('update_bar_graph/', update_bar_graph, name='update_bar_graph'),
    path('update_line_graph/', update_line_graph, name='update_line_graph'),
]
