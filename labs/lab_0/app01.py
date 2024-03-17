import gradio as gra
def user_greeting(name):
    return "Hi! " + name + " Welcome to your first Gradio application!😎"
    
#define gradio interface and other parameters
app =  gra.Interface(fn = user_greeting, inputs="text", outputs="text")
app.launch()