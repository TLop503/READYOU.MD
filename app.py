from flask import Flask, request, jsonify
import re
import time

app = Flask(__name__)

def count(text):
    # regex to find all words
    words = re.findall(r'\b\w+\b', text)
    return len(words)

def complexity(text):
    words = re.findall(r'\b\w+\b', text)
    # return proportion of words over len 8 out of 5
    return ((sum(1 for word in words if len(word) > 8) / len(words)) * 5)

@app.route('/read', methods=['POST'])
def read_you():
    data = request.json
    print(data)
    if 'text' not in data:
        return jsonify({'error': 'Text field is missing'}), 400

    text = data['text']
    wc = count(text)
    ttr = wc / 200 #assume 200 wpm
    cpx = complexity(text)

    res = {
        'count' : wc,
        'time_minutes' : ttr,
        'complexity' : f"{cpx}/5"
    }

    return jsonify(res), 200

if __name__ == '__main__':
    app.run(debug=True)
