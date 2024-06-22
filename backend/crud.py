from sqlalchemy.orm import Session
from . import models, schemas

# Retrieve a user by username
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


# Retrieve a user by email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# Create a new user
def create_user(db: Session, user: models.User):
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


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
