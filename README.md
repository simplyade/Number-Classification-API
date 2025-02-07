Number Classification API

A Flask API that classifies numbers and provides fun facts about them.
git clone <repository_url>
cd project_directory
Installation

 1.   Clone the repository:
 git clone <repository_url>
 cd project_directory
 2. Install dependencies:
 pip install -r requirements.txt
 

 Running the API Locally
 Using Flask Development Server

 flask run --host=0.0.0.0 --port=8000

Using uvicorn (Recommended for Deployment):

uvicorn app:app --host 0.0.0.0 --port 8000

API Endpoint
Classify a Number

   - URL: GET /api/classify-number
   - Query Parameter: number=<integer>
   - Example Request:

curl "http://0.0.0.0:8000/api/classify-number/?number=371"

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

    - Add a uvicorn Start Command in Render settings:
    uvicorn app:app --host 0.0.0.0 --port 8000

