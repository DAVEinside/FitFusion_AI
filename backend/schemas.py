from pydantic import BaseModel, EmailStr
from typing import Optional

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str
    age: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    fitness_goals: Optional[str] = None
    dietary_preferences: Optional[str] = None
    health_conditions: Optional[str] = None

class UserLogin(BaseModel):
    username: str
    password: str

class UserProfile(UserBase):
    age: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    fitness_goals: Optional[str] = None
    dietary_preferences: Optional[str] = None
    health_conditions: Optional[str] = None

    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    age: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    fitness_goals: Optional[str] = None
    dietary_preferences: Optional[str] = None
    health_conditions: Optional[str] = None

class User(UserBase):
    id: int
    age: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None
    fitness_goals: Optional[str] = None
    dietary_preferences: Optional[str] = None
    health_conditions: Optional[str] = None

    class Config:
        from_attributes = True

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
