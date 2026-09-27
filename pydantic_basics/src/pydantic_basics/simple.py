from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id:int
    firstName:str
    lastName:str
    email:EmailStr
    isActive: bool = Field(default=True)

user = User(id=1, firstName="jay", lastName="doe", email="jay.doe@example.com")

print(user)

