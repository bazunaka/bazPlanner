from functools import partial

from PyQt5.QtWidgets import QMessageBox

from modules import deposits

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QLocale
from PyQt5.QtGui import QIntValidator, QDoubleValidator


class Ui_WindowSavingsDeposit(QtWidgets.QWidget):
    count = 0

    def __init__(self, parent=None):
        super(Ui_WindowSavingsDeposit, self).__init__(parent)

        """
        Block where create lists for ComboBox.
        """
        self.lst_percent = ["Фиксированная", "Зависит от суммы", "Зависит от срока"]
        self.lst_period = ["дней", "месяцев", "лет"]
        self.lst_period_payout = ["каждый день", "раз в месяц", "раз в квартал", "раз в полгода", "раз в год",
                                  "в конце срока"]
        self.lst_period_replenishment = ["каждый день", "каждую неделю", "раз в месяц"]

        """
        Block where create labels.
        """
        self.label_sum_deposit = QtWidgets.QLabel("Сумма вклада")
        self.label_period_deposit = QtWidgets.QLabel("Срок размещения")
        self.label_start_date = QtWidgets.QLabel("Дата открытия вклада")
        self.label_percent_deposit = QtWidgets.QLabel("Процентная ставка")
        self.label_period_payout = QtWidgets.QLabel("Периодичность выплат")
        self.label_period_payout = QtWidgets.QLabel("Периодичность выплат")
        self.label_replenishment = QtWidgets.QLabel("Сумма пополнений")

        """
        Block where create and validate edits.
        """
        self.edit_sum_deposit = QtWidgets.QLineEdit()
        self.edit_period_deposit = QtWidgets.QLineEdit()
        self.edit_percent_deposit = QtWidgets.QLineEdit()
        self.edit_period_replenishment = QtWidgets.QLineEdit()
        self.edit_period_replenishment.setPlaceholderText("Сумма пополнений")

        self.edit_sum_deposit.setValidator(QIntValidator(1000, 10000000))
        self.edit_period_deposit.setValidator(QIntValidator(1, 400))
        self.edit_percent_deposit.setValidator(QDoubleValidator(1, 30.0, 2))
        self.edit_period_replenishment.setValidator(QIntValidator(1, 150000))

        self.check_capitalization = QtWidgets.QCheckBox("Капитализация процентов")
        self.check_is_replenishment = QtWidgets.QCheckBox("Возможность пополнения")

        self.date_start_period = QtWidgets.QDateEdit()
        self.date_start_period.setCalendarPopup(True)
        self.date_start_period.setLocale(QLocale(QLocale.Russian, QLocale.Russia))
        self.date_start_period.setDate(QtCore.QDate.currentDate())

        self.date_end_period = QtWidgets.QDateEdit()

        """
        Block where create comboboxes.
        """
        self.combobox_type_percent = QtWidgets.QComboBox()
        self.combobox_period_savings = QtWidgets.QComboBox()
        self.combobox_period_payout = QtWidgets.QComboBox()
        self.combobox_period_replenishment = QtWidgets.QComboBox()

        self.button_calculate = QtWidgets.QPushButton("Рассчитать")

        self.table_view_calculating = QtWidgets.QTableView()

        self.grid = QtWidgets.QGridLayout()
        # self.grid.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.savings_window = QtWidgets.QWidget()

        self.deposits = deposits.Deposits()

    def validate_for_calculate_deposit(self, values):
        if self.edit_sum_deposit.hasAcceptableInput()\
                and self.edit_percent_deposit.hasAcceptableInput()\
                and self.edit_period_deposit.hasAcceptableInput():
            self.table_view_calculating.setModel(self.deposits.calculate_deposit(values))
        else:
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Неверный формат данных",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()

    def create_gui_savings_deposit(self, mdi):
        Ui_WindowSavingsDeposit.count = Ui_WindowSavingsDeposit.count + 1
        self.savings_window.setWindowTitle("Калькулятор вкладов")
        self.savings_window.setFixedSize(580, 550)

        """
        Blocks where add items in comboboxes.
        """
        self.combobox_type_percent.addItems(self.lst_percent)
        self.combobox_period_savings.addItems(self.lst_period)
        self.combobox_period_payout.addItems(self.lst_period_payout)
        self.combobox_period_replenishment.addItems(self.lst_period_replenishment)

        """
        Block where add widgets in grid layout.
        """
        self.grid.addWidget(self.label_sum_deposit, 0, 0, 1, 1)
        self.grid.addWidget(self.edit_sum_deposit, 0, 1, 1, 2)

        self.grid.addWidget(self.label_percent_deposit, 1, 0, 1, 1)
        self.grid.addWidget(self.edit_percent_deposit, 1, 1, 1, 2)

        self.grid.addWidget(self.label_period_deposit, 2, 0, 1, 1)
        self.grid.addWidget(self.edit_period_deposit, 2, 1, 1, 1)
        self.grid.addWidget(self.combobox_period_savings, 2, 2, 1, 1)

        self.grid.addWidget(self.label_start_date, 3, 0, 1, 1)
        self.grid.addWidget(self.date_start_period, 3, 1, 1, 2)

        self.grid.addWidget(self.label_period_payout, 4, 0, 1, 1)
        self.grid.addWidget(self.combobox_period_payout, 4, 1, 1, 2)

        self.grid.addWidget(self.check_capitalization, 5, 0, 1, 1)
        self.grid.addWidget(self.edit_period_replenishment, 5, 1, 1, 1)
        self.grid.addWidget(self.combobox_period_replenishment, 5, 2, 1, 1)

        self.grid.addWidget(self.check_is_replenishment, 6, 1)

        self.grid.addWidget(self.button_calculate, 7, 0, 1, 3)

        self.grid.addWidget(self.table_view_calculating, 8, 0, 3, 3)

        self.savings_window.setContentsMargins(5, 5, 5, 5)

        self.savings_window.setLayout(self.grid)
        mdi.addSubWindow(self.savings_window)
        self.savings_window.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        # self.savings_window.showMaximized()
        self.savings_window.show()

        lst_widgets = [self.edit_sum_deposit, self.edit_percent_deposit, self.edit_period_deposit,
                       self.date_start_period, self.check_capitalization, self.check_is_replenishment]

        self.button_calculate.clicked.connect(partial(self.validate_for_calculate_deposit, lst_widgets))