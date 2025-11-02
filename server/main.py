import uuid
import bcrypt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI

DATABASE_URL = "postgresql://postgres:admin1234@localhost:5432/authentication_system"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

class UserCreate(BaseModel):
    name = str
    email = str
    password = str

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)

@app.post('/signup', 200)
def signup_user(user: UserCreate):
    
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        HTTPException(400, 'User already exists.')

    hashed_pw = bcrypt(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), name=user.name, email=user.email, password=hashed_pw)

    db.add(user_db)
    db.commit()
    db.refresh(user_db)

Base.metadata.create_all(engine)