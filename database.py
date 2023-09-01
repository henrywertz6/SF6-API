from typing import Optional
from datascraper import get_frame_data, get_character_data
from settings import password
from sqlmodel import create_engine, SQLModel, Session
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from models import Move, Character

SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:{password}@localhost/SF6API'
options = Options()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)




engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
character_names = ['rashid', 'cammy', 'lily', 'zangief', 'jp', 'marisa', 'manon', 'deejay', 'ehonda', 'dhalsim', 'blanka', 'ken', 'juri', 'kimberly', 'guile', 'chunli', 'jamie', 'luke', 'ryu']

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def create_moves():
    session = Session(engine)
    
    characterData = get_frame_data(driver)
    print("Here's the data: ", characterData)
    for character in character_names:
        for moveList in characterData[character]:
            for moveType in moveList:
                for moveAttributes in moveList[moveType]:
                
                    removeExtras = moveAttributes[0].split("\n")
                    moveAttributes[0] = removeExtras[0]
                    db_move = Move(name=moveAttributes[0], startup=moveAttributes[1], active=moveAttributes[2], recovery=moveAttributes[3],
                                            onHit=moveAttributes[4], onBlock=moveAttributes[5], cancel=moveAttributes[6], damage=moveAttributes[7],
                                            comboScaling=moveAttributes[8], dgHitIncrease=moveAttributes[9], dgBlockDecrease=moveAttributes[10],
                                            dgPunishDecrease=moveAttributes[11], superArtIncrease=moveAttributes[12], hitboxProperty=moveAttributes[13],
                                            extraInfo=moveAttributes[14], character=character)
                    session.add(db_move)
                
    session.commit()
    
    session.close()

def create_character():
    session = Session(engine)

    for character in character_names:
        db_character = Character(name=character, )
def main():
    # create_db_and_tables()
    # create_moves()
    char_details = get_character_data(driver)
    for character in character_names:
        for detailsList in char_details[character]:
            for detail in detailsList:
                print(detail)

if __name__ == "__main__":
    main()