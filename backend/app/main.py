from fastapi import FastAPI, Depends
from .core.config import settings
from sqlalchemy.orm import Session
from .database import get_db, Base, engine
from sqlalchemy import text



app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get('/')
def root():
    return {"message": "This is Home page."}
