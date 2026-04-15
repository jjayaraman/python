from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
import logfire

app =  FastAPI()
logfire.configure()
logfire.instrument_fastapi(app)


class User(BaseModel):
  firstName:str = Field(min_length=1,max_length=5)
  lastName:str = Field(pattern="^[A-Za-z0-9]*$")
  age: int = Field(ge=0,lt=150)
  email:EmailStr

@app.get("/")
def hello():
  logfire.debug("Calling hello api..zz")
  return {"message": "hello"}


@app.post("/user")
def create_user(user:User):
  return user

@app.get("/users")
def get_users():
  return "users"