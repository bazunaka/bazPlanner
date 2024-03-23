
from PyQt5 import QtWidgets, QtCore


class Ui_WindowSavingsCalc(QtWidgets.QMdiSubWindow):

    count = 0
    def __init__(self, parent=None):
        super(Ui_WindowSavingsCalc, self).__init__(parent)

        self.lst_percent = ["Фиксированная", "Зависит от суммы", "Зависит от срока"]
        self.lst_period = ["дней", "месяцев", "лет"]
        self.lst_period_payout = ["каждый день", "раз в месяц", "раз в квартал", "раз в полгода", "раз в год", "в конце срока"]

        self.label_sum_savings = QtWidgets.QLabel("Сумма вклада")
        self.label_period_savings = QtWidgets.QLabel("Срок размещения")
        self.label_date_start = QtWidgets.QLabel("Начало срока")
        self.label_percent_savings = QtWidgets.QLabel("Процентная ставка")
        self.label_period_payout = QtWidgets.QLabel("Периодичность выплат")

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

        self.grid = QtWidgets.QGridLayout()
        self.savings_window = QtWidgets.QWidget()

    def create_gui_savings_calc(self, mdi):
        Ui_WindowSavingsCalc.count = Ui_WindowSavingsCalc.count + 1
        self.savings_window.setWindowTitle("Калькулятор вкладов")
        self.savings_window.setFixedSize(500, 750)

        self.combobox_type_percent.addItems(self.lst_percent)
        self.combobox_period_savings.addItems(self.lst_period)
        self.combobox_period_payout.addItems(self.lst_period_payout)

        self.grid.addWidget(self.label_sum_savings, 0, 0, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.edit_sum_savings, 0, 1, alignment=QtCore.Qt.AlignTop)

        self.grid.addWidget(self.label_percent_savings, 1, 0, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.edit_period_savings, 1, 1, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.combobox_period_savings, 1, 2, alignment=QtCore.Qt.AlignTop)

        self.grid.addWidget(self.label_date_start, 2, 0, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.date_start_period, 2, 1, alignment=QtCore.Qt.AlignTop)

        self.grid.addWidget(self.check_capitalization, 3, 1, alignment=QtCore.Qt.AlignTop)

        self.grid.addWidget(self.label_period_payout, 4, 0, alignment=QtCore.Qt.AlignTop)
        self.grid.addWidget(self.combobox_period_payout, 4, 1, alignment=QtCore.Qt.AlignTop)

        self.savings_window.setLayout(self.grid)
        mdi.addSubWindow(self.savings_window)
        self.savings_window.show()
