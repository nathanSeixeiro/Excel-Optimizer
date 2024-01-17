import os
import pandas as pd

def getLocators(archive, info):
    df = pd.read_excel(archive)
    for i, row in df.iterrows():
        if pd.notna(row['TELEFONE']):
            locator = str(row['NOME']).strip()
            numberL = str(row['TELEFONE']).strip()
        else:
            locator = "N/A"
            numberL = "N/A"

        info.append({
            'Name': locator,
            'Number': numberL
        })

def printLocators(info):
    for item in info:
        print(f"\nProprietario: {item['Name']},\nNumero: {item['Number']}\n")

def main():
    archive = os.path.abspath('./spreadsheets/JOACIR ROCHA DEZEMBRO 23.xlsx')
    info = []
    getLocators(archive, info)
    printLocators(info)

main()
