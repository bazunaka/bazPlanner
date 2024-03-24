from PyQt5.QtWidgets import QVBoxLayout, QTextEdit, QComboBox, QLabel
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Frame(object):
    def setupUi(self):
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9[count] = QVBoxLayout(self.frame_2)
        self.verticalLayout_9[count].setObjectName(u"verticalLayout_9")
        self.label_3[count] = QLabel(self.frame_2)
        self.label_3[count].setObjectName(u"label_3")

        self.verticalLayout_9[count].addWidget(self.label_3[count])

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

        self.verticalLayout_9[count].addLayout(self.horizontalLayout_6[count])

        self.progressBar_2[count] = QProgressBar(self.frame_2)
        self.progressBar_2[count].setObjectName(u"progressBar_2")
        self.progressBar_2[count].setValue(24)

        self.verticalLayout_9[count].addWidget(self.progressBar_2[count])


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.label.setText(QCoreApplication.translate("Frame", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"TextLabel", None))
    # retranslateUi

