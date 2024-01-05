# Import necessary libraries (OpenAI and Gradio)
import openai
import gradio as gr

# Set your OpenAI API key for authentication
openai.api_key = "insert open api key here" 

# Initialize a list to keep track of messages in the conversation
messages = [{"role": "system", "content": "You're an investment assistant with knowledge about all investments."}]

# Define a function that uses OpenAI Chat API to generate responses
def CustomChatGPT(user_input):
    # Add user's input to the conversation
    messages.append({"role": "user", "content": user_input})
    # Use OpenAI Chat API to create a response based on the conversation
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    # Get the assistant's reply from the API response
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    # Add assistant's reply to the conversation
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    # Return the assistant's reply
    return ChatGPT_reply

# Create a Gradio Interface for the chatbot
iface = gr.Interface(
    fn=CustomChatGPT,
    inputs="text",
    outputs="text",
    title="Investment Assistant",
    live=not True,  # Disable live updates for simplicity
    examples=[
        ["What are some low-risk investment options?"],
        ["How does diversification work in investment portfolios?"],  # Add another example question
    ],
)

# Launch the chatbot interface and make it shareable
iface.launch(share=True)
