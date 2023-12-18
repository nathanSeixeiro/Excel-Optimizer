import os
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
    for i in range(min(2, len(info_tenants_sorted))):
        info = info_tenants_sorted[i]
        ut.printTenants(info)


def main():
    archive = os.path.abspath('./spreadsheets/JOACIR ROCHA OUTUBRO 23.xlsx')  # Obtém o caminho absoluto
    info_tenant = []
    rd.read_excel_archive(archive, info_tenant)
    # showSomeRecords(info_tenant)
    showAllRecords(info_tenant)

main()