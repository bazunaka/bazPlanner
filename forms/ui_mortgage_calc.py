from functools import partial

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox

from modules import mortgage


class Ui_WindowMortgageCalc(QtWidgets.QWidget):
    count = 0

    def __init__(self, parent=None):
        super(Ui_WindowMortgageCalc, self).__init__(parent)

        self.lst_period = ["лет", "месяцев"]
        self.lst_initial_payment = ["₽", "%"]

        self.label_cost_property = QtWidgets.QLabel("Стоимость недвижимости")
        self.label_initial_payment = QtWidgets.QLabel("Первоначальный взнос")
        self.label_initial_info = QtWidgets.QLabel("Расчет взноса")
        self.label_sum_mortgage = QtWidgets.QLabel("Сумма кредита")
        self.label_period_credit = QtWidgets.QLabel("Срок кредита")
        self.label_per_credit = QtWidgets.QLabel("Процентная ставка")

        self.edit_cost_property = QtWidgets.QLineEdit()
        self.edit_initial_payment = QtWidgets.QLineEdit()
        self.edit_sum_mortgage = QtWidgets.QLineEdit()
        self.edit_period_credit = QtWidgets.QLineEdit()
        self.edit_percent_credit = QtWidgets.QLineEdit()

        self.edit_cost_property.setValidator(QtGui.QIntValidator(500000, 150000000))
        self.edit_initial_payment.setValidator(QtGui.QIntValidator(150000, 125000000))
        self.edit_period_credit.setValidator(QtGui.QIntValidator(1, 360))
        self.edit_percent_credit.setValidator(QtGui.QDoubleValidator(1.0, 49.9, 2))

        self.edit_sum_mortgage.setEnabled(False)

        self.combobox_type_initial = QtWidgets.QComboBox()
        self.combobox_period_credit = QtWidgets.QComboBox()

        self.button_calculate = QtWidgets.QPushButton("Рассчитать")

        self.table_view_calculating = QtWidgets.QTableView()

        self.grid = QtWidgets.QGridLayout()
        self.mortgage_window = QtWidgets.QWidget()

        self.mortgage = mortgage.Mortgage()

    def validate_for_calculate_mortgage(self, values):
        if self.edit_cost_property.hasAcceptableInput() \
                and self.edit_initial_payment.hasAcceptableInput() \
                and self.edit_period_credit.hasAcceptableInput() \
                and self.edit_percent_credit.hasAcceptableInput():
            self.table_view_calculating.setModel(self.mortgage.calculate_mortgage(values))
        else:
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Неверный формат данных",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()

    def create_gui_mortgage_calc(self, mdi):
        Ui_WindowMortgageCalc.count = + 1
        self.mortgage_window.setWindowTitle("Ипотечный калькулятор")
        self.mortgage_window.setFixedSize(450, 500)

        self.combobox_type_initial.addItems(self.lst_initial_payment)
        self.combobox_period_credit.addItems(self.lst_period)

        self.grid.addWidget(self.label_cost_property, 0, 0, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.edit_cost_property, 0, 1, alignment=QtCore.Qt.AlignTop)

        self.grid.addWidget(self.label_initial_payment, 1, 0, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.edit_initial_payment, 1, 1, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.combobox_type_initial, 1, 2, alignment=QtCore.Qt.AlignTop)

        self.grid.addWidget(self.label_initial_info, 2, 2, 1, 1)

        self.grid.addWidget(self.label_sum_mortgage, 3, 0, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.edit_sum_mortgage, 3, 1, alignment=QtCore.Qt.AlignTop)

        self.grid.addWidget(self.label_period_credit, 4, 0, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.edit_period_credit, 4, 1, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.combobox_period_credit, 4, 2, alignment=QtCore.Qt.AlignTop)

        self.grid.addWidget(self.label_per_credit, 5, 0, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.edit_percent_credit, 5, 1, alignment=QtCore.Qt.AlignTop)

        self.grid.addWidget(self.button_calculate, 6, 0, 1, 3, alignment=QtCore.Qt.AlignTop)

        self.grid.addWidget(self.table_view_calculating, 7, 0, 7, 3, alignment=QtCore.Qt.AlignTop)

        self.mortgage_window.setLayout(self.grid)
        mdi.addSubWindow(self.mortgage_window)
        self.mortgage_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        self.grid.setContentsMargins(5, 5, 5, 5)

        self.mortgage_window.show()

        # if self.mortgage.check_connect():
        #     statusBar.showMessage("Вы успешно подключились к БД Кредиты.")
        # else:
        #     statusBar.showMessage("Не удалось подключиться к БД Кредиты.")

        lst_widgets = [self.edit_cost_property, self.edit_initial_payment, self.edit_sum_mortgage,
                       self.edit_period_credit, self.edit_percent_credit, self.combobox_period_credit]

        self.button_calculate.clicked.connect(partial(self.validate_for_calculate_mortgage, lst_widgets))
