import pyautogui
from time import sleep

def findimage(image):
    cords = pyautogui.locateOnScreen(image)
    if(cords is not None):
        return cords

def click(img):
    sleep(2)
    global brek
    if(findimage(img) is not None):
        pyautogui.click(findimage(img))
def main():
    to_ban = input("what champion to ban?: ")
    to_select= input("what champion to play?: ")
    global brek
    print("[+] Started Searching [+]")
    #keep searching for the accept button
    while findimage("accepted.png") is None:
        sleep(0.1)
        try:
            click("accept.png")
        except:
            print("cant find accept")
    print("Game Started!")
    while findimage("ban_search.png") is None:
        sleep(0.1)
    ban_cords = findimage("ban_search.png")
    click("ban_search.png")
    sleep(0.3)
    pyautogui.write(to_ban,interval=0.25)
    sleep(0.5)
    pyautogui.click(ban_cords[0]-382,ban_cords[1]+55)
    sleep(1)
    click("ban_button.png")
    sleep(0.5)
    print("Banned "+ to_ban + "!")
    print("Waiting for champ select option")
    while findimage("normal_search.png") is None:
        sleep(0.5)
    normal_search_cords = findimage("normal_search.png")
    print("Selecting!")
    click("normal_search.png")
    sleep(0.5)
    pyautogui.write(to_select,interval=0.25)
    sleep(1)
    pyautogui.click(normal_search_cords[0]-382,normal_search_cords[1]+55)
    sleep(1)
    click("lock_button.png")
    print("Selected [{0}] And Banned [{1}]".format(to_select,to_ban))
if __name__ == "__main__":
    main()
