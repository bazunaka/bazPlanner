
from functools import partial

from PyQt5 import QtWidgets, QtCore

from forms import ui_add_change_name_banks
from modules import database, bank, credit

dictionary_tables = dict(
    name_banks="name_banks",
    calc_types="calculate_types")

lst_name_buttons = ["Список банков", "Типы расчетов", "Категории доходов", "Категории расходов"]

class Ui_NameBanks(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_NameBanks, self).__init__(parent)

        self.grid = None
        self.dict_window = None
        self.dict_tbl_view = None
        self.change_button = QtWidgets.QPushButton("Изменить")
        self.del_button = QtWidgets.QPushButton("Удалить")
        self.add_button = QtWidgets.QPushButton("Добавить")

        self.change_window = ui_add_change_name_banks.Ui_AddChangeBank()
        self.banks = bank.Bank()


    def print_current(self, table):
        old_name = table.currentIndex().data()
        self.change_window.create_GUI(name_window="Изменить", old_name_bank=old_name, name_click="change")

    def create_GUI(self, name_window, name_db):
        self.dict_window = QtWidgets.QWidget()
        self.dict_window.setWindowTitle(name_window)
        self.dict_window.setFixedSize(300, 450)

        self.dict_tbl_view = QtWidgets.QTableView(self.dict_window)
        self.dict_tbl_view.move(60, 60)

        self.add_button.move(10, 10)
        self.del_button.move(20, 20)
        self.change_button.move(30, 30)

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.dict_tbl_view, 0, 0, 1, 3)
        self.grid.addWidget(self.add_button, 1, 0)
        self.grid.addWidget(self.change_button, 1, 1)
        self.grid.addWidget(self.del_button, 1, 2)

        self.dict_window.setLayout(self.grid)
        self.dict_window.setWindowModality(QtCore.Qt.WindowModal)

        self.dict_window.show()

        connection = database.Database.qsql_connect_db(name_db)

        self.dict_tbl_view.setModel(bank.Bank.select_name_bank())
        self.dict_tbl_view.setColumnWidth(0, 250)
        connection.close()

        self.add_button.clicked.connect(partial(self.change_window.create_GUI, name_window="Добавить", name_click="add"))
        self.change_button.clicked.connect(partial(self.print_current, self.dict_tbl_view))

