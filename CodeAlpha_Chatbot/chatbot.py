def get_response(user_input):
    text = user_input.lower().strip()

    if "hello" in text or "hi" in text:
        return "Hi! How can I help you today?"
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"
    elif "your name" in text:
        return "I'm a simple rule-based chatbot."
    elif "thank" in text:
        return "You're welcome!"
    elif "help" in text:
        return "You can say hello, ask how I am, ask my name, ask for a joke, ask about the weather, or say bye.Type help to see options"
    elif "weather" in text:
        return "I can't check the weather, but I hope it's nice outside!"
    elif "joke" in text:
        return "Why do programmers prefer dark mode? Because light attracts bugs."
    elif "age" in text or "how old" in text:
        return "I don't have an age, I'm just lines of code!"
    elif "bye" in text or "goodbye" in text:
        return "Goodbye! Have a great day."
    elif "what can you do" in text:
        return "You can say hello, ask how I am, ask my name, or say bye."
    else:
        return "Sorry, I didn't understand that. Try typing 'help'."
    
def main():
    print("Simple Chatbot (type 'bye' to exit)")

    while True:
        user_input = input("\nYou: ")
        response = get_response(user_input)
        print(f"Bot: {response}")

        if "bye" in user_input.lower():
            break

if __name__ == "__main__":
    main()