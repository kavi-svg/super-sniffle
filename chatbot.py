import nltk
from nltk.chat.util import Chat, reflections

for resource in ['tokenizers/punkt', 'taggers/averaged_perceptron_tagger']:
    try:
        nltk.data.find(resource)
    except LookupError:
        nltk.download(resource.split('/')[1], quiet=True)

pairs = [
    [r"hi|hello|hey", ["Hello! Kaise help karoon?", "Hi there!"]],
    [r"my name is (.*)", ["Hello %1! Kya kaam hai?"]],
    [r"(?:what is|what's|whats) your name\??", ["My name is Alex.", "Main Alex hoon!"]],
    [r"(.*) your name\?", ["My name is Alex.", "Main Alex hoon!"]],
    [r"how are you\??", ["Good, and what about you?", "I'm fine, and you?"]],
    [r"how u doing\??", ["Good, and what about you?", "I'm fine, and you?"]],
    [r"what about you\??", ["Good, and what about you?", "I'm fine, and you?"]],
    [r"tell me a joke", ["Ek chutkula: Ek aadmi computer ko pyar karne laga."]],
    [r"bye|exit|quit", ["Goodbye! Achha din ho!", "Phir milte hain!"]],
    [r"(.*)", ["Samjha nahi, dobara poocho?", "Kya aap ise thoda aur clearly bata sakte hain?"]]
]

class RuleBasedChatbot:
    def __init__(self, pairs):
        self.chat = Chat(pairs, reflections)

    def respond(self, user_input):
        return self.chat.respond(user_input)


def chat_with_bot():
    print("Chatbot ready hai! Type 'start' to begin or 'exit'/'bye'/'quit' to end.")
    while True:
        user_input = input("You: ")
        normalized = user_input.strip().lower()
        if normalized in ('exit', 'bye', 'quit'):
            print("Chatbot: Goodbye! Have a nice day!")
            break
        if normalized == 'start':
            print("Chatbot: Shuru karte hain! Aap kya poochna chahenge?")
            continue
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")


if __name__ == '__main__':
    chatbot = RuleBasedChatbot(pairs)
    chat_with_bot()
