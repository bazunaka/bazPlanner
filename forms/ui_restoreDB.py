import os
import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtCore import (QMetaObject, QSize, Qt, QSettings, QRect)
from PyQt5.QtGui import (QIcon, QPixmap)
from PyQt5.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                             QLabel, QPushButton, QSizePolicy, QVBoxLayout,
                             QWidget, QMessageBox, QLineEdit)

from modules.export_db import export_xlsx
from modules import main

sett = os.getcwd() + "/config/resource_path.ini"
sett2 = os.getcwd() + "/config/settings.ini"
settings = QSettings(sett, QSettings.IniFormat)
settings2 = QSettings(sett2, QSettings.IniFormat)

title_window = "Восстановить БД из резервной копии"
first_item_combobox = "Выберите резервную копию"
text_pushbutton = "Восстановить"

lst_export_table = ["banks.db", "credit.db", "categories.db", "profits.db", "deposits.db", "bonds.db"]
dict_export_table = {"1": "banks.db",
                     "2": "credit.db",
                     "3": "Расходы",
                     "4": "Долги",
                     "5": "Запланированные доходы",
                     "6": "Запланированные расходы"}


class Ui_WindowRestoreDB(QtWidgets.QWidget):

    def create_gui_restoredb(self):
        main.os_environ()

        self.restore_window = QtWidgets.QWidget()
        self.restore_window.setWindowTitle(title_window)
        if sys.platform == "darwin":
            self.restore_window.setFixedSize(380, 145)
        else:
            self.restore_window.setFixedSize(350, main.determine_size_monitor()[1] * 0.14)
        self.restore_window.setWindowModality(Qt.ApplicationModal)

        self.horizontalLayout_3 = QHBoxLayout(self.restore_window)

        self.verticalLayout = QVBoxLayout()

        self.horizontalLayout = QHBoxLayout()

        self.icon_change_db = QLabel(self.restore_window)
        self.icon_change_db.setEnabled(True)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(22)
        sizePolicy.setHeightForWidth(self.icon_change_db.sizePolicy().hasHeightForWidth())

        self.icon_dir = QLabel(self.restore_window)

        sizePolicy.setHeightForWidth(self.icon_dir.sizePolicy().hasHeightForWidth())

        self.icon_dir.setSizePolicy(sizePolicy)
        self.icon_dir.setMinimumSize(QSize(22, 22))
        self.icon_dir.setMaximumSize(QSize(22, 22))
        self.icon_dir.setPixmap(
            QPixmap(os.getcwd() + main.create_settings()["settings"].value('/images_exportDB/image_dir')))
        self.icon_dir.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon_dir)

        self.edit_line_dir_import = QLineEdit(self.restore_window)
        self.edit_line_dir_import.setMinimumSize(QSize(0, main.determine_size_monitor()[1] * 0.012))
        self.horizontalLayout.addWidget(self.edit_line_dir_import)

        self.btn_import_dir = QPushButton(text="...")
        self.horizontalLayout.addWidget(self.btn_import_dir)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()

        self.icon_dir = QLabel(self.restore_window)

        sizePolicy.setHeightForWidth(self.icon_dir.sizePolicy().hasHeightForWidth())

        self.icon_dir.setSizePolicy(sizePolicy)
        self.icon_dir.setMinimumSize(QSize(22, 22))
        self.icon_dir.setMaximumSize(QSize(22, 22))
        self.icon_dir.setPixmap(QPixmap(os.getcwd() + settings.value('/images_exportDB/image_dir')))
        self.icon_dir.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.icon_dir)

        self.label_dir_export = QLabel(self.restore_window)
        if sys.platform == "darwin":
            self.label_dir_export.setText(settings2.value('/restore_directory/restore_directory'))
        else:
            self.label_dir_export.setText(settings2.value('/restore_directory_win32/restore_directory'))

        self.horizontalLayout_2.addWidget(self.label_dir_export)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_export = QPushButton(self.restore_window)
        self.pushButton_export.setText(text_pushbutton)
        icon = QIcon()
        icon.addFile(os.getcwd() + settings.value('/images_exportDB/image_export'), QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_export.setIcon(icon)
        self.pushButton_export.setIconSize(QSize(20, 20))

        self.label_info = QLabel(self.restore_window)
        self.label_info.setText("Внимание! Существующие данные будут перезаписаны!")

        self.verticalLayout.addWidget(self.pushButton_export)
        self.verticalLayout.addWidget(self.label_info)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        QMetaObject.connectSlotsByName(self.restore_window)

        self.restore_window.show()

        self.pushButton_export.clicked.connect(partial(self.validate_export))

    def validate_export(self) -> bool:
        if self.comboBox_changeDB.currentText() == first_item_combobox:
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Выберите БД для резервной копии",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()
            return False
        else:
            export_xlsx(self.comboBox_changeDB.currentText())
            return True
