from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from pydantic import BaseModel
from . import models, schemas, crud, database
from .meal_plan import generate_meal_plan
from .workout_plan import generate_workout_plan
# Importing the meal and workout plan generation functions

from .database import get_db

app = FastAPI()

# Set up CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
database.create_tables()

@app.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)

@app.post("/login", response_model=schemas.User)
def login_user(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    db_user = crud.authenticate_user(db, username=user.username, password=user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return db_user

@app.get("/users/{user_id}", response_model=schemas.UserProfile)
def get_user_profile(user_id: int, db: Session = Depends(database.get_db)):
    db_user = crud.get_user_by_id(db, user_id=user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=schemas.UserProfile)
def update_user_profile(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(database.get_db)):
    db_user = crud.update_user_profile(db, user_id=user_id, user_update=user_update)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user




@app.get("/users/{user_id}/meal_plan", response_model=str)
def get_meal_plan(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    meal_plan = generate_meal_plan(user)
    return meal_plan

@app.get("/users/{user_id}/workout_plan", response_model=str)
def get_workout_plan(user_id: int, db: Session = Depends(database.get_db)):
    user = crud.get_user(db, user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    workout_plan = generate_workout_plan(user)
    return workout_plan



class GeneratePlansRequest(BaseModel):
    user_id: int


@app.post("/generate_meal_plan")
async def generate_meal_plan(request: schemas.MealPlanBase, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == request.user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    meal_plan = models.MealPlan(description="Generated meal plan", user_id=user.id)
    db.add(meal_plan)
    db.commit()
    db.refresh(meal_plan)
    
    return meal_plan

@app.post("/generate_workout_plan")
async def generate_workout_plan(request: schemas.WorkoutBase, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == request.user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    workout_plan = models.WorkoutPlan(description="Generated workout plan", user_id=user.id)
    db.add(workout_plan)
    db.commit()
    db.refresh(workout_plan)
    
    return workout_plan