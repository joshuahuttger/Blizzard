from fastapi import FastAPI

from snowman.data.user import User

app = FastAPI()

@app.get("/user/{user_id}")
async def get_user(user_id):
    return User("jhuggz","jhuggz@skynet.net",12343, "eating chicken")

@app.get("/user")
async def get_user(name: str, email: str, credit_card_number: int, favorite_hobby: str = "netflix"):
#http://127.0.0.1:8000/user?name=Joshua%20Huttger&email=jhuttger@skynet.net&credit_card_number=1231234&favorite_hobby=skiing
    return User(name,email,credit_card_number, favorite_hobby)