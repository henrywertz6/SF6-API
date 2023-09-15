from typing import Optional
from datascraper import get_frame_data, get_character_data
from sqlmodel import create_engine, SQLModel, Session
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from models import Move, Character
from deta import Deta
from fastapi.encoders import jsonable_encoder





character_names = ['rashid', 'cammy', 'lily', 'zangief', 'jp', 'marisa', 'manon', 'deejay', 'ehonda', 'dhalsim', 'blanka', 'ken', 'juri', 'kimberly', 'guile', 'chunli', 'jamie', 'luke', 'ryu']


def create_moves(dbMoves, driver):
    id = 0
    characterData = get_frame_data(driver)
    for character in character_names:
        for moveList in characterData[character]:
            for moveType in moveList:
                for moveAttributes in moveList[moveType]:
                
                    removeExtras = moveAttributes[0].split("\n")
                    moveAttributes[0] = removeExtras[0]
                    db_move = Move(name=moveAttributes[0], type=moveType, startup=moveAttributes[1], active=moveAttributes[2], recovery=moveAttributes[3],
                                            onHit=moveAttributes[4], onBlock=moveAttributes[5], cancel=moveAttributes[6], damage=moveAttributes[7],
                                            comboScaling=moveAttributes[8], dgHitIncrease=moveAttributes[9], dgBlockDecrease=moveAttributes[10],
                                            dgPunishDecrease=moveAttributes[11], superArtIncrease=moveAttributes[12], hitboxProperty=moveAttributes[13],
                                            extraInfo=moveAttributes[14], character=character, id=id)
                    dbMoves.put(jsonable_encoder(db_move), str(id))
                    print("added a move")
                    id += 1
    print("we done for now")
                
    

def create_character(dbCharacters, driver):
    char_details = get_character_data(driver)
    for character in character_names:
        for detailsList in char_details[character]:
            db_character = Character(name=detailsList["name"], vitality=detailsList["vitality"], height=detailsList["height"], weight=detailsList["weight"])
            dbCharacters.put(jsonable_encoder(db_character))
            print("we doing this shit")
            
    
            
def main():
    create_moves()
    create_character()
    

if __name__ == "__main__":
    main()