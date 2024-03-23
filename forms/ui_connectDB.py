import os
import sys
from functools import partial

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QSettings

dict_connection_string = {"win32": "connection_strings_win32", "macos": "connection_strings"}


class Ui_WindowConnectDB(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_WindowConnectDB, self).__init__(parent)

        self.group_box_credits = QtWidgets.QGroupBox("Подключение к БД Кредиты")
        self.group_box_banks = QtWidgets.QGroupBox("Подключение к БД Банки")
        self.group_box_mortgage = QtWidgets.QGroupBox("Подключение к БД Ипотека")
        self.group_box_savings = QtWidgets.QGroupBox("Подключение к БД Сбережения")
        self.group_box_moex = QtWidgets.QGroupBox("Подключение к БД МосБиржи")
        self.group_box_cat = QtWidgets.QGroupBox("Подключение к БД Категорий")
        self.group_box_profits = QtWidgets.QGroupBox("Подключение к БД Доходы")
        self.group_box_spend_money = QtWidgets.QGroupBox("Подключение к БД Расходы")

        self.label_test_connect = QtWidgets.QLabel("Подключение отсутствует...")

        self.button_save_connect1 = QtWidgets.QPushButton("Сохранить файл")
        self.button_save_connect2 = QtWidgets.QPushButton("Сохранить файл")
        self.button_save_connect3 = QtWidgets.QPushButton("Сохранить файл")
        self.button_save_connect4 = QtWidgets.QPushButton("Сохранить файл")
        self.button_save_connect5 = QtWidgets.QPushButton("Сохранить файл")
        self.button_save_connect6 = QtWidgets.QPushButton("Сохранить файл")
        self.button_save_connect7 = QtWidgets.QPushButton("Сохранить файл")
        self.button_save_connect8 = QtWidgets.QPushButton("Сохранить файл")

        self.button_open_file1 = QtWidgets.QPushButton("Выбрать файл")
        self.button_open_file2 = QtWidgets.QPushButton("Выбрать файл")
        self.button_open_file3 = QtWidgets.QPushButton("Выбрать файл")
        self.button_open_file4 = QtWidgets.QPushButton("Выбрать файл")
        self.button_open_file5 = QtWidgets.QPushButton("Выбрать файл")
        self.button_open_file6 = QtWidgets.QPushButton("Выбрать файл")
        self.button_open_file7 = QtWidgets.QPushButton("Выбрать файл")
        self.button_open_file8 = QtWidgets.QPushButton("Выбрать файл")

        self.line_edit_file_connect1 = QtWidgets.QLineEdit()
        self.line_edit_file_connect2 = QtWidgets.QLineEdit()
        self.line_edit_file_connect3 = QtWidgets.QLineEdit()
        self.line_edit_file_connect4 = QtWidgets.QLineEdit()
        self.line_edit_file_connect5 = QtWidgets.QLineEdit()
        self.line_edit_file_connect6 = QtWidgets.QLineEdit()
        self.line_edit_file_connect7 = QtWidgets.QLineEdit()
        self.line_edit_file_connect8 = QtWidgets.QLineEdit()

        self.grid_group1 = QtWidgets.QGridLayout()
        self.grid_group2 = QtWidgets.QGridLayout()
        self.grid_group3 = QtWidgets.QGridLayout()
        self.grid_group4 = QtWidgets.QGridLayout()
        self.grid_group5 = QtWidgets.QGridLayout()
        self.grid_group6 = QtWidgets.QGridLayout()
        self.grid_group7 = QtWidgets.QGridLayout()
        self.grid_group8 = QtWidgets.QGridLayout()

        self.scroll = QtWidgets.QScrollArea()

        self.scrollLayout = QtWidgets.QVBoxLayout()
        self.scrollW = QtWidgets.QWidget()

        self.grid = QtWidgets.QGridLayout()
        self.connectdb_window = QtWidgets.QWidget()

    def create_gui_connectdb(self):
        self.connectdb_window.setWindowTitle("Настройка подключения к БД")
        self.connectdb_window.setFixedSize(500, 350)

        self.grid.addWidget(self.scroll)

        self.scroll.setWidget(self.scrollW)

        self.scrollW.setLayout(self.scrollLayout)
        self.scrollLayout.setAlignment(QtCore.Qt.AlignTop)

        self.scroll.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)

        self.grid_group1.addWidget(self.line_edit_file_connect1, 0, 0, 1, 2)
        self.grid_group1.addWidget(self.button_open_file1, 0, 2, 1, 1)
        self.grid_group1.addWidget(self.button_save_connect1, 1, 0, 1, 3)

        self.grid_group2.addWidget(self.line_edit_file_connect2, 0, 0, 1, 2)
        self.grid_group2.addWidget(self.button_open_file2, 0, 2, 1, 1)
        self.grid_group2.addWidget(self.button_save_connect2, 1, 0, 1, 3)

        self.grid_group3.addWidget(self.line_edit_file_connect3, 0, 0, 1, 2)
        self.grid_group3.addWidget(self.button_open_file3, 0, 2, 1, 1)
        self.grid_group3.addWidget(self.button_save_connect3, 1, 0, 1, 3)

        self.grid_group4.addWidget(self.line_edit_file_connect4, 0, 0, 1, 2)
        self.grid_group4.addWidget(self.button_open_file4, 0, 2, 1, 1)
        self.grid_group4.addWidget(self.button_save_connect4, 1, 0, 1, 3)

        self.grid_group5.addWidget(self.line_edit_file_connect5, 0, 0, 1, 2)
        self.grid_group5.addWidget(self.button_open_file5, 0, 2, 1, 1)
        self.grid_group5.addWidget(self.button_save_connect5, 1, 0, 1, 3)

        self.grid_group6.addWidget(self.line_edit_file_connect6, 0, 0, 1, 2)
        self.grid_group6.addWidget(self.button_open_file6, 0, 2, 1, 1)
        self.grid_group6.addWidget(self.button_save_connect6, 1, 0, 1, 3)

        self.grid_group7.addWidget(self.line_edit_file_connect7, 0, 0, 1, 2)
        self.grid_group7.addWidget(self.button_open_file7, 0, 2, 1, 1)
        self.grid_group7.addWidget(self.button_save_connect7, 1, 0, 1, 3)

        self.grid_group8.addWidget(self.line_edit_file_connect8, 0, 0, 1, 2)
        self.grid_group8.addWidget(self.button_open_file8, 0, 2, 1, 1)
        self.grid_group8.addWidget(self.button_save_connect8, 1, 0, 1, 3)

        self.group_box_banks.setLayout(self.grid_group1)
        self.group_box_credits.setLayout(self.grid_group2)
        self.group_box_mortgage.setLayout(self.grid_group3)
        self.group_box_savings.setLayout(self.grid_group4)
        self.group_box_moex.setLayout(self.grid_group5)
        self.group_box_cat.setLayout(self.grid_group6)
        self.group_box_profits.setLayout(self.grid_group7)
        self.group_box_spend_money.setLayout(self.grid_group8)

        self.scrollLayout.addWidget(self.group_box_banks)
        self.scrollLayout.addWidget(self.group_box_credits)
        self.scrollLayout.addWidget(self.group_box_mortgage)
        self.scrollLayout.addWidget(self.group_box_savings)
        self.scrollLayout.addWidget(self.group_box_moex)
        self.scrollLayout.addWidget(self.group_box_cat)
        self.scrollLayout.addWidget(self.group_box_profits)
        self.scrollLayout.addWidget(self.group_box_spend_money)

        self.connectdb_window.setLayout(self.grid)

        self.connectdb_window.show()

        sett = os.getcwd() + "/config/settings.ini"
        self.settings = QSettings(sett, QSettings.IniFormat)
        if sys.platform == "win32":
            self.check_connection_string(dict_connection_string['win32'])
        else:
            self.check_connection_string(dict_connection_string['macos'])

        self.button_open_file1.clicked.connect(
            partial(self.btn_clicked_openfile, line_edit=self.line_edit_file_connect1))
        self.button_open_file2.clicked.connect(
            partial(self.btn_clicked_openfile, line_edit=self.line_edit_file_connect2))
        self.button_open_file3.clicked.connect(
            partial(self.btn_clicked_openfile, line_edit=self.line_edit_file_connect3))
        self.button_open_file4.clicked.connect(
            partial(self.btn_clicked_openfile, line_edit=self.line_edit_file_connect4))
        self.button_open_file5.clicked.connect(
            partial(self.btn_clicked_openfile, line_edit=self.line_edit_file_connect5))
        self.button_open_file6.clicked.connect(
            partial(self.btn_clicked_openfile, line_edit=self.line_edit_file_connect6))
        self.button_open_file7.clicked.connect(
            partial(self.btn_clicked_openfile, line_edit=self.line_edit_file_connect7))
        self.button_open_file8.clicked.connect(
            partial(self.btn_clicked_openfile, line_edit=self.line_edit_file_connect8))

        self.button_save_connect1.clicked.connect(
            partial(self.btn_clicked_savefile, line_edit=self.line_edit_file_connect1,
                    name_connect='connection_string_banksdb'))
        self.button_save_connect2.clicked.connect(
            partial(self.btn_clicked_savefile, line_edit=self.line_edit_file_connect2,
                    name_connect='connection_string_creditsdb'))
        self.button_save_connect3.clicked.connect(
            partial(self.btn_clicked_savefile, line_edit=self.line_edit_file_connect3,
                    name_connect='connection_string_mortgagesdb'))
        self.button_save_connect4.clicked.connect(
            partial(self.btn_clicked_savefile, line_edit=self.line_edit_file_connect4,
                    name_connect='connection_string_savingsdb'))
        self.button_save_connect5.clicked.connect(
            partial(self.btn_clicked_savefile, line_edit=self.line_edit_file_connect5,
                    name_connect='connection_string_moexdb'))
        self.button_save_connect6.clicked.connect(
            partial(self.btn_clicked_savefile, line_edit=self.line_edit_file_connect6,
                    name_connect='connection_string_categories'))
        self.button_save_connect7.clicked.connect(
            partial(self.btn_clicked_savefile, line_edit=self.line_edit_file_connect7,
                    name_connect='connection_string_profits'))
        self.button_save_connect8.clicked.connect(
            partial(self.btn_clicked_savefile, line_edit=self.line_edit_file_connect8,
                    name_connect='connection_string_spend_money'))

    def btn_clicked_openfile(self, line_edit):
        cwd = os.getcwd() + "/databases"
        result = QtWidgets.QFileDialog.getOpenFileName(None, "Открыть файл", cwd, "Database File (*.db)")
        line_edit.setText(result[0])

    def btn_clicked_savefile(self, line_edit, name_connect):
        # save_file = QtWidgets.QFileDialog.getSaveFileName(self, "Сохранить файл", "Users/", "Database File (*.db)")
        if sys.platform == "win32":
            self.settings = QSettings("config/settings.ini", QSettings.IniFormat)
            self.settings.beginGroup('connection_strings_win32')
            self.settings.setValue(name_connect, line_edit.text())
            self.settings.endGroup()
        else:
            self.settings = QSettings("config/settings.ini", QSettings.IniFormat)
            self.settings.beginGroup('connection_strings')
            self.settings.setValue(name_connect, line_edit.text())
            self.settings.endGroup()

    def check_connection_string(self, name_connection_string):
        self.line_edit_file_connect1.setText(
            self.settings.value(name_connection_string + '/connection_string_banksdb'))
        self.line_edit_file_connect2.setText(
            self.settings.value(name_connection_string + '/connection_string_creditsdb'))
        self.line_edit_file_connect3.setText(
            self.settings.value(name_connection_string + '/connection_string_mortgagesdb'))
        self.line_edit_file_connect4.setText(
            self.settings.value(name_connection_string + '/connection_string_savingsdb'))
        self.line_edit_file_connect5.setText(
            self.settings.value(name_connection_string + '/connection_string_moexdb'))
        self.line_edit_file_connect6.setText(
            self.settings.value(name_connection_string + '/connection_string_categories'))
        self.line_edit_file_connect7.setText(
            self.settings.value(name_connection_string + '/connection_string_profits'))
        self.line_edit_file_connect8.setText(
            self.settings.value(name_connection_string + '/connection_string_spend_money'))
