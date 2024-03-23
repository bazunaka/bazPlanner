import os
import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                          QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QSettings)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                                   QFont, QFontDatabase, QGradient, QIcon,
                                   QImage, QKeySequence, QLinearGradient, QPainter,
                                   QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt5.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
                             QLabel, QPushButton, QSizePolicy, QVBoxLayout,
                             QWidget, QMessageBox)

from modules.export_db import export_xlsx
from modules import main

sett = os.getcwd() + "/config/resource_path.ini"
sett2 = os.getcwd() + "/config/settings.ini"
settings = QSettings(sett, QSettings.IniFormat)
settings2 = QSettings(sett2, QSettings.IniFormat)

lst_export_table = ["Счета", "Доходы", "Расходы", "Долги", "Запланированные доходы", "Запланированные расходы"]
dict_export_table = {"bank_accounts": "Счета",
                     "2": "Доходы",
                     "3": "Расходы",
                     "4": "Долги",
                     "5": "Запланированные доходы",
                     "6": "Запланированные расходы"}

class Ui_WindowExportDB(QtWidgets.QWidget):

    def create_gui_exportdb(self):
        main.os_environ()

        self.export_window = QtWidgets.QWidget()
        self.export_window.setWindowTitle("Экспортировать из БД")
        if sys.platform == "darwin":
            self.export_window.setFixedSize(main.determine_size_monitor()[0] * 0.33, 145)
        else:
            self.export_window.setFixedSize(350, 109)

        self.export_window.setWindowModality(Qt.ApplicationModal)

        self.horizontalLayout_3 = QHBoxLayout(self.export_window)

        self.verticalLayout = QVBoxLayout()

        self.horizontalLayout = QHBoxLayout()

        self.icon_change_db = QLabel(self.export_window)
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
        self.icon_change_db.setPixmap(QPixmap(os.getcwd() + settings.value('/images_exportDB/image_changedb')))
        self.icon_change_db.setScaledContents(True)
        self.icon_change_db.setWordWrap(False)

        self.horizontalLayout.addWidget(self.icon_change_db)

        self.comboBox_changeDB = QComboBox(self.export_window)
        self.comboBox_changeDB.addItem(
            "Выберите таблицу для экспорта..."
        )
        self.comboBox_changeDB.addItems(lst_export_table)

        self.horizontalLayout.addWidget(self.comboBox_changeDB)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()

        self.icon_dir = QLabel(self.export_window)

        sizePolicy.setHeightForWidth(self.icon_dir.sizePolicy().hasHeightForWidth())

        self.icon_dir.setSizePolicy(sizePolicy)
        self.icon_dir.setMinimumSize(QSize(22, 22))
        self.icon_dir.setMaximumSize(QSize(22, 22))
        self.icon_dir.setPixmap(QPixmap(os.getcwd() + settings.value('/images_exportDB/image_dir')))
        self.icon_dir.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.icon_dir)

        self.label_dir_export = QLabel(self.export_window)
        if sys.platform == "darwin":
            self.label_dir_export.setText(settings2.value('/export_directory/export_directory'))
        else:
            self.label_dir_export.setText(settings2.value('/export_directory_win32/export_directory'))

        self.horizontalLayout_2.addWidget(self.label_dir_export)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_export = QPushButton(self.export_window)
        self.pushButton_export.setText("Экспортировать в Excel")
        icon = QIcon()
        icon.addFile(os.getcwd() + settings.value('/images_exportDB/image_export'), QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_export.setIcon(icon)
        self.pushButton_export.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_export)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        QMetaObject.connectSlotsByName(self.export_window)

        self.export_window.show()

        self.pushButton_export.clicked.connect(partial(self.validate_export))

    def validate_export(self) -> bool:
        if self.comboBox_changeDB.currentText() == "Выберите таблицу для экспорта...":
            dialog = QMessageBox(QtWidgets.QMessageBox.Warning, "Ошибка", "Выберите таблицу для экспорта",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()
            return False
        else:
            export_xlsx(self.comboBox_changeDB.currentText())
            return True
