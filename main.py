import pyautogui
import time
import easyocr
from PIL import Image
import re

##### WARNING: DONT USE THIS FOR REAL GAMBLING, AS THIS ISNT 100% ITS JUST A STRAT
##### THIS IS ALSO BASED OF A FRIENDS STRAT TRANLATED INTO PYTHON SO TAKE THE RESULTS WITH A 
##### GRAIN OF SALT

def advise(player_cards, dealer_upcard):
    player_sum = sum([10 if card in ['J', 'Q', 'K'] else int(card) for card in player_cards])
    has_ace = 'A' in player_cards

    if not any(isinstance(item, str) and any(char.isdigit() for char in item) for item in player_cards) or any(isinstance(item, str) and any(char.isdigit() for char in item) for item in dealer_upcard):
        return "SOMETHING WENT WRONG, PLEASE REFER TO JUDGEMENT!"

    if has_ace:
        player_sum += 10

    if player_sum >= 17: ## basic card counting, any real human could do this with intoition, but were here to not play this game for long soooooo
        return "Stand"
    elif player_sum in [13, 14, 15, 16] and dealer_upcard in ['2', '3', '4', '5', '6']:
        return "Stand"
    elif player_sum in [12] and dealer_upcard in ['4', '5', '6']:
        return "Stand"
    elif player_sum in [18, 19, 20, 21]:
        return "Stand"
    elif player_sum in [9] and dealer_upcard in ['3', '4', '5', '6']:
        return "Double if allowed, otherwise Hit"
    elif player_sum in [10] and dealer_upcard not in ['10', 'J', 'Q', 'K', 'A']:
        return "Double if allowed, otherwise Hit"
    elif player_sum in [11] and dealer_upcard != 'A':
        return "Double if allowed, otherwise Hit"
    else:
        return "Hit"
    
def ss(fileName,XCords,YCords,Width,Height): ## screen shot so the image prossexxing can see section of screen the card numbers are
    global width
    global height
    # Specify the coordinates (x, y) for the screenshot
    x_coordinate = XCords
    y_coordinate = YCords

    # Set the width and height for the screenshot
    width = Width
    height = Height

    # Take a screenshot of the specified coordinates
    screenshot = pyautogui.screenshot(region=(x_coordinate, y_coordinate, width, height))

    # Save the screenshot to a file
    screenshot.save(fileName)

while True:
    ##### POSITION ARE HARDCODED, WORKS BEST ON STANDERED 1080P, HOWL.GG BACKJACK, NOT FULLSCREEN

    ### get delaers cards

    time.sleep(2) # no real point of this becuaee image proccessing takes around about that timne so could remove in future.
    ss("DealersCards.png",1200,275,1000,30)
    reader = easyocr.Reader(['en'])
    DealersTotal = reader.readtext(r"C:\Users\Spen\Desktop\gambling\DealersCards.png") ### NEED TO CHANGE PER USER, PYTHON BEING RETARED
    cleanDealers = re.findall(r"'(\d+(?:\.\d+)?)'", str(DealersTotal))

    ### get players cards
    
    ss("PlayersCards.png",1200,550,1000,40) 
    ### IMAGE REC WASNT READING TEXT PROPERLY, SO I HAD TO DO THIS SHIT AHHHHHHHHHHHHHHHHHHH
    ### im the future ill use a ai model to see and detect cards instead of this position shit but this will have to do
    reader = easyocr.Reader(['en'])
    PlayersTotal = reader.readtext(r"C:\Users\Spen\Desktop\gambling\PlayersCards.png") ### SAME AS PREVIOUS
    print(PlayersTotal)
    strPlayer = str(PlayersTotal) ### need to clean up string, becuaseeee this lib is a fucking pain in the ass
    firstCleanPlayers = strPlayer.replace("YOU HAVE A ", "") ### such a bad way to do this. idc tho
    print(firstCleanPlayers)
    cleanPlayers = re.findall(r"'(\d+(?:\.\d+)?)'", str(firstCleanPlayers))
    print(cleanPlayers)

    player_cards = cleanPlayers
    dealer_upcard = cleanDealers
    advice = advise(player_cards, dealer_upcard)
    print(f"Advice: {advice}") ### im so tired, tmr ill make it click the buttons on the website using, uh https, keyboard input or somthing i really havent looked into it 


    ### Remember, the house always wins
