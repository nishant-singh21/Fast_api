import json
from pathlib import Path

from fastapi import FastAPI

app = FastAPI()


# Get the folder containing main.py
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "patient.json"


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data

# def load_data():
#     # Load your data here
#      with open("patient.json", "r") as f:
#         data = json.load(f)
        
#      return data





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