class CanConnectChatbot:
    def __init__(self):
        self.keywords = {
            "hello": "Hello! How can I assist you today?",
            "help": "Sure! What do you need help with?",
            "bye": "Goodbye! Have a great day!",
            # Add more keywords and responses as needed
        }

    def get_response(self, message):
        for keyword, response in self.keywords.items():
            if keyword in message.lower():
                return response
        return "I'm not sure how to respond to that."

    def chat(self):
        print("Welcome to CanConnect AI Assistant! Type 'bye' to exit.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print("Chatbot: Goodbye! Have a great day!")
                break
            response = self.get_response(user_input)
            print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot = CanConnectChatbot()
    chatbot.chat()