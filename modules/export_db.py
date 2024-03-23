import os

import openpyxl

from modules import database

path = os.getcwd() + "/export/"
dict_import_table = {"1": "Счета",
                     "2": "Доходы",
                     "3": "Расходы",
                     "4": "Долги",
                     "5": "Запланированные доходы",
                     "6": "Запланированные расходы"}


def export_xlsx(name_combo_text: str):
    result = database.DatabaseBank.export_data()
    book = openpyxl.Workbook()
    sheet = book.active
    i = 0
    for row in result:
        i += 1
        j = 1
        for col in row:
            cell = sheet.cell(row=i, column=j)
            cell.value = col
            j += 1

    book.save(path + name_combo_text + ".xlsx")
