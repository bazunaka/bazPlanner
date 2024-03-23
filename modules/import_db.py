
from modules import database


def import_xlsx(name_directory, cmb_index):
    # wb = load_workbook(os.getcwd() + "/import/bank_accounts.xlsx")
    # sheet = wb.active
    # for row in range(2, sheet.max_row + 1):
    #     data = []
    #     data_dict = {"id_bank": "",
    #                  "id_type": "",
    #                  "name_bank_acc": "",
    #                  "summary": "",
    #                  "create_date": "",
    #                  "isActive": ""}
    #     for col in range(1, sheet.max_column + 1):
    #         value = sheet.cell(row=row, column=col).value
    #         data.append(str(value))
    #     d = dict(zip(data_dict.keys(), data))
    #     add_record(d)
    new_name_dir = name_directory.split("/")[-1]
    print(new_name_dir, cmb_index)


def add_record(data):
    lst_fields = [
        data
    ]

    database.DatabaseBank.insert(lst_fields, table_name="bank_accounts")
