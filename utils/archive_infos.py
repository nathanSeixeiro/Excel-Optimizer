import os
import pandas as pd

def mostrar_info_arquivo(nome_arquivo):
    df = pd.read_excel(nome_arquivo)

  # Extrair o mês a partir do nome do arquivo
    mes = nome_arquivo.split(' ')[2].capitalize()
    print(f"Situação no mes : {mes}")

    print(f"Nomes das colunas: {df.columns}")

    print(f"\nPrimeiras linhas do DataFrame:\n{df.head()}")

# Caminho relativo para o arquivo na mesma pasta
# arquivo = os.path.abspath('./JOACIR ROCHA OUTUBRO 23 - copia.xlsx')  
arquivo = os.path.abspath('./spreadsheets/JOACIR ROCHA DEZEMBRO 23.xlsx')  # Obtém o caminho absoluto
mostrar_info_arquivo(arquivo)