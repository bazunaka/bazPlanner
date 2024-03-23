from functools import partial

from PyQt5 import QtWidgets, QtCore, QtGui

from forms import ui_add_change_name_banks, ui_MainWindow
from modules.database import Database, DatabaseCategories
from modules import profits


class Ui_Profits(QtWidgets.QWidget):
    count = 0

    def __init__(self, parent=None):
        super(Ui_Profits, self).__init__(parent)

        self.statusbar = None
        self.grid = None
        self.cat_window = None
        self.add_profit = QtWidgets.QPushButton()
        self.change_profit = QtWidgets.QPushButton("Удалить")
        self.delete_profit = QtWidgets.QPushButton("Добавить")

        self.table_view_profits = QtWidgets.QTableView()

        self.profits_window = QtWidgets.QWidget()

        self.profits = profits.Profits()

    def create_gui_profits(self, mdi, statusBar):
        Ui_Profits.count = + 1
        self.statusbar = statusBar

        self.profits_window.setWindowTitle("Личные доходы")
        self.profits_window.setFixedSize(500, 450)

        add_icon = QtGui.QPixmap("../icons/profits/profits_ioee69w4ncdl.png")
        self.add_profit.setIcon(QtGui.QIcon(add_icon))

        self.grid = QtWidgets.QGridLayout()

        self.grid.addWidget(self.add_profit, 0, 0, 1, 1)
        self.grid.addWidget(self.change_profit, 1, 0, 1, 1)
        self.grid.addWidget(self.delete_profit, 2, 0, 1, 1)
        self.grid.addWidget(self.table_view_profits, 0, 1, 3, 3)

        self.profits_window.setLayout(self.grid)
        self.profits_window.setWindowModality(QtCore.Qt.ApplicationModal)

        self.profits_window.show()

        if self.profits.check_connect():
            statusBar.showMessage("Вы успешно подключились к БД Доходы.", 5000)
        else:
            statusBar.showMessage("Не удалось подключиться к БД Доходы.")

        # connection = Database.qsql_connect_db(name_db)
        # query = DatabaseCategories.select("categories", "name_category", where_field="id_type",
        #                                   where_value=id_type, order_by=False)
        # model = DatabaseCategories.view_model(connection, query)
        # self.cat_lst_view.setModel(model)
        # self.cat_lst_view.selectionModel().selectionChanged.connect(self.show_sub_cat)
        #
        # self.profits_window.closeEvent = self.closeEvent

        # if "banks" in name_db:
        #     self.dict_tbl_view.setModel(bank.Bank.select_name_bank(connection))
        #     self.dict_tbl_view.setColumnWidth(0, 250)
        #     connection.close()
        # elif "credits" in name_db:
        #     self.dict_tbl_view.setModel(credit.Credit.select_type_calc(connection))
        #     self.dict_tbl_view.setColumnWidth(0, 250)
        #     connection.close()

        # if connection:
        #     if name_db == "banks.db":
        #         self.dict_tbl_view.setModel(bank.Bank.select_name_bank(connection))
        #         connection.close()
        #     else:
        #         model = database.Database.select_from_tables(connection, dictionary_tables["calc_types"], "type_name")
        #         self.dict_tbl_view.setModel(model)
        #         self.add_button.setEnabled(False)
        #         self.del_button.setEnabled(False)
        #         self.change_button.setEnabled(False)
        #         connection.close()
        # else:
        #     print("Error")

        # self.add_button.clicked.connect(partial(self.change_window.create_GUI, name_window="Добавить", name_click="add"))
