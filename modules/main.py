import os

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings

"""
Names of variables:
"""




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
