from flask import Flask, request, jsonify
from flask_cors import CORS
from number_classifier import classify_number, is_armstrong
import requests

app = Flask(__name__)
CORS(app)

def get_fun_fact(number: int) -> str:
    try:
        url = f"http://numbersapi.com/{number}/math?json=true"
        response = requests.get(url)
        data = response.json()
        return data['text'] if response.status_code == 200 else "No fun fact available."
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/api/classify-number/', methods=['GET'])
def api_classify_number():
    try:
        number = request.args.get('number')
        if number is None:
            return jsonify({"number": "alphabet", "error": True}), 404
        number = int(number)
        result = classify_number(number)
        result['fun_fact'] = get_fun_fact(number)
        return jsonify(result)
    except ValueError:
        return jsonify({"number": "alphabet", "error": True}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)




