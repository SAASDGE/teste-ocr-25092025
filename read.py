# Desenvolva aqui sua atividade

import pytesseract
import cv2
import numpy as np
import pandas as pd
import re

def crop_img(src: str = 'fatura.jpg', dst: str = 'cropped_img.jpg', save: bool = False, startX = 0, startY = 0, endX = -1, endY = -1) -> np.ndarray:
    '''
    Função desenvolvida para cortar áreas de interesse de uma imagem, salvar como jpg e retornar um array numpy.
    Args:
        src: caminho de origem
        dst: caminho de destino
        save: true se quiser salvar as imagens recortadas, do contrário False
        startX, startY: coordenadas do vertice superior exquerdo da área a ser cortada
        endX, endY: coordenadas do vertice inferior direito da área a ser cortada
    '''
    img = cv2.imread(src)
    cropped_img = img[startY:endY, startX:endX]
    if save:
        cv2.imwrite(f'{dst}.jpg', cropped_img)
    return cropped_img 


def transcript_img(src = 'fatura.jpg', dst: str = 'fatura.txt') -> None:
    '''
    Função desenvolvida para transcrever os textos de uma imagem utilizando pytesseract.
    Args:
        src: caminho / array numpy da imagem de origem
        dst: caminho de destino
    '''
    img = src
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config=custom_config)
    with open(dst, 'a', encoding='utf-8') as file:
        file.write(text + '\n') 


def bill_summary(src: str = 'fatura.jpg', dst: str = 'fatura.txt'):
    '''
    Função desenvolvida recortar as seções de interesse de uma fatura de energia,
    realizar a transcrição das áreas recortadas e salvá-la em um arquivo .txt.
    Args:
        src: caminho da imagem de origem
        dst: caminho de destino para o texto transcrito
    '''

    #corta a imagem por áreas de interesse
    ##ajustar o parâmetro booleado para salvar as regiões e permitir sua visualização
    valores_faturados = crop_img(src, 'valores_faturados.jpg', False, 48, 862, 2436, 1764)
    rodape = crop_img(src, 'rodape.jpg', False, 500, 3070, 2284, 3290)
    infos_gerais = crop_img(src, 'infos_gerais.jpg', False, 1000, 2200, 2417, 2246)
 
    #cria o arquivo com os valores transcritos
    imgs = [valores_faturados, rodape, infos_gerais]
    for img in imgs:
        transcript_img(src=img, dst=dst)
    

def pipeline():

    '''
    Realiza o recorte e transcrição da fatura de energia e monta o dataframe com os valores determinados.
    '''

    with open('fatura.txt', 'w', encoding='utf-8') as f: ...
    bill_summary()

    values = []

    #create dataframe backbone
    df = {
        'Campo': ['Instalação', 'Mês', 'Energia consumida (kWh)', 'Energia compensada (kWh)', 'Valor a pagar à distribuidora', 'Crédito acumulado (kWh)'],
        'Valor': values
    }

    #utiliza regex para rastrear os valores-alvo
    with open('fatura.txt', 'r', encoding='utf-8') as f:
        bill = f.read()

        inst_num = re.findall(r'\b\d{10}\b', bill)[0]
        mes = re.findall(r'[A-Z]+/\d{4}', bill, re.IGNORECASE)[0]
        energ_cons_1 = re.findall(r'Energia Elétrica kWh (\d+\b)', bill, re.MULTILINE)[0]
        energ_cons_2 = re.findall(r'Energia SCEE s/ ICMS kWh (\d+\b)', bill, re.MULTILINE)[0]
        energ_cons = sum([float(re.sub(',','.', val)) for val in [energ_cons_1, energ_cons_2]])
        energ_comp_1 = re.findall(r'Energia compensada GD II kWh (\d+\b)', bill, re.MULTILINE)[0]
        energ_comp_2 = re.findall(r'Energia comp. adicional kWh (\d+\b)', bill, re.MULTILINE)[0]
        energ_comp = sum([float(re.sub(',','.', val)) for val in [energ_comp_1, energ_comp_2]])
        val_dist = re.findall(r'R\$\d+,\d+$', bill, re.MULTILINE)[0]
        credito_acumulado = re.findall(r'(\d+,\d+) kWh.', bill, re.MULTILINE)[0]

        df['Valor'] = [inst_num, mes, energ_cons, energ_comp, val_dist, credito_acumulado]
    
        df = pd.DataFrame(df)
        print(df)
        df.to_csv('table.csv', index = False)

pipeline()

