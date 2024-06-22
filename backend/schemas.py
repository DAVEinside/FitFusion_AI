from pydantic import BaseModel
from typing import List, Optional

class WorkoutBase(BaseModel):
    name: str
    description: Optional[str] = None

class WorkoutCreate(WorkoutBase):
    pass

class Workout(WorkoutBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class MealPlanBase(BaseModel):
    name: str
    description: Optional[str] = None

class MealPlanCreate(MealPlanBase):
    pass

class MealPlan(MealPlanBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    workouts: List[Workout] = []
    meal_plans: List[MealPlan] = []

    class Config:
        orm_mode = True
