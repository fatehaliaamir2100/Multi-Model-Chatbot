import gradio as gr
from utils import generate_response

# Define the available LLM models
llm_models = ["gpt-3.5-turbo", "gpt-4", "Llama-2-70b-chat", "Falcon-40b-instruct"]

with gr.Blocks() as demo:
    with gr.Row():
        # Add a dropdown for selecting the LLM model
        model_dropdown = gr.Dropdown(label="Select LLM Model", choices=llm_models, value=llm_models[0])
    
    chatbot = gr.Chatbot(label='CHATBOT', height=750)
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def wrapped_generate_response(message, chat_history, model_choice):
        # Pass the selected model choice to the generate_response function
        return generate_response(message, chat_history, model_choice)

    # Update the submit function to pass the model choice
    msg.submit(wrapped_generate_response, [msg, chatbot, model_dropdown], [msg, chatbot])

demo.launch()