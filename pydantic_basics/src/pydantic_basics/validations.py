from pydantic import BaseModel, EmailStr, Field

class User(BaseModel):
    id: int
    firstName: str = Field(min_length=1, max_length=50)
    lastName: str = Field(min_length=1, max_length=50)
    email: EmailStr = Field(min_length=1, max_length=100)
    isActive: bool = Field(default=True)

user = User(id=1, firstName="J", lastName="doe", email="test@gmail.com", isActive=True)
user.mo
print(user)