from functools import partial

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QRect, QMetaObject, Qt

from forms import (ui_name_banks, ui_connectDB, ui_exportDB, ui_importDB, ui_credit_calc, ui_savings_deposits,
                   ui_mortgage_calc, ui_savings_bonds, ui_categories, ui_profits, ui_bank_accounts, ui_change_directory,
                   ui_main_information, ui_backupDB, ui_restoreDB)

from modules.database import Database
from modules import main

s = "Успешное подключение к БД."

class Ui_MainWindow(object):

    def __init__(self):
        """
        Initialize the main window and set up the menu with various QAction items for different menu options.
        """
        super().__init__()
        self.menubar = None
        self.statusBar = None
        self.mdi = QtWidgets.QMdiArea()

        """
        Check connect to Databases.
        """
        self.dict_connections = Database.check_string_connect()

        """
        QActions for menu Home Finance.
        """
        self.menu_profit = QtWidgets.QAction("Доходы")
        self.menu_spend_money = QtWidgets.QAction("Расходы")
        self.menu_bank_accounts = QtWidgets.QAction("Счета в банках")
        self.menu_planning = QtWidgets.QAction("Планирование")
        self.menu_budget = QtWidgets.QAction("Бюджет")
        self.menu_debts = QtWidgets.QAction("Долги")

        """
        QAction for menu Service.
        """
        self.menu_import_db = QtWidgets.QAction("Импортировать данные в БД")
        self.menu_export_db = QtWidgets.QAction("Экспортировать данные из БД")
        self.menu_backup_db = QtWidgets.QAction("Создать резервную копию БД")
        self.menu_restore_db = QtWidgets.QAction("Восстановить резервную копию БД")
        self.menu_delete_db = QtWidgets.QAction("Очистить БД...")

        """
        QAction for menu Dictionaries.
        """
        self.menu_banks = QtWidgets.QAction("Список банков")
        self.menu_type_profits = QtWidgets.QAction("Категории доходов")
        self.menu_type_spend_money = QtWidgets.QAction("Категории расходов")

        """
        QAction for menu Information.
        """
        self.menu_about = QtWidgets.QAction("О программе")

        """
        QAction for menu Finance Calculator.
        """
        self.menu_mortgage = QtWidgets.QAction("Ипотечный калькулятор")
        self.menu_credit = QtWidgets.QAction("Кредитный калькулятор")

        """
        QAction for menu Settings.
        """
        self.menu_connect_db = QtWidgets.QAction("Подключение к БД")
        self.menu_change_directory = QtWidgets.QAction("Рабочие директории")

        """
        QAction for menu Savings.
        """
        self.calc_deposits = QtWidgets.QAction("Доходность вкладов")
        self.calc_bonds = QtWidgets.QAction("Доходность облигаций")
        self.calc_stocks = QtWidgets.QAction("Доходность акций")

        """
        QAction for menu Reports.
        """
        self.report_profit = QtWidgets.QAction("Отчет о доходах")
        self.report_spend_money = QtWidgets.QAction("Отчет о расходах")

        """
        Create QMenu.
        """
        self.information = QtWidgets.QMenu("Справка", self.menubar)
        self.settings = QtWidgets.QMenu("Настройки", self.menubar)
        self.dictionaries = QtWidgets.QMenu("Справочники", self.menubar)
        self.finance_calculator = QtWidgets.QMenu("Финансовые калькуляторы", self.menubar)
        self.menu_savings = QtWidgets.QMenu("Калькулятор сбережений", self.finance_calculator)
        self.home_finance = QtWidgets.QMenu("Домашняя бухгалтерия", self.menubar)
        self.service_menu = QtWidgets.QMenu("Сервис", self.menubar)
        self.reports_menu = QtWidgets.QMenu("Отчеты", self.menubar)

    def setupUi(self, MainWindow):
        """
        Set up the user interface for the main window.
        This function takes the MainWindow parameter and sets its size,
        minimum size, and title. It also sets the font for the MainWindow
        and initializes the menu bar, central widget, status bar, and various
        menu actions. Additionally, it connects various triggers to their
        corresponding functions.
        """
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(1000, 700)
        MainWindow.setWindowTitle(main.title_window_application)

        font = QtGui.QFont()
        font.setFamily("Helvetica")
        MainWindow.setFont(font)

        self.menubar = QtWidgets.QMenuBar(MainWindow)

        MainWindow.setCentralWidget(self.mdi)
        # self.mdi.setStyleSheet("background-color: #EEEEEE;")
        # self.centralwidget = QWidget(MainWindow)

        # MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setMenuBar(self.menubar)

        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        if Database.check_string_connect():
            self.statusBar.showMessage(s, 5000)
        else:
            self.statusBar.showMessage("Ошибка при подключении к БД.")
        MainWindow.setStatusBar(self.statusBar)

        self.service_menu.addAction(self.menu_import_db)
        self.service_menu.addAction(self.menu_export_db)
        self.service_menu.addSeparator()
        self.service_menu.addAction(self.menu_backup_db)
        self.service_menu.addAction(self.menu_restore_db)
        self.service_menu.addSeparator()
        self.service_menu.addAction(self.menu_delete_db)

        self.home_finance.addAction(self.menu_profit)
        self.home_finance.addAction(self.menu_spend_money)
        self.home_finance.addAction(self.menu_bank_accounts)
        self.home_finance.addSeparator()
        self.home_finance.addAction(self.menu_debts)
        self.home_finance.addSeparator()
        self.home_finance.addAction(self.menu_planning)

        self.finance_calculator.addAction(self.menu_credit)
        self.finance_calculator.addAction(self.menu_mortgage)

        self.finance_calculator.addMenu(self.menu_savings)
        self.menu_savings.addAction(self.calc_deposits)
        self.menu_savings.addAction(self.calc_bonds)
        self.menu_savings.addAction(self.calc_stocks)

        self.dictionaries.addAction(self.menu_banks)
        self.dictionaries.addAction(self.menu_type_profits)
        self.dictionaries.addAction(self.menu_type_spend_money)

        self.settings.addAction(self.menu_connect_db)
        self.settings.addAction(self.menu_change_directory)

        self.reports_menu.addAction(self.report_profit)
        self.reports_menu.addAction(self.report_spend_money)

        self.information.addAction(self.menu_about)

        self.menubar.addAction(self.service_menu.menuAction())
        self.menubar.addAction(self.home_finance.menuAction())
        self.menubar.addAction(self.finance_calculator.menuAction())
        self.menubar.addAction(self.dictionaries.menuAction())
        self.menubar.addAction(self.settings.menuAction())
        self.menubar.addAction(self.reports_menu.menuAction())
        self.menubar.addAction(self.information.menuAction())

        self.menu_banks.triggered.connect(partial(self.show_window_name_banks, name_window="Список банков",
                                                  name_db=self.dict_connections["banks"]))
        self.menu_type_profits.triggered.connect(partial(self.show_window_categories, "Категории доходов",
                                                         "2", self.statusBar))
        self.menu_type_spend_money.triggered.connect(partial(self.show_window_categories, "Категории расходов",
                                                             "1", self.statusBar))

        self.menu_about.triggered.connect(self.show_window_about)
        self.menu_connect_db.triggered.connect(self.show_window_connectdb)
        self.menu_change_directory.triggered.connect(self.show_window_change_directory)
        self.menu_export_db.triggered.connect(self.show_window_exportdb)
        self.menu_import_db.triggered.connect(self.show_window_importdb)
        self.menu_backup_db.triggered.connect(self.show_window_backupdb)
        self.menu_restore_db.triggered.connect(self.show_window_restoredb)
        self.menu_credit.triggered.connect(partial(self.show_window_credit, self.mdi, self.statusBar))
        self.menu_mortgage.triggered.connect(partial(self.show_window_mortgage, self.mdi))
        self.calc_deposits.triggered.connect(partial(self.show_window_savings, self.mdi))
        self.calc_bonds.triggered.connect(partial(self.show_window_savings_bonds, self.mdi))
        self.menu_profit.triggered.connect(partial(self.show_window_profits, self.mdi, self.statusBar))
        # self.menu_spend_money.triggered.connect(partial(self.show_window_profits, self.mdi, self.statusBar))
        self.menu_bank_accounts.triggered.connect(self.show_window_bank_accounts)

        QMetaObject.connectSlotsByName(MainWindow)

        self.ui = ui_main_information.Ui_Form()
        self.ui.setupUi(self.mdi)

    def show_window_name_banks(self, name_window, name_db):
        """
        Displays a window with a dictionary interface based on the given window and database names.

        :param name_window: The name of the window to display.
        :param name_db: The name of the database to use for the dictionary.
        :return: None
        """
        self.dict = QtWidgets.QMainWindow()
        self.ui = ui_name_banks.Ui_NameBanks()
        self.ui.create_GUI(name_window, name_db)

    def show_window_about(self):
        self.about = QtWidgets.QMessageBox()
        self.about.about(None, "О программе", "Программа для учета финансов. Написана на Python 3.9 "
                                              "с использованием библиотеки PyQt5. Версия программы 0.0.2")

    def show_window_connectdb(self):
        self.window_connectdb = QtWidgets.QWidget()
        self.ui = ui_connectDB.Ui_WindowConnectDB()
        self.ui.create_gui_connectdb()

    def show_window_exportdb(self) -> None:
        self.window_exportdb = QtWidgets.QWidget()
        self.ui = ui_exportDB.Ui_WindowExportDB()
        self.ui.create_gui_exportdb()

    def show_window_importdb(self) -> None:
        self.window_importdb = QtWidgets.QWidget()
        self.ui = ui_importDB.Ui_WindowImportDB()
        self.ui.create_gui_importdb()

    def show_window_credit(self, mdi, statusBar) -> None:
        self.window_credit = QtWidgets.QWidget()
        self.ui = ui_credit_calc.Ui_WindowCreditCalc()
        self.ui.create_gui_credit_calc(mdi, statusBar)

    def show_window_mortgage(self, mdi) -> None:
        self.window_mortgage = QtWidgets.QWidget()
        self.ui = ui_mortgage_calc.Ui_WindowMortgageCalc()
        self.ui.create_gui_mortgage_calc(mdi)

    def show_window_savings(self, mdi) -> None:
        self.window_savings = QtWidgets.QWidget()
        self.ui = ui_savings_deposits.Ui_WindowSavingsDeposit()
        self.ui.create_gui_savings_deposit(mdi)

    def show_window_savings_bonds(self, mdi) -> None:
        self.window_savings_bonds = QtWidgets.QWidget()
        self.ui = ui_savings_bonds.Ui_WindowSavingsBonds()
        self.ui.create_gui_savings_bonds(mdi)

    def show_window_categories(self, name_window, id_type, statusbar) -> None:
        self.window_categories = QtWidgets.QWidget()
        self.ui = ui_categories.Ui_DictionaryCategories()
        self.ui.create_gui_categories(name_window, id_type, statusbar)

    def show_window_profits(self, mdi, statusBar) -> None:
        self.window_profits = QtWidgets.QWidget()
        self.ui = ui_profits.Ui_Profits()
        self.ui.create_gui_profits(mdi, statusBar)

    def show_window_bank_accounts(self) -> None:
        self.window_bank_accounts = QtWidgets.QWidget()
        self.ui = ui_bank_accounts.Ui_BankAccount()
        self.ui.create_gui_bank_account()

    def show_window_change_directory(self) -> None:
        self.window_change_directory = QtWidgets.QWidget()
        self.ui = ui_change_directory.Ui_ChangeDirectory()
        self.ui.create_gui_change_directory()

    def show_window_backupdb(self) -> None:
        self.window_backupdb = QtWidgets.QWidget()
        self.ui = ui_backupDB.Ui_WindowBackupDB()
        self.ui.create_gui_backupdb()

    def show_window_restoredb(self) -> None:
        self.window_restoredb = QtWidgets.QWidget()
        self.ui = ui_restoreDB.Ui_WindowRestoreDB()
        self.ui.create_gui_restoredb()
