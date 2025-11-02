import uuid
import bcrypt
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import TEXT, VARCHAR, Column, LargeBinary, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = FastAPI()

DATABASE_URL = "postgresql://postgres:localhost@admin1234:5432/authentication_system"

create_engine = engine(DATABASE_URL)
SessionaLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionaLocal()

class UserCreate(BaseModel):
    name: str
    email: str
    password: str

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)

@app.post('/signup', status_code=200)
def signup_user(user: UserCreate):
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(400, 'User already exists.')
    
    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), name=user.name, email=user.email, password=hashed_pw)

    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db

Base.metadata.create_all(engine)