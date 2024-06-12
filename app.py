from flask import Flask, render_template, request, jsonify
from openai_utils import get_openai_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({'response': 'No question provided.'})
    
    try:
        response = get_openai_response(question)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'response': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
