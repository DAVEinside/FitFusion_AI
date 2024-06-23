from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from . import models, schemas, crud, database

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

@app.post("/login", response_model=schemas.UserWithPlans)
def login_user(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    db_user = crud.authenticate_user(db, username=user.username, password=user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    meal_plans = crud.get_meal_plans(db, user_id=db_user.id)
    workouts = crud.get_workouts(db, user_id=db_user.id)
    
    return {
        "id": db_user.id,
        "username": db_user.username,
        "email": db_user.email,
        "meal_plans": meal_plans,
        "workouts": workouts
    }

@app.get("/users/{user_id}/workouts/", response_model=schemas.Workout)
def read_workouts(user_id: int, db: Session = Depends(database.get_db)):
    workouts = crud.get_workouts_by_user(db, user_id=user_id)
    return workouts

@app.get("/users/{user_id}/meal_plans/", response_model=schemas.MealPlan)
def read_meal_plans(user_id: int, db: Session = Depends(database.get_db)):
    meal_plans = crud.get_meal_plans_by_user(db, user_id=user_id)
    return meal_plans
