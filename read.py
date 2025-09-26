import cv2
import easyocr
import re
import pandas as pd

# --- EXTRAÇÃO DE TEXTO DA IMAGEM COM EASYOCR ---

def extrair_texto(caminho_imagem):
    print("\nIniciando o leitor EasyOCR...")
    reader = easyocr.Reader(['pt'])
    
    try:
        imagem = cv2.imread(caminho_imagem)
        imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        resultados = reader.readtext(imagem_cinza, paragraph=False)
        texto_completo = ''
        for (bbox, texto, prob) in resultados:
            texto_completo += texto + ' '

        return texto_completo

    except Exception as e:
        print(f"\nErro ao processar a imagem: {e}")
        return None

# --- ANÁLISE DO TEXTO E EXTRAÇÃO DOS DADOS ---

def extrair_dados(texto):
    dados = {
        "numero_instalacao": None,
        "mes_referencia": None,
        "energia_consumida_kwh": None,
        "energia_compensada_kwh": None,
        "valor_a_pagar_rs": None,
        "saldo_credito_kwh": None
    }

    # 1. Número da Instalação
    match = re.search(r"\d{11}\s+(\d{10})", texto)
    if match:
        dados["numero_instalacao"] = match.group(1)

    # 2. Mês/Ano de Referência
    match = re.search(r"Referente a .*? ([A-Z]+\d{4})", texto)
    if match:
        dados["mes_referencia"] = match.group(1)
        dados["mes_referencia"] = dados["mes_referencia"].replace('I', '/')


    # 3. Quantidade de Energia Elétrica Consumida (kWh)
    match = re.search(r"JULI23 (\d+)", texto)
    if match:
        dados["energia_consumida_kwh"] = match.group(1)

    # 4. Quantidade de Energia Elétrica Compensada (kWh)
    match = re.search(r"Energia compensada GD II kWh (\d+)", texto)
    if match:
        dados["energia_compensada_kwh"] = match.group(1)

    # 5. Valor a Pagar (R$)
    match = re.search(r"Total a pagar .*? R\$([\d,]+)", texto)
    if match:
        dados["valor_a_pagar_rs"] = match.group(1)

    # 6. Saldo de Crédito de Energia (kWh)
    match = re.search(r"SALDO ATUAL DE GERAÇÃO: ([\d,]+)", texto)
    if match:
        dados["saldo_credito_kwh"] = match.group(1)

    return dados


# --- FUNÇÃO PRINCIPAL ---
def main():
    caminho_fatura = 'fatura.jpg'
    texto_completo = extrair_texto(caminho_fatura)

    if texto_completo:
        print("\n--- TEXTO EXTRAÍDO COM SUCESSO! ---")

        dados_fatura = extrair_dados(texto_completo)

        lista_para_df = [
            {'Campo': 'Número da Instalação', 'Valor': dados_fatura['numero_instalacao']},
            {'Campo': 'Mês/Ano', 'Valor': dados_fatura['mes_referencia']},
            {'Campo': 'Energia Consumida (kWh)', 'Valor': dados_fatura['energia_consumida_kwh']},
            {'Campo': 'Energia Compensada (kWh)', 'Valor': dados_fatura['energia_compensada_kwh']},
            {'Campo': 'Valor a Pagar (R$)', 'Valor': dados_fatura['valor_a_pagar_rs']},
            {'Campo': 'Saldo de Crédito (kWh)', 'Valor': dados_fatura['saldo_credito_kwh']}
        ]

        df_resultado = pd.DataFrame(lista_para_df)

        print("\n--- INFORMAÇÕES DA FATURA ---")
        print(df_resultado)
        print("------------------------------------------")
    
    else:
        print("\nNão foi possível extrair o texto da fatura.")

if __name__ == "__main__":
    main()