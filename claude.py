from flask import Flask, request, jsonify
import requests
import anthropic
import json
from anthropic.types.text_block import TextBlock

app = Flask(__name__)


class AnthropicTextBlockEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, TextBlock):
            text = obj.text
            if text.startswith('[\n "'):
                text = text[4:-2]  # Remove the array wrapping and trailing quote
                text = text.replace('\\n', '\n').replace('\\\\n', '\n').replace('\\"', '"')  # Replace escape sequences
            return text
        return super().default(obj)
    


def send_message_to_claude(prompt):

    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  # Replace YOUR_API_KEY with your actual OpenAI API key
    )
    message = client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    
    print(message.content)
    serialized_data= json.dumps(message.content, cls=AnthropicTextBlockEncoder, indent=2)
    return serialized_data

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('prompt')
    if user_input.lower() == 'quit':
        return jsonify({"message": "Goodbye!"})
    else:
        bot_message = send_message_to_claude(user_input)
        return jsonify({"message": bot_message})

if __name__ == "__main__":
    app.run(debug=True)