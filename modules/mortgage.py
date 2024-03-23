import os

from modules import database


class Mortgage:

    def __init__(self):
        self.connection_qtsql = database.Database.qsql_connect_db(os.getcwd() + "/databases/mortgage.db")
        self.connection_sqlite = database.Database.sqlite_open_db(os.getcwd() + "/databases/mortgage.db")
        self.cursor = self.connection_sqlite.cursor()

        self.property_value = None
        self.initial_payment = None
        self.sum_credit = None
        self.period_credit = None
        self.percent = None
        self.monthly_payment = None
        self.last_monthly_payment = None
        self.sum_credit_per = None
        self.overpayments = None

        self.date_payment = None

        self.lst_values = []

    def set_attr(self, lst_value):
        self.property_value = int(lst_value[0].text())
        self.initial_payment = int(lst_value[1].text())
        self.sum_credit = int(lst_value[0].text()) - int(lst_value[1].text())
        lst_value[2].setText(str(self.sum_credit))
        replaced_percent_string = lst_value[4].text().replace(',', '.')
        self.percent = float(replaced_percent_string)

        if lst_value[5].currentIndex() == 0:
            self.period_credit = int(lst_value[3].text()) * 12
        else:
            self.period_credit = int(lst_value[3].text())

    def calculate_mortgage(self, lst_value):
        self.set_attr(lst_value)
        monthly_percent = float(self.percent / 12 / 100)
        annuity = (monthly_percent * (1 + monthly_percent) ** self.period_credit) / (
                (1 + monthly_percent) ** self.period_credit - 1)
        self.monthly_payment = round(self.sum_credit * annuity, 2)
        self.sum_credit_per = round(self.monthly_payment * self.period_credit, 2)
        self.overpayments = round(self.sum_credit_per - self.sum_credit, 2)
        self.last_monthly_payment = "1"

        self.lst_values = [
            {"property_value": self.property_value, "initial_payment": self.initial_payment, "sum_credit": self.sum_credit,
             "period_credit": self.period_credit, "percent": self.percent, "monthly_payment": self.monthly_payment,
             "last_monthly_payment": self.last_monthly_payment, "sum_credit_per": self.sum_credit_per,
             "overpayments": self.overpayments}
        ]

        database.DatabaseMortgage.insert(self.connection_sqlite, self.lst_values)
        query = database.DatabaseMortgage.select("calculation_monthly_payment", "id_calc_mortgage",
                                               where=False, order_field="id_calc_mortgage", order_value="DESC")

        last_id = database.DatabaseCredit.select_last_el(self.connection_sqlite, query)
        database.DatabaseCredit.insert_month_payments(self.connection_sqlite, self.period_credit, self.monthly_payment,
                                                      last_id)
        model = database.Database.select_all_from_tables_where(self.connection_qtsql, table_name="month_payments",
                                                               column_name="id_calculation", condition=str(last_id))
        return model
