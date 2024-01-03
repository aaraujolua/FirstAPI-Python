from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    user: Optional[str] = None
    password: str

app = FastAPI()

@app.get("/hello-world")
def read_root():
    return {"Msg": "Hello World, this is my first Python api"}

@app.get("/api/sum")
def sum():
    return {"Result": 4+3}


@app.post("/api/login")
def login(user: User):
    if user.user == "lua" and user.password == "123lua":
        return { "Msg": "Successful login!"}

    else:
        return { "Msg": "Login or password incorrect!"}