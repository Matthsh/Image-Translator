import pytesseract #pip install pytesseract (corrigir installação no windows: https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)
import cv2 #pip install opencv-python

# !IMPORTANTE! caminho do tesseract dentro do computador
caminho = r"C:\Users\Mattheus.M.A\AppData\Local\Tesseract-OCR"
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

# passo 1: ler a imagem
imagem = cv2.imread("screenshot.png")

# passo 2: extrair o texto da imagem (vários formatos possiveis)
text = pytesseract.image_to_string(imagem)
# chines tradicional = chi_tra
# chines simplificado = chi_sim
# portugues = por
# japonês = jpn

print(text)