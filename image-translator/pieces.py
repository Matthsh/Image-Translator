import pyautogui #pip install pyautogui
import keyboard #pip install keyboard
from googletrans import Translator #pip install googletrans==4.0.0-rc1  
import pytesseract #pip install pytesseract (https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)
import cv2 #pip install opencv-python
import time

pyautogui.hotkey('alt', 'tab')
nextprint = keyboard.wait('enter')
result = False

while True:
    time.sleep(0.5)
    screenshot = pyautogui.screenshot(region=(660, 660, 890, 150))
    screenshot.save('screenshot.png')
    keyboard.wait('enter')


    #while keyboard.is_pressed('w') == True:
        #pyautogui.mouseDown()
        #pyautogui.mouseUp()
        
        

        #text3 = "よろしく お 願い します"

        #translator = Translator()
        #result = translator.translate(text3, src='ch', dest='pt')
        #print(result.text)

        # x: 660, 1550 y:660, 760