# Desenvolva aqui sua atividade

"""
Script de extração de informações de uma fatura de energia elétrica contidas no enunciado.
Utiliza opencv para pré-processamento da imagem e preparação para OCR com tesseract.
Utiliza expressões regulares para localizar e extrair os dados solicitados.
Os dados extraídos são organizados em um DataFrame do pandas no formato "Campo | Valor".
Este dataframe é a saída final do script.
"""

import re # Biblioteca para expressões regulares (regex)
import cv2 # Biblioteca OpenCV para processamento de imagens
import pytesseract # Biblioteca para OCR (Tesseract)
import pandas as pd # Biblioteca para manipulação de dados em DataFrame

# =============================
# Funções auxiliares para extração de dados de cada campo desejado
# =============================

def extrair_texto_da_imagem(caminho_imagem: str) -> str:
    """
    Lê uma imagem, aplica pré-processamento com opencv e extrai o texto com tesseract.
    """
    imagem = cv2.imread(caminho_imagem)

    # Converte para escala de cinza para melhorar o ocr
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

    # Aplica limiarização para melhorar o ocr
    imagem_binaria = cv2.adaptiveThreshold(
        imagem_cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 11, 2
    )

    # Extrai o texto com pytesseract
    config = '--psm 6'
    texto_extraido = pytesseract.image_to_string(imagem_binaria, lang="por", config=config)

    return texto_extraido

def extrair_numero_instalacao(texto: str) -> str:
    """
    Extrai o número da instalação da unidade consumidora.
    """
    # Busca 'Instalação' no final da fatura
    # ignora sequência de 12 dígitos referentes a 'Código de Débito Automático',
    # e captura os 10 dígitos do número da instalação
    padrao = r"Instalação[^\d]*(?:\d{12}\D+)?(\d{10})"
    match = re.search(padrao, texto)
    return match.group(1) if match else None

def extrair_mes_referencia(texto: str) -> str:
    """
    Extrai o mês/ano de referência da fatura.
    """
    # Procura por 'Referente a'
    # depois procura por três letras maiúsculas (MÊS)
    # depois procura por quatro dígitos (ANO), num espaço de 100 caracteres.
    # como o ocr processou o mes com espaços entre os caracteres
    # depois de encontrado o mês, remove os espaços e retorna
    padrao = r"Referente a[\s\S]{0,100}?([A-Z](?:\s+[A-Z]){2})\s*/\s*(\d{4})"
    match = re.search(padrao, texto, re.MULTILINE)
    if match:
        mes = match.group(1).replace(' ', '')
        ano = match.group(2)
        return f"{mes}/{ano}"
    return None

def extrair_consumo_energia(texto: str) -> str:
    """
    Extrai a quantidade de energia elétrica consumida em 'Histórico de Consumo'.
    """
    # Procura pela linha com 'JUL/23' em 'Histórico de Consumo' e captura o valor numérico subsequente
    match = re.search(r"JUL\/23\s+(\d+)\s+", texto)
    return match.group(1) if match else None

def extrair_energia_compensada(texto: str) -> str:
    """
    Extrai a soma da energia compensada dos campos 'Energia compensada GD II' e 'Energia comp. adicional'.
    """
    valor_gdii = 0
    valor_adicional = 0
    # Encontra a expressão 'Energia compensada GD II kWh' e captura o valor numérico subsequente
    # no caso, o 'II' foi reconhecido como 'Il' (i minúsculo e L maiúsculo), por isso a regex foi ajustada
    match_gdii = re.search(r"Energia compensada GD Il kwh (\d+)", texto)
    if match_gdii:
        valor_gdii = int(match_gdii.group(1))
    # Faz o mesmo para 'Energia comp. adicional'
    match_adicional = re.search(r"Energia comp\. adicional kwh (\d+)", texto)
    if match_adicional:
        valor_adicional = int(match_adicional.group(1))
    # Soma ambos e retorna 
    total = valor_gdii + valor_adicional
    return str(total)

def extrair_valor_a_pagar(texto: str) -> str:
    """
    Extrai o valor total a pagar à distribuidora.
    """
    # Na sessão 'Valores Faturados' procura pelo campo 'TOTAL' (primeira ocorrência na fatura)
    match = re.search(r"TOTAL\s*R?\$?\s*([\d.,]+)", texto)
    return match.group(1) if match else None

def extrair_saldo_credito(texto: str) -> str:
    """
    Extrai o saldo de crédito de energia acumulado na sessão 'Informações Gerais'.
    """
    match = re.search(r"SALDO ATUAL DE GERAÇÃO:\s*([\d.,]+)\s*kWh", texto)
    return match.group(1) if match else None

# =============================
# Função principal
# =============================

def extrair_dados_fatura(caminho_imagem: str) -> pd.DataFrame:
    """
    Extrai todos os campos solicitados pelo enunciado da fatura contida no arquivo 'fatura.jpg'.
    """
    texto = extrair_texto_da_imagem(caminho_imagem)
    # Referência do texto extraído por ocr para debug/conferência com o arquivo fatura.jpg
    # print("===== TEXTO EXTRAÍDO DO OCR =====")
    # print(texto)
    # print("===== FIM DO TEXTO OCR =====")

    numero_instalacao = extrair_numero_instalacao(texto)
    mes_referencia = extrair_mes_referencia(texto)
    consumo_energia = extrair_consumo_energia(texto)
    energia_compensada = extrair_energia_compensada(texto)
    valor_a_pagar = extrair_valor_a_pagar(texto)
    saldo_credito = extrair_saldo_credito(texto)

    # Gera um dataframe no modelo "Campo | Valor"
    rows = [
        ("Número da Instalação", numero_instalacao or None),
        ("Mês/Ano de referência", mes_referencia or None),
        ("Energia consumida (kWh)", consumo_energia or None),
        ("Energia compensada (kWh)", energia_compensada or None),
        ("Valor a pagar (R$)", valor_a_pagar or None),
        ("Saldo de crédito (kWh)", saldo_credito or None)
    ]

    return pd.DataFrame(rows, columns=["Campo", "Valor"])

if __name__ == "__main__":
    caminho_fatura = "fatura.jpg" 
    df_resultado = extrair_dados_fatura(caminho_fatura)
    print(df_resultado.to_string(index=False))
