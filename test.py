from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

user = {
    1: {
        "name": "Sujan",
        "age": 23,
        "location": "Kolkata"
    }
}

# BaseModal create to store the user modal


class User(BaseModel):
    name: str
    age: int
    location: str

# GET methord


@app.get("/")
def index():
    return {"Hello": "World"}


# @app.get("/user/{user_id}")
# def get_user(user_id: int = Path(None, description="Needs the id of the user")):
#     return user[user_id]

# Query Params

@app.get("/user/{user_id}")
def get_admin(user_id: int, admin: Optional[str] = None):
    if admin == "True":
        return user[user_id]
    else:
        return {"error_msg": "You need to be an admin"}


# POST methord

@app.post("/create_user/{user_id}")
def create_user(user_id: int, user_details: User):
    if user_id in user:
        return {"error_msg": "User already exists"}
    else:
        user[user_id] = user_details
        return user[user_id]
