from fastapi import FastAPI, Response, status, HTTPException, Depends
from datascraper import data_scrape
import models
from models import Character
from sqlalchemy.orm import Session
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Welcome to the api"}


@app.get("/test")
def test_api(character: Character, db: Session = Depends(get_db)):
    return {"status": "success"}

@app.post("/test")
def input_characters(db: Session = Depends(get_db)):
    return {"status": "success"}