from typing import List, Optional
from pydantic import BaseModel

class WorkoutBase(BaseModel):
    name: str
    description: Optional[str] = None

class WorkoutCreate(WorkoutBase):
    pass

class Workout(WorkoutBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class MealPlanBase(BaseModel):
    name: str
    description: Optional[str] = None

class MealPlanCreate(MealPlanBase):
    pass

class MealPlan(MealPlanBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserUpdate(BaseModel):
    id: int
    full_name: Optional[str] = None
    age: Optional[int] = None
    height: Optional[int] = None
    weight: Optional[int] = None
    fitness_goals: Optional[str] = None
    dietary_preferences: Optional[str] = None
    health_conditions: Optional[str] = None

class User(UserBase):
    id: int
    is_active: bool
    workouts: List[Workout] = []
    meal_plans: List[MealPlan] = []

    class Config:
        from_attributes = True
