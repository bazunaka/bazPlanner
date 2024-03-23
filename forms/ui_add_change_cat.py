from functools import partial

from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox


class Ui_AddChangeCategory(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit = None


    def validate_for_add_change_cat(self, values):
        # if values[0].text() == "":
        #     dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Заполните поле",
        #                          buttons=QtWidgets.QMessageBox.Ok)
        #     dialog.exec()
        # else:
        #     self.bank.name_bank = values[0].text()
        #     self.bank.add_bank()
        pass

    def create_GUI(self, name_window, name_click, old_name_cat=""):
        self.change_window = QtWidgets.QWidget()
        self.change_window.setWindowTitle(name_window)
        self.change_window.setFixedSize(350, 100)

        self.add_button = QtWidgets.QPushButton("Добавить")
        self.change_button = QtWidgets.QPushButton("Изменить")
        self.text_edit = QtWidgets.QLineEdit()

        self.grid = QtWidgets.QGridLayout()

        self.grid.addWidget(self.text_edit, 0, 0, 1, 3)
        if name_click == "add":
            self.grid.addWidget(self.add_button, 1, 0, 1, 3)
        else:
            self.text_edit.setText(old_name_cat)
            self.grid.addWidget(self.change_button, 1, 0, 1, 3)

        self.change_window.setLayout(self.grid)
        self.change_window.setWindowModality(QtCore.Qt.ApplicationModal)

        self.change_window.show()

        lst_widgets = [self.text_edit]

        # self.save_button.clicked.connect(partial(self.bank.add_bank, connection))
        # self.save_button.clicked.connect(partial(self.validate_for_add_change_bank, lst_widgets))
        # self.save_button1.clicked.connect(self.test1)
        # self.save_button.clicked.connect(partial(self.add_name_bank, name_click, old_name_bank))

