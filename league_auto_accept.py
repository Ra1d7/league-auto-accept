import pyautogui
from time import sleep
global accepted
global banned
global chose
accepted = False
banned = False
chose = False

def findimage(image):
    cords = pyautogui.locateOnScreen(image,confidence=0.98)
    if(cords is not None):
        return cords

def click(img):
    sleep(2)
    if(findimage(img) is not None):
        pyautogui.click(findimage(img))
def main():
    to_ban = input("what champion to ban?: ")
    to_select= input("what champion to play?: ")
    global accepted,banned,chose
    print("[+] Started Searching [+]")
    #keep searching for the accept button
    while findimage("accepted.png") is None and accepted == False:
        sleep(0.1)
        try:
            click("accept.png")
        except:
            print("cant find accept")
    accepted = True
    print("Game Started!")
    while findimage("ban_search.png") is None and banned == False:
        print(findimage("ban_search.png"))
        sleep(0.1)
    print("[+] Found Ban Button [+]")
    ban_cords = findimage("ban_search.png")
    click("ban_search.png")
    print("[+] Clicked Ban Button [+]")
    sleep(0.3)
    pyautogui.write(to_ban,interval=0.25)
    sleep(0.5)
    pyautogui.click(ban_cords[0]-378,ban_cords[1]+55)
    sleep(1)
    click("ban_button.png")
    sleep(0.5)
    print("Banned "+ to_ban + "!")
    banned = True
    print("Waiting for champ select option")
    while findimage("normal_search.png") is None and chose == False:
        sleep(0.5)
    normal_search_cords = findimage("normal_search.png")
    print("Selecting!")
    click("normal_search.png")
    sleep(0.5)
    pyautogui.write(to_select,interval=0.25)
    sleep(1)
    pyautogui.click(normal_search_cords[0]-378,normal_search_cords[1]+55)
    sleep(1)
    click("lock_button.png")
    print("Selected [{0}] And Banned [{1}]".format(to_select,to_ban))
    chose = True
if __name__ == "__main__":
    main()
