Hng_backend_api

A Flask API that classifies numbers and provides fun facts about them.
git clone <repository_url>
cd Hng_backend_api
Installation

 1.   Clone the repository:
 git clone <repository_url>
 cd Hng_backend_api
 2. Install dependencies:
 pip install -r requirements.txt
 

 Running the API Locally
 Using Flask Development Server

 flask run --host=0.0.0.0 --port=5000

Using Gunicorn (Recommended for Deployment):

gunicorn -w 4 -b 192.168.107.50:5000 app:app


API Endpoint
Classify a Number

   - URL: GET /api/classify-number
   - Query Parameter: number=<integer>
   - Example Request:

curl "http://192.168.107.50:5000/api/classify-number?number=371"

Response:
json
{
  "number": 371,
  "is_even": false,
  "is_prime": false,
  "is_armstrong": true,
  "fun_fact": "371 is an Armstrong number because 3**3 + 7**3 + 1**3 = 371"
}


Deployment on Render

    - Push your changes to GitHub.

    - Connect the repository to Render.

    - Add a Gunicorn Start Command in Render settings:
    gunicorn -w 4 -b 0.0.0.0:5000 app:app

