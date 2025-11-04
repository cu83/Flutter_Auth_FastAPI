from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config

params = config()

DATABASE_URL = f"postgresql://{params['username']}:{params['password']}@{params['hostname']}:{params['port']}/{params['database']}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()