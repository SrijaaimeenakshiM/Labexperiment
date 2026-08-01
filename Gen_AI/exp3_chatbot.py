# Experiment 3: Conversational AI Chatbot Using Transformer-Based Language Models
from transformers import pipeline, Conversation

def main():
    print("--- Conversational AI Chatbot ---")
    # Initialize the conversational pipeline
    # We use Facebook's blenderbot as it is specifically designed for dialogue tasks
    chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")
    
    # Start a conversation
    user_input1 = "Hi, I'm trying to learn about Generative AI. Can you explain what it is?"
    print(f"User: {user_input1}")
    
    conversation = Conversation(user_input1)
    
    # Get response from the chatbot
    conversation = chatbot(conversation)
    print(f"Bot: {conversation.generated_responses[-1]}")
    
    # Continue the conversation to demonstrate context retention
    user_input2 = "That sounds interesting. What are some popular examples of it?"
    print(f"\nUser: {user_input2}")
    
    conversation.add_user_input(user_input2)
    conversation = chatbot(conversation)
    print(f"Bot: {conversation.generated_responses[-1]}")

if __name__ == "__main__":
    main()
