from fastapi import FastAPI, Response, status, HTTPException, Depends
from models import Character, Move, CharacterOut, APIResource
from sqlmodel import SQLModel, Field, Session, create_engine, select
from typing import List
from deta import Deta


app = FastAPI()
deta = Deta()

dbCharacters = deta.Base("characters")

dbMoves = deta.Base("moves")



@app.get("/api/characters", response_model=List[Character])
def get_all_characters():
    all_characters = dbCharacters.fetch()
    resultList = []
    for item in all_characters.items:
        character = Character(name=item["name"], vitality=item["vitality"], height=item["height"], weight=item["weight"])
        resultList.append(character)
    return resultList

async def fetchName(name):
    response = dbCharacters.fetch({"name": name})
    if (len(response.items) == 0):
        raise HTTPException(status_code=404, detail="Character not found")
    return response.items

async def fetchNormals(name):
    response =  dbMoves.fetch({"character": name, "type": "Normal Moves"})
    normal_moves = []
    for item in response.items:
        normal_moves.append(APIResource(name=item["name"], url=f"http://sfapi.co/api/move/{item['id']}"))
    return normal_moves

async def fetchUniques(name):
    response = dbMoves.fetch({"character": name, "type": "Unique Attacks"})
    unique_attacks = []
    for item in response.items:
        unique_attacks.append(APIResource(name=item["name"], url=f"http://sfapi.co/api/move/{item['id']}"))
    return unique_attacks


async def fetchSpecials(name):
    response = dbMoves.fetch({"character": name, "type": "Special Moves"})
    special_moves = []
    for item in response.items:
        special_moves.append(APIResource(name=item["name"], url=f"http://sfapi.co/api/move/{item['id']}"))
    return special_moves


async def fetchSupers(name):
    response = dbMoves.fetch({"character": name, "type": "Super Arts"})
    super_arts = []
    for item in response.items:
        super_arts.append(APIResource(name=item["name"], url=f"http://sfapi.co/api/move/{item['id']}"))
    return super_arts

async def fetchThrows(name):
    response = dbMoves.fetch({"character": name, "type": "Throws"})
    throws = []
    for item in response.items:
        throws.append(APIResource(name=item["name"], url=f"http://sfapi.co/api/move/{item['id']}"))
    return throws

async def fetchCommons(name):
    response = dbMoves.fetch({"character": name, "type": "Common Moves"})
    common_moves = []
    for item in response.items:
        common_moves.append(APIResource(name=item["name"], url=f"http://sfapi.co/api/move/{item['id']}"))
    return common_moves


@app.get("/api/characters/{name}", response_model=CharacterOut)
async def get_character(name: str):
    character_response = await fetchName(name)
    # Get normal moves APIResources
    normal_moves = await fetchNormals(name)
    
    
            
    # Get unique attacks APIResources
    unique_attacks = await fetchUniques(name)

    # Get special moves APIResources
    special_moves = await fetchSpecials(name)

    # Get super arts APIResources
    super_arts = await fetchSupers(name)

    # Get throws APIResources
    throws = await fetchThrows(name)

    # Get common moves APIResources
    common_moves = await fetchCommons(name)

    character_out = CharacterOut(
        name=character_response[0]["name"],
        vitality=character_response[0]["vitality"],
        height=character_response[0]["height"],
        weight=character_response[0]["weight"],
        normal_moves=normal_moves,
        unique_attacks=unique_attacks,
        special_moves=special_moves,
        super_arts=super_arts,
        throws=throws,
        common_moves=common_moves
    )
    
    return character_out

@app.get("/api/move/{id}", response_model=Move)
def get_move_info(id: int):
    move_response = dbMoves.fetch({"id": id})
    if (len(move_response.items) == 0):
        raise HTTPException(status_code=404, detail=f"Move with id {id} does not exist")
    
    return move_response.items[0]