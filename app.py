from fastapi import FastAPI, HTTPException
from number_classifier import classify_number, is_fun_fact
from utils import get_fun_fact
from pydantic import BaseModel

app = FastAPI()

class NumberRequest(BaseModel):
    number: int

@app.get("/")
async def index():
    return {"message": "Welcome to the Number Classification API!"}

@app.get("/api/classify-number/")
async def api_classify_number(number_request: NumberRequest):
    result = classify_number(number_request.number)
    result['fun_fact'] = is_fun_fact(number_request.number)
    result['external_fact'] = get_fun_fact(number_request.number)
    return result

Alternatively, you can use query parameters
@app.get("/api/classify-number-alt")
async def api_classify_number_alt(number: int):
    if not isinstance(number, int):
        raise HTTPException(status_code=400, detail="Invalid input. Provide a valid integer.")
    result = classify_number(number)
    result['fun_fact'] = is_fun_fact(number)
    result['external_fact'] = get_fun_fact(number)
    return result


