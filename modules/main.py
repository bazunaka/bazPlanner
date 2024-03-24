import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QFrame

from PyQt5.QtWidgets import QMenuBar, QMenu, QStatusBar, QPushButton, QProgressBar, QHBoxLayout, QLineEdit, QFrame, \
    QVBoxLayout, QLabel, QWidget, QScrollArea, QCheckBox, QDateEdit, QDateTimeEdit, QListView, QGroupBox, QAction
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                          QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                         QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *

"""
Names of variables:
"""

title_window_application = "bazPlanner 0.0.1 - Планировщик задач"
title_application = "bazPlanner"

"""
Methods:
"""


def determine_size_monitor() -> list:
    size_monitor = QtWidgets.QDesktopWidget().availableGeometry()
    monitor_width = size_monitor.width()
    monitor_height = size_monitor.height()
    return [monitor_width, monitor_height]


def os_environ() -> None:
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"


def create_settings() -> dict:
    sett = os.getcwd() + "/config/resource_path.ini"
    sett2 = os.getcwd() + "/config/settings.ini"
    settings = QSettings(sett, QSettings.IniFormat)
    settings2 = QSettings(sett2, QSettings.IniFormat)
    return {"settings": settings, "settings2": settings2}


def create_frames(self, count):
    self.frame_2 = QFrame()
    self.frame_2.setObjectName(u"frame_2")
    self.frame_2.setFrameShape(QFrame.StyledPanel)
    self.frame_2.setFrameShadow(QFrame.Raised)
    # self.verticalLayout_9[count] = QVBoxLayout(self.frame_2)
    # self.verticalLayout_9[count].setObjectName(u"verticalLayout_9")
    self.label_3[count] = QLabel(self.frame_2)
    self.label_3[count].setObjectName(u"label_3")

    # self.verticalLayout_9[count].addWidget(self.label_3[count])

    self.horizontalLayout_6[count] = QHBoxLayout()
    self.horizontalLayout_6[count].setObjectName(u"horizontalLayout_6")
    self.lineEdit_3[count] = QLineEdit(self.frame_2)
    self.lineEdit_3[count].setObjectName(u"lineEdit_3")
    self.lineEdit_3[count].setFrame(True)
    self.lineEdit_3[count].setDragEnabled(False)
    self.lineEdit_3[count].setReadOnly(False)
    self.lineEdit_3[count].setClearButtonEnabled(False)

    self.horizontalLayout_6[count].addWidget(self.lineEdit_3[count])

    self.pushButton_12[count] = QPushButton(self.frame_2)
    self.pushButton_12[count].setObjectName(u"pushButton_12")

    self.horizontalLayout_6[count].addWidget(self.pushButton_12[count])

    self.pushButton_13[count] = QPushButton(self.frame_2)
    self.pushButton_13[count].setObjectName(u"pushButton_13")

    self.horizontalLayout_6[count].addWidget(self.pushButton_13[count])

    # self.verticalLayout_9[count].addLayout(self.horizontalLayout_6[count])

    self.progressBar_2[count] = QProgressBar(self.frame_2)
    self.progressBar_2[count].setObjectName(u"progressBar_2")
    self.progressBar_2[count].setValue(24)

    # self.verticalLayout_9[count].addWidget(self.progressBar_2[count])

    return self.frame_2
