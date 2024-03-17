import gradio as gr

def sentence_builder(morning, activity_list):
    return f"""It is a nice time take a {"morning" if morning else "later in the day"} glass of water 
    {" and take a ".join(activity_list)}"""

demo = gr.Interface(
    sentence_builder,
    [
        gr.Checkbox(label="Is it before noon"),
        gr.CheckboxGroup(["juice", "beverage", "snack", "nap"]),
    ],
    "text")

if __name__ == "__main__":
    demo.launch()