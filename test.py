from fastapi import FastAPI

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


@app.get("/user/{id}")
def get_user(id: int):
    return students[id]
