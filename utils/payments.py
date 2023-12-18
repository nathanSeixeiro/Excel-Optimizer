import os
import util as ut
import read_excel as rd

def showrRecordsWithPaymentsOk(info_locatarios):
    for i in range(len(info_locatarios)):
        info = info_locatarios[i]
        if info['Situação'] == 'PAGO':
            ut.printTenants(info)

def choseFunc(op, tenants):
    if op == 1:
        info_tenants_sorted = ut.sortedByDate(tenants, 20.0)
    else:
        info_tenants_sorted = ut.showThisMonth(tenants)    
    return info_tenants_sorted

def main():
    archive = os.path.abspath('./spreadsheets/JOACIR ROCHA DEZEMBRO 23.xlsx') 
    info_tenant = []
    rd.read_excel_archive(archive, info_tenant)
    info_tenants_sorted = choseFunc(2, info_tenant)
    showrRecordsWithPaymentsOk(info_tenants_sorted)

main()