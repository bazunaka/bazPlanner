import os
from functools import partial

from PyQt5 import QtWidgets, QtSvg
from PyQt5.QtCore import QMetaObject, QSize, QSettings, Qt
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter

from forms import ui_add_change_bank_acc
from modules.database import Database, DatabaseCategories, DatabaseBank
from modules import bank_accounts

lst_headers = ["Название счета", "Название банка", "Тип счета", "Сумма на счете"]


class Ui_BankAccount(QtWidgets.QWidget):
    count = 0

    def __init__(self, parent=None):
        super(Ui_BankAccount, self).__init__(parent)

        self.statusbar = None
        self.cat_window = None
        self.add_bank_account = QtWidgets.QPushButton()
        self.change_bank_account = QtWidgets.QPushButton()
        self.delete_bank_account = QtWidgets.QPushButton()

        self.bank_accounts_window = QtWidgets.QWidget()
        sett = os.getcwd() + "/config/resource_path.ini"
        self.settings = QSettings(sett, QSettings.IniFormat)

        self.bank_accounts = bank_accounts.BankAccount()

    def create_gui_bank_account(self):
        Ui_BankAccount.count = + 1

        os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
        os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
        os.environ["QT_SCALE_FACTOR"] = "1"

        self.bank_accounts_window.setWindowTitle("Счета в банках")
        self.bank_accounts_window.resize(515, 350)
        self.bank_accounts_window.setMinimumSize(515, 350)

        self.grid = QtWidgets.QGridLayout(self.bank_accounts_window)
        self.verticalLayout = QtWidgets.QVBoxLayout()

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_bank_account.sizePolicy().hasHeightForWidth())
        self.add_bank_account.setSizePolicy(sizePolicy)
        self.add_bank_account.setSizeIncrement(QSize(0, 0))
        icon = QIcon()
        icon.addFile(os.getcwd() + self.settings.value('/images_bank_accounts/image_add'), QSize(),
                     QIcon.Normal, QIcon.Off)
        self.add_bank_account.setIcon(icon)
        self.add_bank_account.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.add_bank_account)

        sizePolicy.setHeightForWidth(self.change_bank_account.sizePolicy().hasHeightForWidth())
        self.change_bank_account.setSizePolicy(sizePolicy)
        self.change_bank_account.setSizeIncrement(QSize(0, 0))
        icon1 = QIcon()
        icon1.addFile(os.getcwd() + self.settings.value('/images_bank_accounts/image_change'), QSize(),
                      QIcon.Normal, QIcon.Off)
        self.change_bank_account.setIcon(icon1)
        self.change_bank_account.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.change_bank_account)

        sizePolicy.setHeightForWidth(self.delete_bank_account.sizePolicy().hasHeightForWidth())
        self.delete_bank_account.setSizePolicy(sizePolicy)
        self.delete_bank_account.setSizeIncrement(QSize(0, 0))
        icon2 = QIcon()
        icon2.addFile(os.getcwd() + self.settings.value('/images_bank_accounts/image_delete'), QSize(),
                      QIcon.Normal, QIcon.Off)
        self.delete_bank_account.setIcon(icon2)
        self.delete_bank_account.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.delete_bank_account)

        self.grid.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.tableView = QtWidgets.QTableView(self.bank_accounts_window)

        self.verticalLayout_2.addWidget(self.tableView)

        self.grid.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        QMetaObject.connectSlotsByName(self.bank_accounts_window)
        self.bank_accounts_window.setWindowModality(Qt.ApplicationModal)
        self.bank_accounts_window.show()

        model = self.show_bank_accounts()
        self.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableView.setModel(model)
        for i in range(4):
            model.setHeaderData(i, Qt.Orientation.Horizontal, lst_headers[i])
            i += 1

        self.add_bank_account.clicked.connect(partial(self.show_add_window,
                                                      name_window="Добавить счет", name_click="add"))
        self.change_bank_account.clicked.connect(partial(self.show_change_window,
                                                         name_window="Изменить счет", name_click="change"))
        self.delete_bank_account.clicked.connect(self.delete_bank_acc)

    def show_add_window(self, name_window, name_click):
        self.ui = ui_add_change_bank_acc.Ui_ChangeBankAcc()
        self.ui.setupUi(name_window, name_click)

    def show_change_window(self, name_window, name_click):
        indexes = self.tableView.selectedIndexes()
        lst_values = []
        for index in range(len(indexes)):
            lst_values.append(indexes[index].data())

        self.ui = ui_add_change_bank_acc.Ui_ChangeBankAcc()
        self.ui.setupUi(name_window, name_click, lst_values)

    def show_bank_accounts(self):
        query = DatabaseBank.select("*", table_name="view_bank_accounts", where=False, order_by=False)
        model = DatabaseBank.view_model(query)
        return model

    def delete_bank_acc(self):
        indexes = self.tableView.selectedIndexes()
        name = indexes[0].data()
        # if bank_accounts.BankAccount.delete_bank_acc(name):
        #     print("Счет " + name + " удален")
        # else:
        #     print("Счет " + name + " не удален")
        print(name)