import plotly.express as px
import pandas as pd
import gradio as gr

def plotly_plot():
    # prepare some data
    x = ["Math", "Business", "Statistics", "IT", "Commerce"]
    y = [68, 73, 82, 74, 85]
    data = pd.DataFrame()
    data['Subject'] = x
    data['Score'] = y
    # create a new plot
    p = px.bar(data, x='Subject', y='Score')

    return p

# show the results
outputs = gr.Plot()

demo = gr.Interface(fn=plotly_plot, inputs=None, outputs=outputs)

demo.launch()