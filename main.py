from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "FastAPI is working"}


@app.get('/about')
def about():
    return {"message": "This is the about of my web page "}