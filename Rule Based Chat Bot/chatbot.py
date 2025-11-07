import re

def simple_chatbot (user_input):
    # Responds to user based on a pre defined set of rules.
    user_input = user_input.lower()

    rules = {
        r"hello|hi|hey": "Hello! How Can I Help You Today?",
        r"how are you": "I'm just a bot, but I'm doing great! How about you?",
        r"what is your name": "I am a simple rule-based chatbot.",
        r"bye|goodbye|exit": "Goodbye! Have a nice day.",
        r"help": "You can ask me things like 'hello', 'how are you', 'what is your name', or 'bye'.",
        # Default fallback rule
        r".*": "I'm sorry, I don't understand that. Can you rephrase? (Type 'help' for options)"
    }

    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    return "I'm Sorry, I don't understand that. Can you rephrase? (Type 'help' for options)"

def main():
    # main function to un the chatbot loop.
    print ("Chatbot: Hello Type 'bye' to exit")

    while True:
        try:    
            user_input = input("You: ")
            response = simple_chatbot(user_input)
            print(f"Chatbot: {response}")

            if re.search(r"bye|goodbye|exit", user_input.lower()):
                break
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye! Hope to see you soon.")
            break

if __name__ == "__main__":
    main()