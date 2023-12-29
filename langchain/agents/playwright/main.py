import gradio as gr
from custom_lcel_agent import create_custom_agent

existing_agent = None

async def echo(message, history):
    global existing_agent
    if existing_agent is None:
        existing_agent = await create_custom_agent()
    response = await existing_agent.arun(message)    
    return response

demo = gr.ChatInterface(fn=echo, examples=["Retrieve landmarks", "List pictures", "Create sitemap"], title="Echo Bot")
demo.launch()