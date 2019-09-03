from flask import Flask, send_from_directory, jsonify, render_template, abort, redirect, request
import plotly, json, os
import plotly.graph_objects as go
import chart_studio.plotly as py
import numpy as np
import pandas as pd
from werkzeug.utils import secure_filename
import matplotlib.pyplot as plt

app=Flask(__name__)
app.config['UPLOAD_FOLDER']='./static/upload'

@app.route('/')
def home():
    return render_template('uploadcsv.html')

@app.route('/plotly', methods=['POST'])
def plotly1():
    request.method == 'POST'
    myFile = request.files['file']
    fn = secure_filename(myFile.filename)
    myFile.save(os.path.join(app.config['UPLOAD_FOLDER'],fn))
    df = pd.read_csv(os.path.join(app.config['UPLOAD_FOLDER'],fn))
    x = list(df['x'])
    y = list(df['y'])
    plot = go.Scatter(x=x,y=y)
    plot=[plot]
    plotJson = json.dumps(plot, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('visual.html', x = plotJson)

@app.route('/matplotlib', methods=['POST'])
def matplotlib():
    request.method == 'POST'
    myFile = request.files['file']
    fn = secure_filename(myFile.filename)
    # myFile.save(os.path.join(app.config['UPLOAD_FOLDER'],fn))
    df = pd.read_csv(fn)
    x = list(df['x'])
    y = list(df['y'])
    plt.plot(x,y, linestyle='-',marker='o', color='red')
    plt.title('Matplotlib Grafik Plotting', fontdict={'fontsize':30})
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.savefig('./static/upload/inigrafikku.png')
    return render_template('visual2.html')
        


if __name__ == '__main__':
    app.run(debug=True)