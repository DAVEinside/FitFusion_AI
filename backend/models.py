from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Base class for all SQLAlchemy models
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  # Name of the table in the database
    id = Column(Integer, primary_key=True, index=True)  # Primary key column
    username = Column(String, unique=True, index=True)  # Username column
    email = Column(String, unique=True, index=True)  # Email column
    hashed_password = Column(String)  # Hashed password column
