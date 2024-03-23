import json
from functools import partial

from PyQt5 import QtWidgets, QtCore
from modules import bonds

'''Класс графического интерфейса калькулятора доходности облигаций. '''


class Ui_WindowSavingsBonds(QtWidgets.QMdiSubWindow):
    count = 0

    def __init__(self, parent=None):
        super(Ui_WindowSavingsBonds, self).__init__(parent)

        self.lst_percent = ["Фиксированная", "Зависит от суммы", "Зависит от срока"]
        self.lst_period = ["дней", "месяцев", "лет"]
        self.lst_period_payout = ["каждый день", "раз в месяц", "раз в квартал", "раз в полгода", "раз в год",
                                  "в конце срока"]

        '''Блок инициализации надписей типа QLabel.'''
        self.label_name_bonds = QtWidgets.QLabel("Найдите облигацию")
        self.label_period_savings = QtWidgets.QLabel("Срок размещения")
        self.label_date_start = QtWidgets.QLabel("Начало срока")
        self.label_percent_savings = QtWidgets.QLabel("Процентная ставка")
        self.label_period_payout = QtWidgets.QLabel("Периодичность выплат")

        '''Блок инициализации строк ввода текста типа QLineEdit.'''
        self.edit_name_bonds = QtWidgets.QLineEdit()
        self.edit_name_bonds.setPlaceholderText("Введите часть названия или ISIN")
        self.edit_sum_savings = QtWidgets.QLineEdit()
        self.edit_period_savings = QtWidgets.QLineEdit()
        self.edit_percent_credit = QtWidgets.QLineEdit()
        self.edit_payment = QtWidgets.QLineEdit()

        self.check_capitalization = QtWidgets.QCheckBox("Капитализация процентов")

        self.date_start_period = QtWidgets.QDateEdit()
        self.date_end_period = QtWidgets.QDateEdit()

        self.combobox_type_percent = QtWidgets.QComboBox()
        self.combobox_period_savings = QtWidgets.QComboBox()
        self.combobox_period_payout = QtWidgets.QComboBox()

        self.button_calculate = QtWidgets.QPushButton("Рассчитать")

        self.grid = QtWidgets.QGridLayout()
        self.savings_window = QtWidgets.QWidget()

    def test(self, j):
        # print(json.dumps(j, ensure_ascii=False, indent=4, sort_keys=True))
        print("asd")

    def create_gui_savings_bonds(self, mdi):
        Ui_WindowSavingsBonds.count = Ui_WindowSavingsBonds.count + 1
        self.savings_window.setWindowTitle("Калькулятор доходности облигаций")
        self.savings_window.setFixedSize(500, 750)

        # self.combobox_type_percent.addItems(self.lst_percent)
        # self.combobox_period_savings.addItems(self.lst_period)
        # self.combobox_period_payout.addItems(self.lst_period_payout)

        self.grid.addWidget(self.label_name_bonds, 0, 0, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.edit_name_bonds, 0, 1, alignment=QtCore.Qt.AlignTop)

        self.grid.addWidget(self.button_calculate, 1, 1, alignment=QtCore.Qt.AlignTop)

        # self.grid.addWidget(self.label_percent_savings, 1, 0, alignment=QtCore.Qt.AlignTop)
        # self.grid.addWidget(self.edit_period_savings, 1, 1, alignment=QtCore.Qt.AlignTop)
        # self.grid.addWidget(self.combobox_period_savings, 1, 2, alignment=QtCore.Qt.AlignTop)
        #
        # self.grid.addWidget(self.label_date_start, 2, 0, alignment=QtCore.Qt.AlignTop)
        # self.grid.addWidget(self.date_start_period, 2, 1, alignment=QtCore.Qt.AlignTop)
        #
        # self.grid.addWidget(self.check_capitalization, 3, 1, alignment=QtCore.Qt.AlignTop)
        #
        # self.grid.addWidget(self.label_period_payout, 4, 0, alignment=QtCore.Qt.AlignTop)
        # self.grid.addWidget(self.combobox_period_payout, 4, 1, alignment=QtCore.Qt.AlignTop)

        self.savings_window.setLayout(self.grid)
        mdi.addSubWindow(self.savings_window)
        self.savings_window.show()

        # self.button_calculate.clicked.connect(partial(self.test, bonds.Bonds.query("securities", q="втб", group_by="group",
        #                                                                            group_by_filter="stock_bonds",
        #                                                                            limit=10)))

        # engine = "stock"
        # market = "bonds"
        # board = "TQOD"
        # secid = "RU000A0JWHA4"
        self.button_calculate.clicked.connect(partial(self.test, bonds.Bonds.query("engines/stock/markets/bonds/boards/TQOD/securities/RU000A0JWHA4/")))