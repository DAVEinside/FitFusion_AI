from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
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
    
    # In a real application, you should hash the password
    hashed_password = user.password
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed_password)
    
    # Create the new user
    return crud.create_user(db=db, user=db_user)

