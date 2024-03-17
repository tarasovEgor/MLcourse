import gradio as gr

def sentence_builder(quantity, morning, activity_list, watch):
    return f"""{quantity} o'clock is a nice time take a {"morning" if morning else "later in the day"}
      glass of water {" and take a ".join(activity_list)} or watch a {watch}"""

demo = gr.Interface(
    sentence_builder,
    [   gr.Slider(2, 24, value=4, step = 2),
        gr.Checkbox(label="Is it before noon"),
        gr.CheckboxGroup(["juice", "beverage", "snack", "nap"]),
        gr.Dropdown(["Television series", "Movie", "Documentary", "Class"]),
     
    ],
    "text")

if __name__ == "__main__":
    demo.launch()