import gradio as gr
from dotenv import load_dotenv
from chatbot_engine import chat

def respond(message, chat_history):
    bot_message = chat(message)
    chat_history.append({"role": "user", "content": message})
    chat_history.append({"role": "assistant", "content": bot_message})
    return "", chat_history

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(type="messages")
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])



    msg.submit(respond, [msg, chatbot], [msg, chatbot])

if __name__ == "__main__":
    load_dotenv()
    demo.launch()
