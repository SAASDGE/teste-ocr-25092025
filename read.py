# Desenvolva aqui sua atividade

import pytesseract
import pandas as pd
from PIL import Image
import re

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


imagem = Image.open('fatura.jpg')
# Extraindo Texto com Pytesseract
texto_extraido = pytesseract.image_to_string(imagem)

#Extraindo Mes/Ano
padrao_data = r"Referente a\s+([A-Z]{3}/\d{4})"
match = re.search(padrao_data, texto_extraido)

data = {}

if match:
    data["Mês/Ano"] = [match.group(1)]
else:
    data["Mês/Ano"] = [None]


# Extraindo Instalação
padrao_instalacao = r"N° DA INSTALAGAO\s+(\d+)"
match = re.search(padrao_instalacao, texto_extraido)
if match:
    data["Instalação"] = [match.group(1)]
else:
    data["Instalação"] = [None]

#Extraindo Consumo
padrao_consumo = r"Energia kWh (.*)"
match = re.search(padrao_consumo, texto_extraido)
if match:
    data["Consumo"] = [match.group().split(" ")[3]]
else:
    data["Consumo"] = [None]

#Extraindo valor a pagar a distribuidora
padrao_valor = r"Total a pagar\s*R\$\s*(\d.,\d{2})"
match = re.search(padrao_valor, texto_extraido)
if match:
    data["Valor"] = [match.group(1)]
else:
    data["Valor"] = [None]

#Extraindo saldo atual de geracao
padrao_saldo = r"SALDO ATUAL DE GERAGAO:\s*([\d]+,[\d]+) kWh."
match = re.search(padrao_saldo, texto_extraido)
if match:
    saldo_atual = match.group().split(" ")[4]
    data["Saldo"] = [saldo_atual]
else:
    saldo_atual = None





print(data)
