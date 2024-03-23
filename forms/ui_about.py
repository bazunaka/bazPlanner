
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WindowAbout(QtWidgets.QMessageBox):
    def __init__(self, parent=None):
        super(Ui_WindowAbout, self).__init__(parent)

        self.about_window = None
        self.create_GUI()

    def create_GUI(self):
        self.about_window = QtWidgets.QMessageBox()
        self.about_window.about(None, "О программе", "Программа для учета финансов. Написана на Python 3.11 "
                                                     "с использованием библиотеки PyQt5. Версия программы 0.0.1")

        self.about_window.show()