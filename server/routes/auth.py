from fastapi import HTTPException, Depends, APIRouter
from pydantic_schemas.user_create import UserCreate
from database import get_db
from models.user import User
from sqlalchemy.orm import Session
import bcrypt
import uuid

router = APIRouter()

@router.post('/signup', status_code=201)
def signup_user(user: UserCreate, db: Session=Depends(get_db)):
    
    user_db = db.query(User).filter(User.email == user.email).first()

    if user_db:
        raise HTTPException(400, 'User already exists.')

    hashed_pw = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    user_db = User(id=str(uuid.uuid4()), name=user.name, email=user.email, password=hashed_pw)

    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db