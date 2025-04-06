import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import matplotlib.pyplot as plt
import io
import urllib
import base64

def generate_bar_graph(labels, values, headers):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title(headers[0])
    ax.set_xlabel(headers[1])
    ax.set_ylabel(headers[2])

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_data = base64.b64encode(buf.read()).decode('utf-8')
    plt.close(fig)
    return img_data

def generate_pie_graph(labels, sizes, headers):
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.set_title(headers[0])
    ax.axis('equal')  

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    
    img_data = base64.b64encode(buf.read()).decode('utf-8')
    return img_data

def generate_line_graph(labels, values, headers):
    fig, ax = plt.subplots()

    ax.plot(labels, values, marker='o')  
    ax.set_title(headers[0])
    ax.set_xlabel(headers[1])
    ax.set_ylabel(headers[2])

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    image_base64 = base64.b64encode(buf.getvalue()).decode('utf8')
    plt.close(fig)  
    return image_base64

