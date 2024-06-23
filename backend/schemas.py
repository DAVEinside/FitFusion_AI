from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class WorkoutBase(BaseModel):
    title: str
    description: str

class WorkoutCreate(WorkoutBase):
    pass

class Workout(WorkoutBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class MealPlanBase(BaseModel):
    title: str
    description: str

class MealPlanCreate(MealPlanBase):
    pass

class MealPlan(MealPlanBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class UserWithPlans(UserBase):
    id: int
    meal_plans: List[MealPlan]
    workouts: List[Workout]

    class Config:
        orm_mode = True
