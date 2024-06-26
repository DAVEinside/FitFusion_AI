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
