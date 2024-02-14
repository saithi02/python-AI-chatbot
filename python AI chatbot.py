#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import nltk
from nltk.chat.util import Chat, reflections

# Define patterns and responses for the chatbot
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I am fine, thanks for asking.']),
    (r'what is your name?', ['My name is Chatbot.', 'You can call me Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'Bye!', 'Take care!']),
    # Add more patterns and responses as needed
]

# Create a chatbot with defined patterns
chatbot = Chat(patterns, reflections)

def main():
    prinet("Welcome to the Chatbot! Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()


# In[ ]:




