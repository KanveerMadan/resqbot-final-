
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load the trained model
model = joblib.load("combined_model.pkl")

app = FastAPI()

# Define the expected input format
class ModelInput(BaseModel):
    feature1: float
    feature2: float
    feature3: float
    feature4: float
    feature5: float

@app.post("/predict")
def predict(input_data: ModelInput):
    data = [[
        input_data.feature1,
        input_data.feature2,
        input_data.feature3,
        input_data.feature4,
        input_data.feature5
    ]]
    prediction = model.predict(data)
    return {"prediction": prediction.tolist()}
