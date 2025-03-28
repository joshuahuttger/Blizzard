from fastapi import FastAPI

from snowman.data.user import User

app = FastAPI()

temp_store = dict()

@app.get("/users/{user_id}")
async def get_user(user_id : int):
    return temp_store[user_id]

@app.post("/users/")
async def create_user(user: User):
    temp_store[user.id] = user
    return temp_store[user.id]