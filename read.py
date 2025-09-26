# Desenvolva aqui sua atividade

import pytesseract
import pandas as pd
from PIL import Image
import re
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


#Colocando Imagem em Escala de Cinza

def imagem_cinza(imagem):
    imagem = cv2.imread(imagem)
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    return imagem_cinza

def extrair_dados(imagem):
    # Extraindo Texto com Pytesseract
    texto_extraido = pytesseract.image_to_string(imagem_cinza(imagem), config='--psm 6')

    #Extraindo Mes/Ano
    padrao_data = r"([A-Z]{3}/\d{4}) (\d{2}/\d{2}/\d{4})"
    match = re.search(padrao_data, texto_extraido)

    data = {}

    if match:
        data["Mês/Ano"] = [match.group(1)]
    else:
        data["Mês/Ano"] = [None]


    # Extraindo Instalação
    padrao_instalacao = r"Cédigo de Débito Automatico Instalagao Vencimento Total a pagar\s*\n(.*)"
    match = re.search(padrao_instalacao, texto_extraido)

    if match:
        data["Instalação"] = [match.group(1).split(" ")[2]]
    else:
        data["Instalação"] = [None]

    #Extraindo Consumo
    padrao_consumo = r"Energia kWh (.*)"
    match = re.search(padrao_consumo, texto_extraido)
    if match:
        data["Consumo"] = [match.group().split(" ")[6]]
    else:
        data["Consumo"] = [None]

    #Extraindo valor a pagar a distribuidora
    padrao_valor = r"TOTAL\s*(\d.,\d{2})"
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

    #Extraindo quantidade de energia elétrica compensada

    padrao_compensacao = r"Energia compensada GD II kWh\s*(\d+)"
    match = re.search(padrao_compensacao, texto_extraido)
    if match:
        data["Compensacao"] = [match.group().split(" ")[5]]
    else:
        data["Compensacao"] = [None]

    dataframe = pd.DataFrame(data)

    return dataframe


if __name__ == "__main__":
    df = extrair_dados('fatura.jpg')
    print(df)