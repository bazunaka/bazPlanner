import os
import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtCore import (QMetaObject, QSize, Qt)
from PyQt5.QtGui import (QIcon, QPixmap)
from PyQt5.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                             QLabel, QPushButton, QSizePolicy, QVBoxLayout,
                             QWidget, QLineEdit, QMessageBox)

from modules.import_db import import_xlsx
from modules import main

lst_import_table = ["Счета", "Доходы", "Расходы", "Долги", "Запланированные доходы", "Запланированные расходы"]
dict_import_table = {"1": "Счета", "2": "Доходы", "3": "Расходы", "4": "Долги", "5": "Запланированные доходы",
                     "6": "Запланированные расходы"}


class Ui_WindowImportDB(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_WindowImportDB, self).__init__(parent)

    def create_gui_importdb(self):
        main.os_environ()

        self.import_window = QtWidgets.QWidget()
        self.import_window.setWindowTitle("Импортировать в БД")
        if sys.platform == "darwin":
            self.import_window.setFixedSize(375,
                                            main.determine_size_monitor()[1] * 0.2)
        else:
            self.import_window.setFixedSize(main.determine_size_monitor()[0] * 0.19,
                                            main.determine_size_monitor()[1] * 0.15)

        self.import_window.setWindowModality(Qt.ApplicationModal)

        self.horizontalLayout_3 = QHBoxLayout(self.import_window)

        self.verticalLayout = QVBoxLayout()

        self.horizontalLayout = QHBoxLayout()

        self.icon_change_db = QLabel(self.import_window)
        self.icon_change_db.setEnabled(True)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(22)
        sizePolicy.setHeightForWidth(self.icon_change_db.sizePolicy().hasHeightForWidth())

        self.horizontalLayout_2 = QHBoxLayout()

        self.icon_dir = QLabel(self.import_window)

        sizePolicy.setHeightForWidth(self.icon_dir.sizePolicy().hasHeightForWidth())

        self.icon_dir.setSizePolicy(sizePolicy)
        self.icon_dir.setMinimumSize(QSize(22, 22))
        self.icon_dir.setMaximumSize(QSize(22, 22))
        self.icon_dir.setPixmap(QPixmap(os.getcwd() + main.create_settings()["settings"].value('/images_exportDB/image_dir')))
        self.icon_dir.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.icon_dir)

        self.edit_line_dir_import = QLineEdit(self.import_window)
        self.edit_line_dir_import.setMinimumSize(QSize(0, main.determine_size_monitor()[1] * 0.012))
        self.horizontalLayout_2.addWidget(self.edit_line_dir_import)

        self.btn_import_dir = QPushButton(text="...")
        self.horizontalLayout_2.addWidget(self.btn_import_dir)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.icon_change_db.setSizePolicy(sizePolicy)
        self.icon_change_db.setMinimumSize(QSize(22, 22))
        self.icon_change_db.setMaximumSize(QSize(22, 22))
        self.icon_change_db.setAutoFillBackground(False)
        self.icon_change_db.setFrameShape(QFrame.NoFrame)
        self.icon_change_db.setFrameShadow(QFrame.Plain)
        self.icon_change_db.setPixmap(QPixmap(os.getcwd() + main.create_settings()["settings"].value('/images_exportDB/image_changedb')))
        self.icon_change_db.setScaledContents(True)
        self.icon_change_db.setWordWrap(False)

        self.horizontalLayout.addWidget(self.icon_change_db)

        self.comboBox_changeDB = QComboBox(self.import_window)
        self.comboBox_changeDB.addItem(
            "Выберите таблицу для импорта..."
        )
        self.comboBox_changeDB.addItems(dict_import_table.values())

        self.horizontalLayout.addWidget(self.comboBox_changeDB)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.pushButton_import = QPushButton(self.import_window)
        self.pushButton_import.setText("Импортировать из Excel")
        icon = QIcon()
        icon.addFile(os.getcwd() + main.create_settings()["settings"].value('/images_importDB/image_import'), QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_import.setIcon(icon)
        self.pushButton_import.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_import)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        QMetaObject.connectSlotsByName(self.import_window)

        self.import_window.show()

        self.btn_import_dir.clicked.connect(partial(self.open_dir, self.edit_line_dir_import))
        self.pushButton_import.clicked.connect(partial(self.validate_import, self.comboBox_changeDB))

    def open_dir(self, line_edit):
        cwd = os.getcwd()
        result = QtWidgets.QFileDialog.getOpenFileName(None, "Открыть файл", cwd + "/import", "Excel Files (*.xlsx)")
        line_edit.setText(result[0])

    def validate_import(self, comboBox) -> bool:
        s = self.edit_line_dir_import.text()
        if self.edit_line_dir_import.text() == "":
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Выберите файл для импорта",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()
            return False
        elif comboBox.currentText() == "Выберите таблицу для импорта...":
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Выберите таблицу для импорта",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()
            return False
        elif (s.split("/")[-1] == "bank_accounts.xlsx" and comboBox.currentText() == "Счета") or \
                (s.split("/")[-1] == "income.xlsx" and comboBox.currentText() == "Доходы") or \
                (s.split("/")[-1] == "expenses.xlsx" and comboBox.currentText() == "Расходы") or \
                (s.split("/")[-1] == "debt.xlsx" and comboBox.currentText() == "Долги") or \
                (s.split("/")[-1] == "plan_income.xlsx" and comboBox.currentText() == "Запланированные доходы") or \
                (s.split("/")[-1] == "plan_expenses.xlsx" and comboBox.currentText() == "Запланированные расходы"):
            import_xlsx(self.edit_line_dir_import.text(), comboBox.currentIndex())
            return True
        else:
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка",
                                 "Выбранный файл не совпадает с выбранной таблицей",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()
            return False
