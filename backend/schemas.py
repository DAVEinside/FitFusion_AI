from pydantic import BaseModel

# Pydantic model for user creation request
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Pydantic model for user response
class User(BaseModel):
    id: int
    username: str
    email: str

    # Configuration to support ORM mode
    class Config:
        orm_mode = True
