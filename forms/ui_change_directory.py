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
from PyQt5.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                             QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
                             QToolButton, QVBoxLayout, QWidget)

dict_export_string = {"win32": "export_directory_win32", "macos": "export_directory"}
dict_backup_string = {"win32": "backup_directory_win32", "macos": "backup_directory"}

sett = os.getcwd() + "/config/settings.ini"
settings = QSettings(sett, QSettings.IniFormat)


class Ui_ChangeDirectory(object):

    def __init__(self):
        self.Form = QtWidgets.QWidget()

    def create_gui_change_directory(self):

        self.Form.setFixedSize(480, 105)
        self.Form.setWindowTitle("Настройки папок")

        self.gridLayout = QGridLayout(self.Form)
        self.verticalLayout = QVBoxLayout()
        self.horizontalLayout = QHBoxLayout()
        self.label_export_dir = QLabel(self.Form)
        self.label_export_dir.setText("Путь к папке для экспорта данных:")

        self.horizontalLayout.addWidget(self.label_export_dir)

        self.lineEdit_export_dir = QLineEdit(self.Form)

        self.horizontalLayout.addWidget(self.lineEdit_export_dir)

        self.toolButton_export_dir = QToolButton(self.Form)
        self.toolButton_export_dir.setText("...")

        self.horizontalLayout.addWidget(self.toolButton_export_dir)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.label_backup_dir = QLabel(self.Form)
        self.label_backup_dir.setText("Путь к папке для бэкапа данных:")

        self.horizontalLayout_2.addWidget(self.label_backup_dir)

        self.horizontalSpacer = QSpacerItem(11, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.lineEdit_backup_dir = QLineEdit(self.Form)
        self.lineEdit_backup_dir.setObjectName(u"lineEdit_backup_dir")

        self.horizontalLayout_2.addWidget(self.lineEdit_backup_dir)

        self.toolButton_backup_dir = QToolButton(self.Form)
        self.toolButton_backup_dir.setText("...")

        self.horizontalLayout_2.addWidget(self.toolButton_backup_dir)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton_save = QPushButton(self.Form)
        self.pushButton_save.setText("Сохранить изменения")

        self.verticalLayout.addWidget(self.pushButton_save)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        QMetaObject.connectSlotsByName(self.Form)
        self.Form.setWindowModality(Qt.ApplicationModal)
        self.Form.show()

        self.pushButton_save.setFocus()

        if sys.platform == "win32":
            self.check_directory_string(dict_backup_string['win32'], dict_export_string['win32'])
        else:
            self.check_directory_string(dict_backup_string['macos'], dict_export_string['macos'])

        self.pushButton_save.clicked.connect(self.btn_clicked_savefile)
        self.toolButton_export_dir.clicked.connect(partial(self.btn_clicked_openfile, self.lineEdit_export_dir))
        self.toolButton_backup_dir.clicked.connect(partial(self.btn_clicked_openfile, self.lineEdit_backup_dir))

    def check_directory_string(self, name_backup_string, name_export_string):
        self.lineEdit_export_dir.setText(
            settings.value(name_export_string + '/export_directory'))
        self.lineEdit_backup_dir.setText(
            settings.value(name_backup_string + '/backup_directory'))

    def btn_clicked_openfile(self, line_edit):
        cwd = os.getcwd()
        result = QtWidgets.QFileDialog.getExistingDirectory(None, "Выберите папку", cwd)
        if result == "":
            pass
        else:
            line_edit.setText(result)
    def btn_clicked_savefile(self):
        if sys.platform == "win32":
            settings.beginGroup('export_directory_win32')
            settings.setValue("export_directory", self.lineEdit_export_dir.text())
            settings.endGroup()
            settings.beginGroup('backup_directory_win32')
            settings.setValue("backup_directory", self.lineEdit_backup_dir.text())
            settings.endGroup()
        else:
            settings.beginGroup('export_directory')
            settings.setValue("export_directory", self.lineEdit_export_dir.text())
            settings.endGroup()
            settings.beginGroup('backup_directory')
            settings.setValue("backup_directory", self.lineEdit_backup_dir.text())
            settings.endGroup()
