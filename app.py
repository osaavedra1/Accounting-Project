from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    input_word = request.json['word']
    # Process the input word and generate output
    output = f"Generated output based on '{input_word}'"
    return jsonify({'output': output})

if __name__ == '__main__':
    app.run(debug=True)
