

"""
Number Classification API

This API provides endpoints for classifying numbers and retrieving fun facts.
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from number_classifier import classify_number, is_armstrong
import requests
import logging
import unittest

app = Flask(__name__)
CORS(app)

Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_fun_fact(number: int) -> str:
    """
    Retrieves a fun fact about a given number from the Numbers API.

    Args:
        number (int): The number for which to retrieve a fun fact.

    Returns:
        str: The fun fact about the number, or an error message if the request fails.
    """
    try:
        url = f"http://numbersapi.com/{number}/math?json=true"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        return data['text']
    except requests.exceptions.RequestException as e:
        logger.error(f"Error retrieving fun fact: {e}")
        return "An error occurred while retrieving the fun fact."
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return "An unexpected error occurred."

def validate_input(number: str) -> int:
    """
    Validates the input number and converts it to an integer.

    Args:
        number (str): The input number as a string.

    Returns:
        int: The validated and converted input number.

    Raises:
        ValueError: If the input number is not a valid integer.
    """
    try:
        number = int(number)
        if number < 0:
            raise ValueError("Input number must be a non-negative integer.")
        return number
    except ValueError as e:
        logger.error(f"Invalid input number: {e}")
        raise ValueError("Invalid input number.") from e

@app.route('/api/classify-number/', methods=['GET'])
def api_classify_number():
    """
    Classifies a given number and retrieves a fun fact about it.

    Args:
        number (int): The number to classify, passed as a query parameter.

    Returns:
        jsonify: A JSON response containing the classification result and fun fact.
    """
    try:
        number = request.args.get('number')
        if number is None:
            return jsonify({"error": "Missing required query parameter 'number'."}), 400
        number = validate_input(number)
        result = classify_number(number)
        result['fun_fact'] = get_fun_fact(number)
        return jsonify(result)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred."}), 500

class TestNumberClassificationAPI(unittest.TestCase):
    def test_classify_number(self):
        # Test with a valid input number
        response = requests.get('http://localhost:5000/api/classify-number/?number=42')
        self.assertEqual(response.status_code, 200)
        self.assertIn('classification', response.json())
        self.assertIn('fun_fact', response.json())

        # Test with an invalid input number
        response = requests.get('http://localhost:5000/api/classify-number/?number=abc')
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())

if __name__ == '__main__':
    unittest.main()
    app.run(host="0.0.0.0", port=5000)


