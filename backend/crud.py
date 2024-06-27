from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Retrieve a user by username
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# Retrieve a user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user or not verify_password(password, user.hashed_password):
        return None
    return user

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = get_user_by_id(db, user_id)
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def create_workout(db: Session, workout: schemas.WorkoutCreate, user_id: int):
    db_workout = models.Workout(**workout.dict(), owner_id=user_id)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

def get_workouts(db: Session, user_id: int):
    return db.query(models.Workout).filter(models.Workout.owner_id == user_id).all()

def create_meal_plan(db: Session, meal_plan: schemas.MealPlanCreate, user_id: int):
    db_meal_plan = models.MealPlan(**meal_plan.dict(), owner_id=user_id)
    db.add(db_meal_plan)
    db.commit()
    db.refresh(db_meal_plan)
    return db_meal_plan

def get_meal_plans(db: Session, user_id: int):
    return db.query(models.MealPlan).filter(models.MealPlan.owner_id == user_id).all()
