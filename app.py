
from fastapi import FastAPI
from pydantic import BaseModel
import pickle

app = FastAPI()

with open('model.pkl', 'rb') as f:
    clf, feature_names, target_names = pickle.load(f)

class Features(BaseModel):
    features: list

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post('/predict')
def predict(input: Features):
    pred = clf.predict([input.features])[0]
    return {'prediction': target_names[pred]}
