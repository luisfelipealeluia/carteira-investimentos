from openpyxl import Workbook
from openpyxl.worksheet.table import Table
import pandas as pd
import os

def create_table(data):
    
    wb = Workbook()
    ws = wb.active
    
    ws.append(["Ativo", "Código", "Moeda", "Total"]) # nome das colunas
    
    for row in data:
        ws.append(row)
        
    # cria uma tabela com nome Portfolio
    tab = Table(displayName="Portfolio", ref=f"A1:D{len(data)+1}")
    ws.add_table(tab)
    
    wb.save(os.path.join(os.path.dirname(os.getcwd()), "excel", "portfolio.xlsx"))


def insert_images():

    df = pd.read_excel(os.path.join(os.path.dirname(os.getcwd()), "excel", "portfolio.xlsx"))
    writer = pd.ExcelWriter('portfolio.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Portfolio')

    workbook  = writer.book
    worksheet = writer.sheets['Portfolio']

    worksheet.insert_image('B10', '../temp/qrcode.png')
    worksheet.insert_image('H3', '../temp/barplot.png')
    worksheet.insert_image('R3', '../temp/boxplot.png')
    worksheet.insert_image('AB3', '../temp/pieplot.png')

    writer.save()

if __name__ == "__main__":

    insert_images()