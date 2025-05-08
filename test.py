import gradio as gr
gr.Interface(
    lambda x: f"You entered: {x}",
    inputs="text",
    outputs="text"
).launch()