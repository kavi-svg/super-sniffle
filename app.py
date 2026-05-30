from flask import Flask, render_template, request, jsonify
from chatbot import RuleBasedChatbot, pairs

app = Flask(__name__)
chatbot = RuleBasedChatbot(pairs)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json or {}
    text = data.get('message', '')
    resp = chatbot.respond(text) or "Samjha nahi, dobara poocho?"
    return jsonify({"response": resp})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
