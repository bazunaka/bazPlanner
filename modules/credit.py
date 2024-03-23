import math
import os

from PyQt5.QtCore import Qt

from modules import database
from modules.database import Database, DatabaseCredit


class Credit:
    def __init__(self):

        self.connection_sqlite = None
        self.connection_qtsql = None
        self.cursor = None

        self.type_calculate_credit = None

        self.sum_credit = None
        self.period_credit = None
        self.percent = None
        self.monthly_payment = None
        self.last_monthly_payment = None
        self.sum_credit_per = None
        self.overpayments = None

        self.lst_values = []

    def check_connect(self):
        self.connection_sqlite = DatabaseCredit.sqlite_open_db(DatabaseCredit.check_string_connect()["credits"])
        self.connection_qtsql = DatabaseCredit.qsql_connect_db(DatabaseCredit.check_string_connect()["credits"])
        self.cursor = self.connection_sqlite.cursor()
        if self.connection_sqlite and self.connection_qtsql:
            return True
        else:
            return False

    def set_attr(self, lst_value):
        if lst_value[0].text() == "":
            pass
        else:
            self.sum_credit = int(lst_value[0].text())

        if lst_value[4].currentIndex() == 0:
            if lst_value[1].text() != '':
                self.period_credit = int(lst_value[1].text()) * 12
            else:
                pass
        else:
            self.period_credit = int(lst_value[1].text())

        self.replaced_percent_string = lst_value[2].text().replace(',', '.')
        self.percent = float(self.replaced_percent_string)
        if lst_value[3].text() == "":
            pass
        else:
            self.monthly_payment = int(lst_value[3].text())

    def calculate_month(self, lst_value):
        self.set_attr(lst_value)
        month_per = float(self.percent / 12 / 100)
        annuity = (month_per * (1 + month_per) ** self.period_credit) / (
                (1 + month_per) ** self.period_credit - 1)
        self.monthly_payment = round(self.sum_credit * annuity, 2)
        self.sum_credit_per = round(self.monthly_payment * self.period_credit, 2)
        self.overpayments = round(self.sum_credit_per - self.sum_credit, 2)
        self.last_monthly_payment = "1"

        lst_fields = [
            {"sum_credit": self.sum_credit, "period_credit": self.period_credit, "percent": self.percent,
             "monthly_payment": self.monthly_payment, "last_monthly_payment": self.last_monthly_payment,
             "sum_credit_per": self.sum_credit_per, "overpayments": self.overpayments}
        ]

        DatabaseCredit.insert(self.connection_sqlite, lst_fields)

        last_id = DatabaseCredit.select_last_el()
        DatabaseCredit.insert_month_payments(self.connection_sqlite, self.period_credit, self.monthly_payment,
                                             last_id)

        query = DatabaseCredit.select("view_month_payments", "date_payment", "payment",
                                      where=True, where_field="id_calculation", where_value=str(last_id),
                                      order_by=False)
        model = DatabaseCredit.view_model(query)
        return model

    def calculate_date(self, lst_value):
        self.set_attr(lst_value)

        base1 = 1 + (self.percent / 1200)
        n1 = 1 - self.sum_credit * (self.percent / 1200) / self.monthly_payment

        self.period_credit = round(-math.log(n1, base1))
        self.sum_credit_per = round(self.monthly_payment * self.period_credit, 2)
        self.overpayments = round(self.sum_credit_per - self.sum_credit, 2)
        self.last_monthly_payment = "1"

        lst_fields = [
            {"sum_credit": self.sum_credit, "period_credit": self.period_credit, "percent": self.percent,
             "monthly_payment": self.monthly_payment, "last_monthly_payment": self.last_monthly_payment,
             "sum_credit_per": self.sum_credit_per, "overpayments": self.overpayments}
        ]

        DatabaseCredit.insert(self.connection_sqlite, lst_fields)

        last_id = DatabaseCredit.select_last_el()
        DatabaseCredit.insert_month_payments(self.connection_sqlite, self.period_credit, self.monthly_payment,
                                             last_id)

        query_month_payments = database.DatabaseCredit.select("*", table_name="month_payments",
                                                              where_field="id_calculation", where_value=str(last_id),
                                                              order_by=False)
        model = database.DatabaseCredit.view_model(query_month_payments)
        return model

    def calculate_max_credit(self, lst_value):
        self.set_attr(lst_value)

        count_pay = 1
        self.sum_credit = round(self.monthly_payment - self.monthly_payment * (self.percent / 100) / 12, 2)

        while count_pay < self.period_credit:
            self.sum_credit_per = round((self.monthly_payment + self.sum_credit) * (self.percent / 100) / 12, 2)
            self.sum_credit = round(self.sum_credit + (self.monthly_payment - self.sum_credit_per), 2)
            count_pay += 1

        self.sum_credit_per = round(self.monthly_payment * self.period_credit, 2)
        self.overpayments = round(self.sum_credit_per - self.sum_credit, 2)
        self.last_monthly_payment = "1"

        lst_fields = [
            {"sum_credit": self.sum_credit, "period_credit": self.period_credit, "percent": self.percent,
             "monthly_payment": self.monthly_payment, "last_monthly_payment": self.last_monthly_payment,
             "sum_credit_per": self.sum_credit_per, "overpayments": self.overpayments}
        ]

        DatabaseCredit.insert(self.connection_sqlite, lst_fields)

        last_id = DatabaseCredit.select_last_el()
        DatabaseCredit.insert_month_payments(self.connection_sqlite, self.period_credit, self.monthly_payment,
                                             last_id)

        query_month_payments = database.DatabaseCredit.select("*", table_name="month_payments",
                                                              where_field="id_calculation", where_value=str(last_id),
                                                              order_by=False)
        model = database.DatabaseCredit.view_model(query_month_payments)
        return model
