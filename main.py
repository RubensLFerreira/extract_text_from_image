import streamlit as st
import pytesseract
import cv2
from PIL import Image
import numpy as np

# Configurar o caminho do Tesseract
caminho_do_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
pytesseract.pytesseract.tesseract_cmd = caminho_do_tesseract

# Título da aplicação no Streamlit
st.title("Leitura de Texto em Imagem usando Tesseract e Streamlit")

# Carregar a imagem
imagem_carregada = st.file_uploader("Escolha uma imagem", type=["png", "jpg", "jpeg"])

if imagem_carregada is not None:
    # Carregar a imagem para exibição e processamento
    imagem = Image.open(imagem_carregada)
    st.image(imagem, caption="Imagem Carregada", use_column_width=True)

    # Converter a imagem para um formato que o Tesseract entenda (usando OpenCV)
    imagem_cv = cv2.cvtColor(np.array(imagem), cv2.COLOR_RGB2BGR)

   # passo 2: pedir pro tesseract ler texto da imagem
     texto = pytesseract.image_to_string(imagem)

   # passo 3: exibir o texto
     print(texto)
