import os
import pandas as pd

def read_excel_archive(archive_name):
    df = pd.read_excel(archive_name)

    # Extrair o mês a partir do nome do arquivo
    month = archive_name.split(' ')[2].capitalize()
    print(f"\nSITUAÇÃO DOS INQUILINO NO MÊS: {month}")

    # Iterar sobre as linhas do DataFrame
    for index, row in df.iterrows():
        tenat = row['LOCATÁRIO (INQUILINO)']  
        amount = round(row['VALOR BOLETO'],2) 
        situation = row['SITUAÇÃO']

        # Se a situação estiver vazia ou não for 'pago', definir como 'rever'
        situation = 'REVER' if pd.isna(situation) or situation.lower() != 'pago' else situation
       
         # Se o nome for invalido não exibir  
        if isinstance(tenat, str):
            print(f"\nLocatário: {tenat}\n Valor: {amount}\n Situação: {situation}")

    print(f"Arquivo {archive_name} lido com sucesso.")

# Caminho relativo para o arquivo na mesma pasta
archive = os.path.abspath('./JOACIR ROCHA SETEMBRO 23 - copia.xlsx')  # Obtém o caminho absoluto

read_excel_archive(archive)