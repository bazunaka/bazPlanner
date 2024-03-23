import os
import sys

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication

from forms import ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_MainWindow.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    os.environ["QT_SCALE_FACTOR"] = "1"
    app = QApplication(sys.argv)  # создает объект приложения в виде экземпляра класса QApplication
    app.setApplicationName("bazPlanner - Планировщик задач")
    app.setApplicationVersion("0.0.1")
    app.setApplicationDisplayName("bazPlanner")
    app.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps)
    window = MainWindow()  # загрузка UI-файла с формой
    desktop = QtWidgets.QApplication.desktop()
    x = (desktop.width() - window.width()) // 2
    y = (desktop.height() - window.height()) // 2
    window.move(x, y)
    window.show()
    sys.exit(app.exec_())


