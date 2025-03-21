import gradio as gr
from dotenv import load_dotenv
from chatbot_engine import chat
import os


def respond(message, chat_history):
    print(chat_history)

    chat_history = chat(message, chat_history)
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    load_dotenv()
    
    app_env = os.environ.get("APP_ENV", "production")
    
    if app_env == "production":
        username = os.environ["GRADIO_USERNAME"]
        password = os.environ["GRADIO_PASSWORD"]
        auth = (username, password)
    else:
        auth = None
    
    demo.launch(auth=auth)
