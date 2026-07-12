from fastapi import FastAPI
app = FastAPI()

# User routes
@app.get("/users/{user_id}")
async def get_users(user_id : int):
    return {"user_id": user_id}