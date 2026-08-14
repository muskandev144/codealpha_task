def chatbot():
    print("=" * 50)
    print("WELCOME TO CHATBOT!")
    print("=" * 50)
    print("Type your message (type 'bye' to exit)\n")
    
    while True:
        user_input = input("You: ").lower().strip()
        
        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi there! How can I help you?")
        
        elif user_input == "how are you":
            print("Bot: I'm doing great, thanks for asking!")
        
        elif user_input == "what is your name":
            print("Bot: I'm a simple chatbot created for CodeAlpha.")
        
        elif user_input == "help":
            print("Bot: I can chat with you. Try saying 'hello', 'how are you', or 'bye'")
        
        elif user_input == "bye" or user_input == "goodbye":
            print("Bot: Goodbye! Have a great day!")
            break
        
        else:
            print("Bot: I didn't understand that. Can you say something else?")

if __name__ == "__main__":
    chatbot()
    
