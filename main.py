from fastapi import FastAPI, Response, status, HTTPException, Depends
from models import Character, Move, CharacterOut, APIResource
from sqlmodel import SQLModel, Field, Session, create_engine, select
from database import engine


app = FastAPI()




@app.get("/character/{name}")
def get_character(name: str):
    with Session(engine) as session:
        character = session.get(Character, name)
        if not character:
            raise HTTPException(status_code=404, detail="Character not found")
        # Get normal moves APIResources
        statement = select(Move).where(Move.character == name, Move.type == "Normal Moves")
        results = session.exec(statement)
        normal_moves = []
        for result in results:
            normal_moves.append(APIResource(name=result.name, url=f"http://127.0.0.1:8000/move/{result.id}"))
        
        # Get unique attacks APIResources
        statement = select(Move).where(Move.character == name, Move.type == "Unique Attacks")
        results = session.exec(statement)
        unique_attacks = []
        for result in results:
            unique_attacks.append(APIResource(name=result.name, url=f"http://127.0.0.1:8000/move/{result.id}"))

        # Get special moves APIResources
        statement = select(Move).where(Move.character == name, Move.type == "Special Moves")
        results = session.exec(statement)
        special_moves = []
        for result in results:
            special_moves.append(APIResource(name=result.name, url=f"http://127.0.0.1:8000/move/{result.id}"))

        # Get super arts APIResources
        statement = select(Move).where(Move.character == name, Move.type == "Super Arts")
        results = session.exec(statement)
        super_arts = []
        for result in results:
            super_arts.append(APIResource(name=result.name, url=f"http://127.0.0.1:8000/move/{result.id}"))

        # Get throws APIResources
        statement = select(Move).where(Move.character == name, Move.type == "Throws")
        results = session.exec(statement)
        throws = []
        for result in results:
            throws.append(APIResource(name=result.name, url=f"http://127.0.0.1:8000/move/{result.id}"))

        # Get common moves APIResources
        statement = select(Move).where(Move.character == name, Move.type == "Common Moves")
        results = session.exec(statement)
        common_moves = []
        for result in results:
            common_moves.append(APIResource(name=result.name, url=f"http://127.0.0.1:8000/move/{result.id}"))


        character_response = CharacterOut(
            name=character.name,
            vitality=character.vitality,
            height=character.height,
            weight=character.weight,
            normal_moves=normal_moves,
            unique_attacks=unique_attacks,
            special_moves=special_moves,
            super_arts=super_arts,
            throws=throws,
            common_moves=common_moves
        )
        
        return character_response

@app.get("/move/{id}")
def get_move_info(id: int):
    with Session(engine) as session:
        move = session.get(Move, id)
        return move