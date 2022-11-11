import pyautogui #pip install pyautogui
import pytesseract #pip install pytesseract (https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)
import cv2 #pip install opencv-python


# print(pyautogui.displayMousePosition())
# x = 1406 - 1806, y = 330 - 430

# !IMPORTANTE! caminho do tesseract dentro do computador
caminho = r"C:\Users\Mattheus.M.A\AppData\Local\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

#procura item na tela
def printaValor(img):
    posicao = pyautogui.locateOnScreen(img)
    x = posicao.left + 55 # x do dado = (x do dado - x da imagem) + x da imagem
    y = posicao.top + 265 # y = (y do dado - y da imagem) + y da imagem
    print("feito")
    screenshot = pyautogui.screenshot(region=(x, y, 27, 16))
    return screenshot
    

arr = [
    ({'id': 1, 'nome': r'C:\Users\Mattheus.M.A\Documents\Projetos\Programas\Python\Studing-python\Albion_loja\itens\tosost.png'}),
    ({'id': 2, 'nome': r'C:\Users\Mattheus.M.A\Documents\Projetos\Programas\Python\Studing-python\Albion_loja\itens\dev.png'}),
    ({'id': 3, 'nome': r'C:\Users\Mattheus.M.A\Documents\Projetos\Programas\Python\Studing-python\Albion_loja\itens\edume.png'})
]

for img in arr:
    if pyautogui.locateOnScreen(img['nome']):
        print('achei')
        screenshot = printaValor(img['nome'])
        nomeImg = f"{img['id']}.png"
        print(nomeImg)
        screenshot.save(nomeImg)

        #le os dados do print
        imagem = cv2.imread(nomeImg)
        text = pytesseract.image_to_string(imagem)
        print(text)
    else:
        print("não achei")




