# Desenvolva aqui sua atividade

import pytesseract
import pandas as pd
import re
import cv2

"""
Teste Técnico 2 - Extração de informações
Autor : Mateus Mendes da Silva
Data : 26/09/2025
"""

#Configurando Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'


#Colocando Imagem em Escala de Cinza
def imagem_cinza(imagem):
    try:
            
        imagem = cv2.imread(imagem)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        return imagem_cinza
    
    except Exception as e:
        print(f"Erro ao ler a imagem: {e}")
        return None

def extrair_dados(imagem):
    # Extraindo Texto com Pytesseract
    try:
        texto_extraido = pytesseract.image_to_string(imagem_cinza(imagem), config='--psm 6')
    except Exception as e:
        print(f"Erro ao extrair o texto: {e}")
        return None


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
        data["Saldo de Geracao"] = [saldo_atual]
    else:
        saldo_atual = None

    #Extraindo quantidade de energia elétrica compensada

    padrao_compensacao = r"Energia compensada GD II kWh\s*(\d+)"
    match = re.search(padrao_compensacao, texto_extraido)
    if match:
        data["Energia Compensada"] = [match.group().split(" ")[5]]
    else:
        data["Energia Compensada"] = [None]

    #Criando DataFrame
    dataframe = pd.DataFrame(data)
    return dataframe


if __name__ == "__main__":

    imagem = './fatura.jpg'
    df = extrair_dados(imagem)
    # Coloca o dataframe na vertical como no enunciado do teste
    vertical_df = df.T.reset_index()
    vertical_df.columns = ["Campo", "Valor"]

    print(vertical_df)