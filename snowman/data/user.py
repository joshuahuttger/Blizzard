from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    id: int
    favorite_hobby: str | None = None