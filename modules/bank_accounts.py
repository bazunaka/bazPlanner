from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from modules.database import DatabaseBank
from modules import bank


class BankAccount(bank.Bank):

    def __init__(self):
        super().__init__()

        self.connection_sqlite = None
        self.connection_qtsql = None
        self.cursor = None

        self.name_bank = None
        self.name_type_bank_acc = None
        self.summary = None
        self.is_active = None

        self.lst_values = []
        self.check_connect()

    def check_connect(self):
        self.connection_sqlite = DatabaseBank.sqlite_open_db(DatabaseBank.check_string_connect()["banks"])
        self.connection_qtsql = DatabaseBank.qsql_connect_db(DatabaseBank.check_string_connect()["banks"])
        self.cursor = self.connection_sqlite.cursor()
        if self.connection_sqlite and self.connection_qtsql:
            return True
        else:
            return False

    @staticmethod
    def delete_bank_acc(value: str) -> bool:
        name_table = "bank_accounts"
        name_column = "name_bank_acc"
        DatabaseBank.delete_from_table(name_table, name_column, value)
        return True
