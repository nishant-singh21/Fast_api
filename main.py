import json
from pathlib import Path

from fastapi import FastAPI

app = FastAPI()


def load_data():
    # Load your data here
     with open("patient.json", "r") as f:
        data = json.load(f)
        
     return data





@app.get("/")
def home():
    return {"message": "patient Management system API "}


@app.get('/about')
def about():
    return {"message": "A fully functional patient Api to manage your pateint records"}  



@app.get('/view')
def view():
    data = load_data()
    return data