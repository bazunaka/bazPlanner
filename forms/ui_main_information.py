from PyQt5 import QtWidgets
from PyQt5.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_Form(QtWidgets.QWidget):


    count = 0
    def setupUi(self, mdi):
        Ui_Form.count += 1
        self.main_info_window = QtWidgets.QWidget()
        self.main_info_window.setFixedSize(980, 620)

        self.gridLayout = QGridLayout(self.main_info_window)

        mdi.addSubWindow(self.main_info_window)

        '''
        This block about information.
        '''
        self.groupBox_information = QGroupBox(self.main_info_window)
        self.groupBox_information.setTitle("Общая информация")

        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_information)

        self.verticalLayout = QVBoxLayout()

        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()

        self.label_summary_money = QLabel(self.groupBox_information)
        self.label_summary_money.setText("Всего средств:")

        self.horizontalLayout.addWidget(self.label_summary_money)

        self.label = QLabel(self.groupBox_information)
        self.label.setText("Test1")
        self.label.setAlignment(Qt.AlignRight)

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.label_all_summary_profit = QLabel(self.groupBox_information)
        self.label_all_summary_profit.setText("Всего доходов:")

        self.horizontalLayout_2.addWidget(self.label_all_summary_profit)

        self.label_2 = QLabel(self.groupBox_information)
        self.label_2.setText("Test2")
        self.label_2.setAlignment(Qt.AlignRight)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()

        self.label_all_spend_money = QLabel(self.groupBox_information)
        self.label_all_spend_money.setText("Всего расходов:")

        self.horizontalLayout_3.addWidget(self.label_all_spend_money)

        self.label_3 = QLabel(self.groupBox_information)
        self.label_3.setText("Test3")
        self.label_3.setAlignment(Qt.AlignRight)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_4 = QHBoxLayout()

        self.label_profit_month = QLabel(self.groupBox_information)
        self.label_profit_month.setText("Доход за месяц:")

        self.horizontalLayout_4.addWidget(self.label_profit_month)

        self.label_profit_money = QLabel(self.groupBox_information)
        self.label_profit_money.setText("Test4")
        self.label_profit_money.setAlignment(Qt.AlignRight)

        self.horizontalLayout_4.addWidget(self.label_profit_money)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()

        self.label_spend_month = QLabel(self.groupBox_information)
        self.label_spend_month.setText("Расход за месяц:")

        self.horizontalLayout_5.addWidget(self.label_spend_month)

        self.label_spend_money = QLabel(self.groupBox_information)
        self.label_spend_money.setText("Test5")
        self.label_spend_money.setAlignment(Qt.AlignRight)

        self.horizontalLayout_5.addWidget(self.label_spend_money)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()

        self.label_different = QLabel(self.groupBox_information)
        self.label_different.setText("Разница:")

        self.horizontalLayout_6.addWidget(self.label_different)

        self.label_summary_month = QLabel(self.groupBox_information)
        self.label_summary_month.setText("Test6")
        self.label_summary_month.setAlignment(Qt.AlignRight)

        self.horizontalLayout_6.addWidget(self.label_summary_month)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.horizontalLayout_7.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.groupBox_information, 5, 1, 1, 1)

        '''
        Left block tables.
        '''
        self.label_name_banks_acc_table = QLabel(self.main_info_window)
        self.label_name_banks_acc_table.setText("Банковские счета")
        self.gridLayout.addWidget(self.label_name_banks_acc_table, 0, 0, 1, 1)

        self.tableView_bank_accounts = QTableView(self.main_info_window)
        self.gridLayout.addWidget(self.tableView_bank_accounts, 1, 0, 1, 1)

        self.label_name_spend_table = QLabel(self.main_info_window)
        self.label_name_spend_table.setText("Расходы")
        self.gridLayout.addWidget(self.label_name_spend_table, 2, 0, 1, 1)

        self.tableView_debt = QTableView(self.main_info_window)
        self.gridLayout.addWidget(self.tableView_debt, 4, 0, 1, 1)

        '''
        Graphics profit and spend money.
        '''
        self.label_5 = QLabel(self.main_info_window)
        self.label_5.setText("Графики доходов и расходов")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.graphicsView = QGraphicsView(self.main_info_window)
        self.graphicsView_categories = QGraphicsView(self.main_info_window)

        self.gridLayout.addWidget(self.graphicsView, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.graphicsView_categories, 3, 1, 2, 1)

        '''
        Right table view for nearest spend money.
        '''
        self.label_6 = QLabel(self.main_info_window)
        self.label_6.setText("Ближайшие расходы")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)

        self.tableView = QTableView(self.main_info_window)
        self.gridLayout.addWidget(self.tableView, 1, 2, 5, 1)

        self.main_info_window.show()

    # def retranslateUi(self, Form):
    #     Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi