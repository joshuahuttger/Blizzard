from fastapi import FastAPI

from snowman.data.user import User

app = FastAPI()

@app.get("/user/{user_id}")
async def get_user(user_id):
    return User("jhuggz","jhuggz@skynet.net",12343)

