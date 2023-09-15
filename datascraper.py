from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
def get_frame_data(driver):
    
    character_names = ['rashid', 'cammy', 'lily', 'zangief', 'jp', 'marisa', 'manon', 'deejay', 'ehonda', 'dhalsim', 'blanka', 'ken', 'juri', 'kimberly', 'guile', 'chunli', 'jamie', 'luke', 'ryu']
    
    characterMoveList = {}
    for character_name in character_names:
        characterMoveList[character_name] = []
    moveTypeIndex = ""
    for character in character_names:
        moveList = {
            "Normal Moves": [],
            "Unique Attacks": [],
            "Special Moves": [],
            "Super Arts": [],
            "Throws": [],
            "Common Moves": []
        }
        driver.get(f'https://www.streetfighter.com/6/character/{character}/frame')
        

        mytable = driver.find_elements(By.TAG_NAME, "tbody")
        rows = mytable[0].find_elements(By.TAG_NAME, "tr")
        for row in rows:
            move = []
            
            rowClass = row.get_attribute("class")
            if rowClass == "frame_heading__YeMdJ":
                moveTypeIndex = row.text
            else:
                cols = row.find_elements(By.TAG_NAME, 'td')
                for col in cols:
                    move.append(col.text)
                
                moveList[moveTypeIndex].append(move)

        # title = list(filter(None, title))
        # finalTitles = []
        # for element in title:
        #     finalTitles.append(element[0].text)
        # print(finalTitles)
        for moveType in moveList:
            for move in moveList[moveType]:
                move = list(filter(None, move))
        # print(moveList)
        characterMoveList[character].append(moveList)
        print("loaded character data")
    return characterMoveList

def get_character_data(driver):
    character_names = ['rashid', 'cammy', 'lily', 'zangief', 'jp', 'marisa', 'manon', 'deejay', 'ehonda', 'dhalsim', 'blanka', 'ken', 'juri', 'kimberly', 'guile', 'chunli', 'jamie', 'luke', 'ryu']
    character_detail_list = {}
    for character in character_names:
        character_detail_list[character] = []
    
    for character in character_names:
        characterDetails = {
        "name": "",
        "vitality": "",
        "height": "",
        "weight": "",
        }
        driver.get(f'https://www.streetfighter.com/6/character/{character}/frame')
        vitality_element = driver.find_elements(By.CLASS_NAME, "frame_attention__6H6pd")
        removeLine = vitality_element[0].text.split("\n")
        vitality = removeLine[1]
        driver.get(f'https://www.streetfighter.com/6/character/{character}')
        desc = driver.find_elements(By.CLASS_NAME, "detail_info__item__text__JV6QL")
        
        characterDetails["name"] = character
        characterDetails["vitality"] = vitality
        characterDetails["height"] = desc[2].get_attribute("textContent")
        characterDetails["weight"] = desc[3].get_attribute("textContent")
        

        character_detail_list[character].append(characterDetails)
    return character_detail_list
    # print('ken')
    # for moveList in characterMoveList['ken']:
    #     for moveType in moveList:
    #         for moveAttributes in moveList[moveType]:
    #             removeExtras = moveAttributes[0].split("\n")
    #             moveAttributes[0] = removeExtras[0]
    #             for move in moveAttributes:
    #                 print(move)