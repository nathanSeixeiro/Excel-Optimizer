import os
import pandas as pd

locatarios = {}

def ler_arquivo_excel(nome_arquivo):
    df = pd.read_excel(nome_arquivo)

    # Extrair o mês a partir do nome do arquivo
    mes = nome_arquivo.split(' ')[2].capitalize()
    print(f"\nSITUAÇÃO DOS INQUILINO NO MÊS: {mes}")

    # Iterar sobre as linhas do DataFrame
    for index, row in df.iterrows():
        locatario = row['LOCATÁRIO (INQUILINO)']  
        valor_boleto = round(row['VALOR BOLETO'],2) 
        situacao = row['SITUAÇÃO']

        # Se a situação estiver vazia ou não for 'pago', definir como 'rever'
        situacao = 'REVER' if pd.isna(situacao) or situacao.lower() != 'pago' else situacao
       
         # Se o nome for invalido não exibir  
        if isinstance(locatario, str):
            print(f"\nLocatário: {locatario}\n Valor: {valor_boleto}\n Situação: {situacao}")

    print(f"Arquivo {nome_arquivo} lido com sucesso.")

# Caminho relativo para o arquivo na mesma pasta
arquivo = './JOACIR ROCHA SETEMBRO 23 - copia.xlsx'
arquivo_path = os.path.abspath(arquivo)  # Obtém o caminho absoluto

ler_arquivo_excel(arquivo_path)