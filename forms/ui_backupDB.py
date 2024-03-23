import os
import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtCore import (QMetaObject, QSize, Qt, QSettings, QRect)
from PyQt5.QtGui import (QIcon, QPixmap)
from PyQt5.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                             QLabel, QPushButton, QSizePolicy, QVBoxLayout,
                             QWidget, QMessageBox)

from modules import backupDB, main

title_window = "Создать резервную копию БД"
first_item_combobox = "Выберите БД для резервной копии"
text_pushbutton = "Создать резервную копию БД"

lst_export_table = ["banks.db", "credit.db", "categories.db", "profits.db", "deposits.db", "bonds.db"]
dict_export_table = {"1": "banks.db",
                     "2": "credit.db",
                     "3": "Расходы",
                     "4": "Долги",
                     "5": "Запланированные доходы",
                     "6": "Запланированные расходы"}


class Ui_WindowBackupDB(QtWidgets.QWidget):

    def create_gui_backupdb(self):
        main.os_environ()

        self.backup_window = QtWidgets.QWidget()
        self.backup_window.setWindowTitle(title_window)
        if sys.platform == "darwin":
            self.backup_window.setFixedSize(380, 145)
        else:
            self.backup_window.setFixedSize(350, 109)
        self.backup_window.setWindowModality(Qt.ApplicationModal)

        self.horizontalLayout_3 = QHBoxLayout(self.backup_window)

        self.verticalLayout = QVBoxLayout()

        self.horizontalLayout = QHBoxLayout()

        self.icon_change_db = QLabel(self.backup_window)
        self.icon_change_db.setEnabled(True)

        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(22)
        sizePolicy.setVerticalStretch(22)
        sizePolicy.setHeightForWidth(self.icon_change_db.sizePolicy().hasHeightForWidth())

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

        self.comboBox_changeDB = QComboBox(self.backup_window)
        self.comboBox_changeDB.addItem(first_item_combobox)
        self.comboBox_changeDB.addItems(lst_export_table)

        self.horizontalLayout.addWidget(self.comboBox_changeDB)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()

        self.icon_dir = QLabel(self.backup_window)

        sizePolicy.setHeightForWidth(self.icon_dir.sizePolicy().hasHeightForWidth())

        self.icon_dir.setSizePolicy(sizePolicy)
        self.icon_dir.setMinimumSize(QSize(22, 22))
        self.icon_dir.setMaximumSize(QSize(22, 22))
        self.icon_dir.setPixmap(QPixmap(os.getcwd() + main.create_settings()["settings"].value('/images_exportDB/image_dir')))
        self.icon_dir.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.icon_dir)

        self.label_dir_export = QLabel(self.backup_window)
        if sys.platform == "darwin":
            self.label_dir_export.setText(main.create_settings()["settings2"].value('/backup_directory/backup_directory'))
        else:
            self.label_dir_export.setText(main.create_settings()["settings2"].value('/backup_directory_win32/backup_directory'))

        self.horizontalLayout_2.addWidget(self.label_dir_export)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_export = QPushButton(self.backup_window)
        self.pushButton_export.setText(text_pushbutton)
        icon = QIcon()
        icon.addFile(os.getcwd() + main.create_settings()["settings"].value('/images_exportDB/image_export'), QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_export.setIcon(icon)
        self.pushButton_export.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_export)

        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.horizontalLayout_3.setGeometry(QRect(0, 0, 350, 50))

        QMetaObject.connectSlotsByName(self.backup_window)

        self.backup_window.show()

        self.pushButton_export.clicked.connect(partial(self.validate_export))

    def validate_export(self) -> bool:
        if self.comboBox_changeDB.currentText() == first_item_combobox:
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Выберите БД для резервной копии",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()
            return False
        else:
            backupDB.do_backup(self.comboBox_changeDB.currentText())
            return True
