import pyautogui
import time


#mostra os atalhos
pyautogui.KEYBOARD_KEYS

#Mostra um alerta na tela 
pyautogui.alert("A execução vai começar, não mecha no seu mouse ou teclado durante a execução.")

# Cada comando espera 0.5 segundos para executar após o anterios
pyautogui.PAUSE = 0.5

#preciona a tecla selecionada
pyautogui.press('win')

# espera o tempo indicado antes do proximo comando
time.sleep(1)

# preciona um comando como "windows + d" por exemplo
pyautogui.hotkey('win', 'd')

# mostra a posição atual do mouse
pyautogui.position()

#move o mouse até a posição
pyautogui.moveTo(x, y)

#preciona o botão do mouse
pyautogui.mouseDown()

# despreciona o botão do mouse
pyautogui.mouseUp()