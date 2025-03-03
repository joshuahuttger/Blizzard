from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{user_id}")
async def get_user(user_id):
    return {"user_id": user_id}
