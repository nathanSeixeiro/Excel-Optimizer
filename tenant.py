import os
import pandas as pd

def read_excel_archive(archive_name, info_tenants):
    df = pd.read_excel(archive_name)

    # Extrair o mês a partir do nome do arquivo
    month = archive_name.split(' ')[2].capitalize()
    
    # Iterar sobre as linhas do DataFrame
    for index, row in df.iterrows():
        tenant = str(row['LOCATÁRIO (INQUILINO)'])  # Convertendo para string
        # amount = round(row['VALOR BOLETO'], 2) or 0   # arredondar 2 casas decimais
        amount = row['VALOR BOLETO'] or 0   # arredondar 2 casas decimais
        transfer_amount = row['REPASSE FINAL'] or 0  
        rent = row['ALUGUEL'] or 0  
        iptu = row['IPTU'] or 0  
        cond = row['CONDOMÍNIO']
        assessment_discont = row['MULTA / DESCONTO'] or 0.0
        consume_bills = row['CONTAS DE CONSUMO']
        adm_amount = row['VALOR ADM'] or 0.0 
        situation = row['SITUAÇÃO'] or 0.0
        water_bill = row['ÁGUA '] or 0.0
        light_bill = row['LUZ'] or 0.0
        gas_bill = row['GÁS '] or 0.0

        # Se a situação estiver vazia ou não for 'pago', definir como 'rever'
        situation = 'REVER' if pd.isna(situation) or situation.lower() != 'pago' else situation

        roundIfIsNan(amount)
        roundIfIsNan(transfer_amount)
        roundIfIsNan(rent)
        roundIfIsNan(iptu)
        roundIfIsNan(cond)
        roundIfIsNan(assessment_discont)
        roundIfIsNan(adm_amount)

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

def roundIfIsNan(value):
    if pd.isna(value):
        value = 0
    else:
        round(value,2)

def showAllRecords(info_locatarios_sorted):
    # Exibir informações ordenadas
    for info in info_locatarios_sorted:  
        print(f"\nLocatário: {info['Locatário']},\n  Aluguel: {info['Aluguel']},\n  Valor do boleto: {info['Valor Boleto']},\n  Valor Repasse: {info['Repasse']},\n  Água: {info['Água']},\n  Luz: {info['Luz']},\n  Gás:{info['Gás']},\n  Condominio: {info['Condominio']},\n  IPTU: {info['IPTU']},\n Valor ADM: {info['Valor ADM']},\n  Multa/Desconto: {info['Multa/Desconto']},\n  Situação no mês de {info['Mês']}: {info['Situação']}\n ")

def showSomeRecords(info_locatarios_sorted):
    # exibi 10 registros
    for i in range(min(10, len(info_locatarios_sorted))):
        info = info_locatarios_sorted[i]
        print(f"\nLocatário: {info['Locatário']},\n  Aluguel: {info['Aluguel']},\n  Valor do boleto: {info['Valor Boleto']},\n  Valor Repasse: {info['Repasse']},\n  Água: {info['Água']},\n  Luz: {info['Luz']},\n  Gás:{info['Gás']},\n  Condominio: {info['Condominio']},\n  IPTU: {info['IPTU']},\n Valor ADM: {info['Valor ADM']},\n  Multa/Desconto: {info['Multa/Desconto']},\n  Situação no mês de {info['Mês']}: {info['Situação']}\n ")

# Caminho relativo para o arquivo na mesma pasta
archive = os.path.abspath('./JOACIR ROCHA OUTUBRO 23 - copia.xlsx')  # Obtém o caminho absoluto

info_tenant = []

read_excel_archive(archive, info_tenant)

info_locatarios_sorted = sorted(info_tenant, key=lambda x: x['Locatário'])

showSomeRecords(info_locatarios_sorted)
# showAllRecords(info_locatarios_sorted)