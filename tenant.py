import os
import pandas as pd

def read_excel_archive(archive_name, info_tenants):
    df = pd.read_excel(archive_name)

    # Extrair o mês a partir do nome do arquivo
    month = archive_name.split(' ')[2].capitalize()
    
    # Iterar sobre as linhas do DataFrame
    for index, row in df.iterrows():
        tenant = str(row['LOCATÁRIO (INQUILINO)'])  # Convertendo para string
        amount = round(row['VALOR BOLETO'], 2) or 0   # arredondar 2 casas decimais
        transfer_amount = round(row['REPASSE FINAL'], 2) or 0  
        rent = round(row['ALUGUEL'], 2) or 0  
        iptu = round(row['IPTU'], 2) or 0  
        cond = row['CONDOMÍNIO']
        assessment_discont = round(row['MULTA / DESCONTO'],2) or 0
        consume_bills = row['CONTAS DE CONSUMO']
        adm_amount = round(row['VALOR ADM'],2)
        situation = row['SITUAÇÃO']
        water_bill = row['ÁGUA ']
        light_bill = row['LUZ']
        gas_bill = row['GÁS ']

        # Se a situação estiver vazia ou não for 'pago', definir como 'rever'
        situation = 'REVER' if pd.isna(situation) or situation.lower() != 'pago' else situation

        # Se o nome for valido e se tiver contas de consumo  

        if isinstance(tenant, str) :
           info_tenants.append({
                'Locatário': tenant,
                'Aluguel': rent,
                'Valor Boleto': amount,
                'Repasse': transfer_amount,
                'Consumo': consume_bills,
                'Condominio': cond,
                'Água': water_bill,
                'Luz': light_bill,
                'Gás': gas_bill,
                'IPTU': iptu,
                'Valor ADM': adm_amount,
                'Multa/Desconto': assessment_discont,
                'Situação': situation,
                'Mês': month
           })

def showAllRecords(info_locatarios_sorted):
    # Exibir informações ordenadas
    for info in info_locatarios_sorted:  
        print(f"\nLocatário: {info['Locatário']},\n  Aluguel: {info['Aluguel']},\n  Valor do boleto: {info['Valor Boleto']},\n  Valor Repasse: {info['Repasse']},\n  Água: {info['Água']},\n  Luz: {info['Luz']},\n  Gás:{info['Gás']},\n  Condominio: {info['Condominio']},\n  IPTU: {info['IPTU']},\n Valor ADM: {info['Valor ADM']},\n  Multa/Desconto: {info['Multa/Desconto']},\n  Situação no mês de {info['Mês']}: {info['Situação']}\n ")

def showSomeRecords(info_locatarios_sorted):
    # exibi 10 registros
    for i in range(min(150, len(info_locatarios_sorted))):
        info = info_locatarios_sorted[i]
        print(f"\nLocatário: {info['Locatário']},\n  Aluguel: {info['Aluguel']},\n  Valor do boleto: {info['Valor Boleto']},\n  Valor Repasse: {info['Repasse']},\n  Água: {info['Água']},\n  Luz: {info['Luz']},\n  Gás:{info['Gás']},\n  Condominio: {info['Condominio']},\n  IPTU: {info['IPTU']},\n Valor ADM: {info['Valor ADM']},\n  Multa/Desconto: {info['Multa/Desconto']},\n  Situação no mês de {info['Mês']}: {info['Situação']}\n ")

# Caminho relativo para o arquivo na mesma pasta
archive = os.path.abspath('./JOACIR ROCHA SETEMBRO 23 - copia.xlsx')  # Obtém o caminho absoluto

info_tenant = []

read_excel_archive(archive, info_tenant)

info_locatarios_sorted = sorted(info_tenant, key=lambda x: x['Locatário'])

showSomeRecords(info_locatarios_sorted)