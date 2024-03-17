import matplotlib.pyplot as plt
import gradio as gr

def plt_plot():
    # prepare some data
    x = ["Math", "Business", "Statistics", "IT", "Commerce"]
    y = [68, 73, 82, 74, 85]
    # create a new plot
    plt.rcParams['figure.figsize'] = 6,4
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    ax.bar(x, y)
    plt.title("Marks per subject")
    plt.xlabel("Subject")
    plt.ylabel("Score")

    return fig

# show the results
outputs = gr.Plot()

demo = gr.Interface(fn=plt_plot, inputs=None, outputs=outputs)

demo.launch()