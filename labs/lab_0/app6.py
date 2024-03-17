import gradio as gr

def combine(a, b):
    return "Hey! " + a + " " + b + '\n'+ " Welcome to Machine Learning Nuggets."


with gr.Blocks() as demo:
    
    txt = gr.Textbox(label="First Name", lines=2)
    txt_2 = gr.Textbox(label="Second Name")
    txt_3 = gr.Textbox(value="", label="Output")
    btn = gr.Button(value="Submit")
    btn.click(combine, inputs=[txt, txt_2], outputs=[txt_3])


if __name__ == "__main__":
    demo.launch()