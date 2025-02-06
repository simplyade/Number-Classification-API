from flask import Flask, request, jsonify
from flask_caching import Cache
from number_classifier import classify_number, is_fun_fact
from flask_cors import CORS
from utils import get_fun_fact
import time

app = Flask(__name__)
CORS(app)

# Redis Cache configuration
cache_config = {'CACHE_TYPE':'redis',
                'CACHE_REDIS_URL':'redis://localhost:6379/0'}
# Initialize cache
cache =Cache(app,config=cache_config)

@app.route('/api/classify-number', methods=['GET'])
@cache.cached(timeout=60,query_string=True) # Cache for  60 seconds
def api_classify_number():
    #start_time = time.time()
    number = request.args.get('number')
    # Validate input: Ensure it's an integer
    if not number or not number.lstrip('-').isdigit():
        return jsonify({"number": "alphabet", "error": True}), 400  # 400 Bad Request
    
    number = int(number)
    
    # Get classification results
    result = classify_number(number)
    
    # Fetch the fun fact from the external API
    fun_fact = get_fun_fact(number)  # Using the get_fun_fact function from utils.py
    
    
    # Call is_fun_fact with the number as integer
    result['fun_fact'] = is_fun_fact(int(number))  # Ensure number is passed as integer
    response = jsonify(result)
    #end_time= time.time()
    #response_time = (end_time- start_time)*1000 # Convert to milliseconds
   # print (f"Response time: {response_time:.2f} " " ms")
    
    return response
    


if __name__ == '__main__':
    app.run (host="0.0.0.0", port=5000)



