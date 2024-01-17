import os
import pandas as pd
import util as ut
import read_excel as rd

def showAllRecords(info_tenants):
    info_tenants_sorted = ut.sortedByName(info_tenants)
    # Exibir informações ordenadas
    for info in info_tenants_sorted:  
        ut.printTenants(info)

def showSomeRecords(info_tenants):
    info_tenants_sorted = ut.sortedByName(info_tenants)
    # exibi num x de registros
    for i in range(min(20, len(info_tenants_sorted))):
        info = info_tenants_sorted[i]
        ut.printTenants(info)

def printTenantsNames(info_tenants):
    info_tenants_sorted = ut.sortedByName(info_tenants)
    for info in info_tenants_sorted: 
        if isinstance(info['Locatário'], str) and not pd.isna(info):
            print(f"Locatário: {info['Locatário']}\n")

def main():
    archive = os.path.abspath('./spreadsheets/JOACIR ROCHA JANEIRO 24.xlsx')  # Obtém o caminho absoluto
    info_tenant = []
    rd.read_excel_archive(archive, info_tenant)
    # showSomeRecords(info_tenant)
    # showAllRecords(info_tenant)
    printTenantsNames(info_tenant)

main()