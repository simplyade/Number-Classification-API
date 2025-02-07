from fastapi import FastAPI, HTTPException,Query
from number_classifier import classify_number, is_fun_fact


app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Welcome to the Number Classification API!"}

@app.get("/api/classify-number/")
async def api_classify_number(number: int = Query(...)):
    result = classify_number(number)
    result['fun_fact'] = is_fun_fact(number)
    return result





