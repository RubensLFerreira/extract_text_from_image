import pytesseract
import cv2

# https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i

# passo 1: ler a imagem
imagem = cv2.imread('imagem_texto.png')

# Corrigir o caminho do Tesseract
caminho = r"" # Colocar o caminho do Tesseract

# Configurar o executável do Tesseract
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"

# passo 2: pedir pro tesseract ler texto da imagem
texto = pytesseract.image_to_string(imagem)

# passo 3: exibir o texto
print(texto)
