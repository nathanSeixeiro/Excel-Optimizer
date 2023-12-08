import os
import pandas as pd
from read_excel_archive import read_excel_archive

def printTenants(info):
    return print(f"\nLocatário: {info['Locatário']},\n  Vencimento: {info['Vencimento']},\n  Aluguel: {info['Aluguel']},\n  Valor do boleto: {info['Valor Boleto']},\n  Valor Repasse: {info['Repasse']},\n  Água: {info['Água']},\n  Luz: {info['Luz']},\n  Gás:{info['Gás']},\n  Condominio: {info['Condominio']},\n  IPTU: {info['IPTU']},\n  Valor ADM: {info['Valor ADM']},\n  Multa/Desconto: {info['Multa/Desconto']},\n  Situação no mês de {info['Mês']}: {info['Situação']}\n ")

def showAllRecords(info_locatarios_sorted):
    # Exibir informações ordenadas
    for info in info_locatarios_sorted:  
        printTenants(info)

def showSomeRecords(info_locatarios_sorted):
    # exibi num x de registros
    for i in range(min(2, len(info_locatarios_sorted))):
        info = info_locatarios_sorted[i]
        printTenants(info)

def showrRecordsWithPaymentsOk(info_locatarios):
    # exibi com situação == pago
    for i in range(len(info_locatarios)):
        info = info_locatarios[i]
        if info['Situação'] == 'PAGO':
             printTenants(info)

def sortedByName(tenants):
    tenants_sorted = sorted(tenants, key=lambda x: x['Locatário'])
    return tenants_sorted

def sortedByDate(tenants, day):
    tenants_sorted = sorted(
        [tenant for tenant in tenants if pd.notna(tenant['Vencimento']) and tenant['Vencimento'] != ''],
        key=lambda x: x['Vencimento']
    )
    filtered_tenants = [tenant for tenant in tenants_sorted if tenant['Vencimento'] == day]
    filtered_tenants_name = sortedByName(filtered_tenants)
    return filtered_tenants_name


# Caminho relativo para o arquivo na mesma pasta
# archive = os.path.abspath('./JOACIR ROCHA OUTUBRO 23 - copia.xlsx')  # Obtém o caminho absoluto
archive = os.path.abspath('./JOACIR ROCHA DEZEMBRO 23.xlsx')  # Obtém o caminho absoluto 

info_tenant = []

read_excel_archive(archive, info_tenant)

#sorted by name
# info_tenants_sorted = sortedByName(info_tenant)

#sorted by date
info_tenants_sorted = sortedByDate(info_tenant, 15.0)

showrRecordsWithPaymentsOk(info_tenants_sorted)
# showSomeRecords(info_tenants_sorted)
# showAllRecords(info_tenants_sorted)