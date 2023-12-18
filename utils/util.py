import pandas as pd

def printTenants(info):
    return print(f"\nLocatário: {info['Locatário']},\n  Vencimento: {info['Vencimento']},\n  Aluguel: {info['Aluguel']},\n  Valor do boleto: {info['Valor Boleto']},\n  Valor Repasse: {info['Repasse']},\n  Água: {info['Água']},\n  Luz: {info['Luz']},\n  Gás:{info['Gás']},\n  Condominio: {info['Condominio']},\n  IPTU: {info['IPTU']},\n  Valor ADM: {info['Valor ADM']},\n  Multa/Desconto: {info['Multa/Desconto']},\n  Situação no mês de {info['Mês']}: {info['Situação']}\n ")

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

def showThisMonth(tenants):
    tenants_sorted = sorted(
        [tenant for tenant in tenants if pd.notna(tenant['Vencimento']) and tenant['Vencimento'] != ''],
        key=lambda x: x['Vencimento']
    )
    return tenants_sorted