from fastapi import FastAPI
app = FastAPI()

# home Route
@app.get("/")
async def home():
    return {"message": "Welcome to the home page!"}

# about Route
@app.get("/about")
def about():
    return {"message": "This is the about page."}

# user Route
@app.get("/users/")
def users():
    return{
        "users":["mohit", "rohit", "Amit"]
    }