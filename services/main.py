from typing import Dict, List
from fastapi import FastAPI
import joblib
from pydantic import BaseModel
import pandas as pd
import os 

class RequestItem(BaseModel):
    orders: List[Dict]

class ResponseItem(BaseModel):
    predictions: List

app = FastAPI()

@app.post("/predictions", response_model=ResponseItem)
async def gen_predictions(request: RequestItem):
    request = request.dict()
    if os.getenv("MODEL") == "baseline":
        results = [1012.0908190373273] * len(request["orders"])
    else:
        model = joblib.load("model.joblib")
        data = pd.DataFrame(request["orders"])
        results = model.predict(data).tolist()
    return {"predictions": results}