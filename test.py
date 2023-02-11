from typing import Optional
from fastapi import FastAPI, Path

app = FastAPI()

students = {
    1: {
        "name": "Sujan",
        "age": 23,
        "location": "Kolkata"
    }
}


@app.get("/")
def index():
    return {"Hello": "World"}


# @app.get("/user/{user_id}")
# def get_user(user_id: int = Path(None, description="Needs the id of the user")):
#     return students[user_id]


@app.get("/user/{user_id}")
def get_admin(user_id: int, admin: Optional[str] = None):
    if admin == "True":
        return students[user_id]
    else:
        return {"error_msg": "You need to be an admin"}
