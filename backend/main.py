from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud, database

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

# Initialize the FastAPI app
app = FastAPI()

# Set up CORS middleware
origins = [
    "http://localhost:3000",  # React default port
    "http://localhost:3001",  # React alternate port
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to the FitFusion API!"}

# API endpoint to register a new user
@app.post("/register", response_model=schemas.User)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if the email is already registered
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    hashed_password = user.password  # In a real application, you should hash the password
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db_user = crud.create_user(db=db, user=db_user)
    
    # Add sample workouts and meal plans
    sample_workout = schemas.WorkoutCreate(name="Sample Workout", description="A sample workout plan.")
    crud.create_workout(db=db, workout=sample_workout, user_id=db_user.id)
    
    sample_meal_plan = schemas.MealPlanCreate(name="Sample Meal Plan", description="A sample meal plan.")
    crud.create_meal_plan(db=db, meal_plan=sample_meal_plan, user_id=db_user.id)
    
    return db_user

# API endpoint to create a workout
@app.post("/users/{user_id}/workouts/", response_model=schemas.Workout)
def create_workout(user_id: int, workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    return crud.create_workout(db=db, workout=workout, user_id=user_id)

# API endpoint to get workouts
@app.get("/users/{user_id}/workouts/", response_model=List[schemas.Workout])
def get_workouts(user_id: int, db: Session = Depends(get_db)):
    return crud.get_workouts(db=db, user_id=user_id)

# API endpoint to create a meal plan
@app.post("/users/{user_id}/meal_plans/", response_model=schemas.MealPlan)
def create_meal_plan(user_id: int, meal_plan: schemas.MealPlanCreate, db: Session = Depends(get_db)):
    return crud.create_meal_plan(db=db, meal_plan=meal_plan, user_id=user_id)

# API endpoint to get meal plans
@app.get("/users/{user_id}/meal_plans/", response_model=List[schemas.MealPlan])
def get_meal_plans(user_id: int, db: Session = Depends(get_db)):
    return crud.get_meal_plans(db=db, user_id=user_id)
