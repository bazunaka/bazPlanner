
import os
import sqlite3
from functools import partial

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIntValidator, QDoubleValidator

from modules import credit
from forms import ui_MainWindow


class Ui_WindowCreditCalc(QtWidgets.QWidget):
    count = 0

    def __init__(self, parent=None):

        super(Ui_WindowCreditCalc, self).__init__(parent)

        self.lst_credit = ["Расчет ежемесячного платежа", "Расчет срока кредита", "Расчет максимальной суммы кредита"]
        self.lst_period = ["лет", "месяцев"]

        self.label_type_credit = QtWidgets.QLabel("Выберите тип расчета")
        self.label_credit_date_sum = QtWidgets.QLabel()
        self.label_sum_credit = QtWidgets.QLabel("Сумма кредита")
        self.label_date_credit = QtWidgets.QLabel("Срок кредита")
        self.label_per_credit = QtWidgets.QLabel("Процентная ставка")
        self.label_payment = QtWidgets.QLabel("Ежемесячный платеж")

        self.edit_sum_credit = QtWidgets.QLineEdit()
        self.edit_period_credit = QtWidgets.QLineEdit()
        self.edit_percent_credit = QtWidgets.QLineEdit()
        self.edit_payment = QtWidgets.QLineEdit()

        self.edit_sum_credit.setValidator(QIntValidator(1000, 100000000))
        self.edit_period_credit.setValidator(QIntValidator(1, 360))
        self.edit_percent_credit.setValidator(QDoubleValidator(1.0, 49.9, 2))
        self.edit_payment.setValidator(QDoubleValidator(500.0, 500000.0, 2))

        self.combobox_type_credit = QtWidgets.QComboBox()
        self.combobox_period_credit = QtWidgets.QComboBox()

        self.button_calculate1 = QtWidgets.QPushButton("Рассчитать")
        self.button_calculate2 = QtWidgets.QPushButton("Рассчитать")
        self.button_calculate3 = QtWidgets.QPushButton("Рассчитать")

        self.table_view_calculating = QtWidgets.QTableView()

        self.grid = QtWidgets.QGridLayout()
        self.credit_window = QtWidgets.QWidget()

        self.connection = sqlite3.connect(
            os.getcwd() + "/databases/credits.db")
        self.cursor = self.connection.cursor()

        self.credit = credit.Credit()

    def select_item(self, cmb_index):
        if cmb_index == 0:
            self.clean_widgets()

            self.grid.addWidget(self.label_type_credit, 0, 0, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.combobox_type_credit, 0, 1, 1, 2, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.label_sum_credit, 1, 0, 1, 1, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.edit_sum_credit, 1, 1, 1, 2, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.label_date_credit, 2, 0, 1, 1, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.edit_period_credit, 2, 1, 1, 1, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.combobox_period_credit, 2, 2, 1, 1, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.label_per_credit, 3, 0, 1, 1, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.edit_percent_credit, 3, 1, 1, 2, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.button_calculate1, 4, 0, 1, 3)

            self.grid.addWidget(self.table_view_calculating, 5, 0, 5, 3)

        elif cmb_index == 1:
            self.clean_widgets()

            self.grid.addWidget(self.label_type_credit, 0, 0, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.combobox_type_credit, 0, 1, 1, 2, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.label_sum_credit, 1, 0, 1, 1, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.edit_sum_credit, 1, 1, 1, 2, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.label_payment, 2, 0, 1, 1, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.edit_payment, 2, 1, 1, 2, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.label_per_credit, 3, 0, 1, 1, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.edit_percent_credit, 3, 1, 1, 2, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.button_calculate2, 4, 0, 1, 3)

            self.grid.addWidget(self.table_view_calculating, 5, 0, 5, 3)

        else:
            self.clean_widgets()

            self.grid.addWidget(self.label_type_credit, 0, 0, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.combobox_type_credit, 0, 1, 1, 2, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.label_date_credit, 1, 0, 1, 1, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.edit_period_credit, 1, 1, 1, 1, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.combobox_period_credit, 1, 2, 1, 1, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.label_payment, 2, 0, 1, 1, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.edit_payment, 2, 1, 1, 2, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.label_per_credit, 3, 0, 1, 1, alignment=QtCore.Qt.AlignTop)
            self.grid.addWidget(self.edit_percent_credit, 3, 1, 1, 2, alignment=QtCore.Qt.AlignTop)

            self.grid.addWidget(self.button_calculate3, 4, 0, 1, 3)

            self.grid.addWidget(self.table_view_calculating, 5, 0, 5, 3)

    def clean_widgets(self):
        for i in reversed(range(self.grid.count())):
            self.grid.itemAt(i).widget().setParent(None)

    def validate_for_calculate_month(self, values):
        if self.edit_sum_credit.hasAcceptableInput()\
                and self.edit_period_credit.hasAcceptableInput()\
                and self.edit_percent_credit.hasAcceptableInput():
            self.table_view_calculating.setModel(self.credit.calculate_month(values))
        else:
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Неверный формат данных",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()

    def validate_for_calculate_date(self, values):
        if self.edit_sum_credit.hasAcceptableInput()\
                and self.edit_payment.hasAcceptableInput()\
                and self.edit_percent_credit.hasAcceptableInput():
            self.table_view_calculating.setModel(self.credit.calculate_date(values))
        else:
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Неверный формат данных",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()

    def validate_for_calculate_max_credit(self, values):
        if self.edit_period_credit.hasAcceptableInput() \
                and self.edit_payment.hasAcceptableInput() \
                and self.edit_percent_credit.hasAcceptableInput():
            self.table_view_calculating.setModel(self.credit.calculate_max_credit(values))
        else:
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Неверный формат данных",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()

    def create_gui_credit_calc(self, mdi, statusBar):
        Ui_WindowCreditCalc.count = + 1
        self.credit_window.setWindowTitle("Кредитный калькулятор")
        self.credit_window.setFixedSize(450, 350)

        self.combobox_type_credit.addItems(self.lst_credit)
        self.combobox_period_credit.addItems(self.lst_period)

        self.credit_window.setLayout(self.grid)
        mdi.addSubWindow(self.credit_window)
        self.credit_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.grid.setContentsMargins(8, 8, 8, 8)

        self.credit_window.show()

        if self.credit.check_connect():
            statusBar.showMessage("Вы успешно подключились к БД Кредиты.")
        else:
            statusBar.showMessage("Не удалось подключиться к БД Кредиты.")

        lst_widgets = [self.edit_sum_credit, self.edit_period_credit, self.edit_percent_credit,
                       self.edit_payment, self.combobox_period_credit]

        self.select_item(self.combobox_type_credit.currentIndex())
        self.combobox_type_credit.currentIndexChanged.connect(self.select_item)

        self.button_calculate1.clicked.connect(partial(self.validate_for_calculate_month, lst_widgets))
        self.button_calculate2.clicked.connect(partial(self.validate_for_calculate_date, lst_widgets))
        self.button_calculate3.clicked.connect(partial(self.validate_for_calculate_max_credit, lst_widgets))
