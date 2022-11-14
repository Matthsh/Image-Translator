import pyautogui
import keyboard

print("you can click")
while True:
    if keyboard.is_pressed('w') == True:
        pyautogui.mouseDown()
        pyautogui.mouseUp()