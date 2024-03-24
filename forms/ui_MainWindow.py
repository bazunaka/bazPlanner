from PyQt5.QtWidgets import QMenuBar, QMenu, QStatusBar, QPushButton, QProgressBar, QHBoxLayout, QLineEdit, QFrame, \
    QVBoxLayout, QLabel, QWidget, QScrollArea, QCheckBox, QDateEdit, QDateTimeEdit, QListView, QGroupBox, QAction
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
                          QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
                         QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from modules import main
from forms import ui_frame


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        MainWindow.setWindowTitle(main.title_window_application)
        MainWindow.setMinimumSize(QSize(main.determine_size_monitor()[0] * 0.5,
                                        main.determine_size_monitor()[1] * 0.3))

        self.action   = QAction(MainWindow)
        self.action_2 = QAction(MainWindow)
        self.action_4 = QAction(MainWindow)
        self.action_5 = QAction(MainWindow)
        self.action_6 = QAction(MainWindow)
        self.action_7 = QAction(MainWindow)

        self.centralwidget = QWidget(MainWindow)
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(371, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")

        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setTitle("Проекты")

        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setText("Добавить проект")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setText("Удалить проект")

        self.listView = QListView(self.groupBox)

        self.checkBox = QCheckBox(self.groupBox)
        self.checkBox.setText("Показывать завершенные проекты")

        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addWidget(self.listView)
        self.verticalLayout_2.addWidget(self.checkBox)

        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setTitle("Задачи")

        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setText("Сегодня")
        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setText("Предстоящие")
        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setText("Календарь")

        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addWidget(self.pushButton_4)
        self.verticalLayout.addWidget(self.pushButton_5)

        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.horizontalLayout_5.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)

        self.verticalLayout_10 = QVBoxLayout(self.widget_2)

        self.label = QLabel(self.widget_2)
        self.label.setText("Имя проекта")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)

        self.verticalLayout_10.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.widget_3 = QWidget(self.widget_2)
        self.verticalLayout_4 = QVBoxLayout(self.widget_3)
        self.horizontalLayout = QHBoxLayout()

        self.pushButton_6 = QPushButton(self.widget_3)
        self.pushButton_6.setText("Добавить раздел")
        self.pushButton_7 = QPushButton(self.widget_3)
        self.pushButton_7.setText("Переименовать раздел")
        self.pushButton_8 = QPushButton(self.widget_3)
        self.pushButton_8.setText("Удалить раздел")

        self.horizontalLayout.addWidget(self.pushButton_6)
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.horizontalLayout.addWidget(self.pushButton_8)

        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.listView_2 = QListView(self.widget_3)

        self.verticalLayout_4.addWidget(self.listView_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.verticalLayout_7 = QVBoxLayout(self.widget_4)
        self.lineEdit = QLineEdit(self.widget_4)
        self.lineEdit.setPlaceholderText("Название задачи")

        self.verticalLayout_7.addWidget(self.lineEdit)

        self.horizontalLayout_2 = QHBoxLayout()
        self.verticalLayout_5 = QVBoxLayout()

        self.checkBox_2 = QCheckBox(self.widget_4)
        self.checkBox_2.setText("Начало задачи")
        self.checkBox_2.setChecked(True)

        self.verticalLayout_5.addWidget(self.checkBox_2)

        self.dateEdit = QDateEdit(self.widget_4)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDateTime(QDateTime.currentDateTime())

        self.verticalLayout_5.addWidget(self.dateEdit)
        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()

        self.checkBox_3 = QCheckBox(self.widget_4)
        self.checkBox_3.setText("Конец задачи")
        self.checkBox_3.setChecked(True)

        self.verticalLayout_6.addWidget(self.checkBox_3)

        self.dateEdit_2 = QDateEdit(self.widget_4)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_2.setDateTime(QDateTime.currentDateTime())

        self.verticalLayout_6.addWidget(self.dateEdit_2)

        self.horizontalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_7.addLayout(self.horizontalLayout_2)

        self.pushButton_9 = QPushButton(self.widget_4)
        self.pushButton_9.setText("Добавить задачу")

        self.verticalLayout_7.addWidget(self.pushButton_9)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.widget_4)

        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.scrollArea = QScrollArea(self.widget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        # self.scrollAreaWidgetContents = QWidget()
        # self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        # self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 709, 301))
        # self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        # self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame = QFrame()
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(14)
        self.label_2.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFrame(True)
        self.lineEdit_2.setDragEnabled(False)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setClearButtonEnabled(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_2)

        self.pushButton_10 = QPushButton(self.frame)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.horizontalLayout_4.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.horizontalLayout_4.addWidget(self.pushButton_11)

        self.verticalLayout_8.addLayout(self.horizontalLayout_4)

        self.progressBar = QProgressBar(self.frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout_8.addWidget(self.progressBar)

        # self.verticalLayout_9.addWidget(self.frame)
        # self.verticalLayout_9.addWidget(self.frame)
        # self.verticalLayout_9.addWidget(self.frame)

        # self.verticalLayout_9.addWidget(main.create_frames(self, 2))
        # self.verticalLayout_9.addWidget(main.create_frames(self, 3))
        # self.verticalLayout_9.addWidget(main.create_frames(self, 4))
        # self.verticalLayout_9.addWidget(main.create_frames(self, 5))
        # self.verticalLayout_9.addWidget(main.create_frames(self, 6))

        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setWidget(self.frame)
        self.scrollArea.setWidget(self.frame)
        self.scrollArea.setWidget(self.frame)

        self.verticalLayout_10.addWidget(self.scrollArea)

        self.horizontalLayout_5.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1124, 21))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_4)
        self.menu.addAction(self.action_5)
        self.menu.addAction(self.action_6)
        self.menu_2.addAction(self.action_7)

        QMetaObject.connectSlotsByName(MainWindow)

