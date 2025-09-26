# Desenvolva aqui sua atividade

import pytesseract
import pandas as pd
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


imagem = Image.open('fatura.jpg')

texto_extraido = pytesseract.image_to_string(imagem)

texto = texto_extraido.split('\n')

padrao_data = r"Referente a\s+([A-Z]{3}/\d{4})"
match = re.search(padrao, texto_extraido)

data = {}

data["Mês/Ano"] = [match.group(1)]
