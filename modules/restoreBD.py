import os
import sys
from shutil import copy

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from modules import main


def restore_db(name_database: str):
    if sys.platform == "darwin":
        pass
    else:
        connection_string = main.create_settings()["settings2"].value('/connection_strings_win32/connection_string_main')
        if os.path.exists(connection_string + name_database):
            copy(connection_string + name_database, os.getcwd() + "/backup/")
        else:
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Файл не найден!",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()
            return False
