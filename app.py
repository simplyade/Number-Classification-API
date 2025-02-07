from flask import Flask, request, jsonify
from number_classifier import classify_number, is_fun_fact
from flask_cors import CORS
from utils import get_fun_fact
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Number Classification API!"})

@app.route('/api/classify-number', methods=['GET'])
def api_classify_number():
    number = request.args.get('number')
    # Validate input
    try:
        number = int(number)
    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Provide a valid integer."}), 400

    # Classify number and fetch fun fact
    result = classify_number(number)
    result['fun_fact'] = is_fun_fact(number)  # Ensure is_fun_fact is robust
    result['external_fact'] = get_fun_fact(number)  # Use get_fun_fact for external API
    
    return jsonify(result)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use PORT from environment, default to 5000
    app.run(host="0.0.0.0", port=port, debug=False)  # Disable debug for production