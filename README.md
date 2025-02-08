
Number Classification API

A Flask API that classifies numbers and provides fun facts about them.

Installation

1. Clone the repository: `git clone <repository_url>`
2. Change into the project directory: `cd project_directory`
3. Install dependencies: `pip install -r requirements.txt`

Running the API Locally

Using Flask Development Server:
```
bash
flask run --host=0.0.0.0 --port=5000
```

API Endpoint

*Classify a Number*
- URL: `GET /api/classify-number`
- Query Parameter: `number=<integer>`
- Example Request: `curl "http://0.0.0.0:5000/api/classify-number/?number=371"`

Response:
```
{
  "number": 371,
  "is_even": false,
  "is_prime": false,
  "is_armstrong": true,
  "fun_fact": "371 is an Armstrong number because 3**3 + 7**3 + 1**3 = 371"
}
```

Deployment on Render

1. Push your changes to GitHub.
2. Connect the repository to Render.
3. Add a Gunicorn Start Command in Render settings:
```
bash
gunicorn app:app --host 0.0.0.0 --port 5000
```