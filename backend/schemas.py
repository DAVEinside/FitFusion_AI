from pydantic import BaseModel, EmailStr
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True  # Update to from_attributes if using Pydantic V2

class WorkoutBase(BaseModel):
    title: str
    description: str

class WorkoutCreate(WorkoutBase):
    pass

class Workout(WorkoutBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True  # Update to from_attributes if using Pydantic V2

class MealPlanBase(BaseModel):
    title: str
    description: str

class MealPlanCreate(MealPlanBase):
    pass

class MealPlan(MealPlanBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True  # Update to from_attributes if using Pydantic V2
