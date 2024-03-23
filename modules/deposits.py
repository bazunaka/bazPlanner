import datetime
import os
import calendar

from PyQt5.QtCore import Qt

from modules import database


class Deposits:
    def __init__(self):
        self.connection_sqlite = database.Database.sqlite_open_db(os.getcwd() + "/databases/deposits.db")
        self.connection_qtsql = database.Database.qsql_connect_db(os.getcwd() + "/databases/deposits.db")
        self.cursor = self.connection_sqlite.cursor()

        self.sum_deposit = None
        self.period_deposit = None
        self.start_date = None
        self.percent_deposit = None
        self.sum_percent = None
        self.total_sum = None
        self.is_capitalization = None
        self.is_replenishment = None
        self.period_payment = None

        self.lst_values = []

    def set_attr(self, lst_value):
        self.sum_deposit = lst_value[0].text()
        self.percent_deposit = lst_value[1].text().replace(',', '.')
        self.period_deposit = lst_value[2].text()
        self.start_date = lst_value[3].text()

        self.sum_percent = self.calculate_percent()
        self.total_sum = self.calculate_sum_percent()

        self.is_capitalization = lst_value[4].checkState()
        self.is_replenishment = lst_value[5].checkState()

        print(self.is_capitalization)
        print(self.is_replenishment)

    @staticmethod
    def days_in_year():
        current_year = datetime.datetime.now().year
        return 366 if calendar.isleap(int(current_year)) else 365

    def calculate_percent(self):
        self.sum_percent = round((int(self.sum_deposit) * float(self.percent_deposit) * int(self.period_deposit) / self.days_in_year()) / 100, 2)
        return self.sum_percent

    def calculate_sum_percent(self):
        self.total_sum = round(float(self.calculate_percent()) + int(self.sum_deposit), 2)
        return self.total_sum

    @staticmethod
    def insert_into_db(connection, values):
        database.DatabaseDeposits.insert(connection, values)

    @staticmethod
    def select_deposit(connection):
        query = database.DatabaseDeposits.select("view_calculate_deposits", "*", where=False, order_by=False)
        model = database.DatabaseDeposits.view_model(connection, query)
        return model

    def calculate_deposit(self, lst_value):
        self.set_attr(lst_value)

        lst_fields = [{
            "sum_deposit": self.sum_deposit, "period_deposit": self.period_deposit, "start_date": self.start_date,
            "percent_deposit": self.percent_deposit, "sum_percent": self.sum_percent, "total_sum": self.total_sum,
            "is_capitalization": self.is_capitalization, "is_replenishment": self.is_replenishment,
            "period_payment": self.period_payment
        }]

        lst_headers = ["Сумма вклада", "Срок вклада", "Дата начала", "Процентная ставка", "Сумма процентов",
                            "Общая сумма"]

        self.insert_into_db(self.connection_sqlite, lst_fields)
        model = self.select_deposit(self.connection_qtsql)
        for i in range(6):
            model.setHeaderData(i, Qt.Orientation.Horizontal, lst_headers[i])
            i += 1
        return model
