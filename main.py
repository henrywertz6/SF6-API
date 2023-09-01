from fastapi import FastAPI, Response, status, HTTPException, Depends
from models import Character, Move
from sqlmodel import SQLModel, Field, Session, create_engine, select
from database import engine


app = FastAPI()




@app.get("/character/{name}")
def root(name: str):
    with Session(engine) as session:
        character = session.get(Character, name)
        if not character:
            raise HTTPException(status_code=404, detail="Character not found")
        return character

