from functools import partial

from PyQt5 import QtWidgets, QtCore, QtGui

from forms import ui_add_change_cat
from modules import categories


def delete_cat(lst):
    name = lst.currentIndex().data()
    if categories.Category.delete_category(name):
        print("Категория " + name + " удалена")
    else:
        print("Категория " + name + " не удалена")


def delete_sub_cat(lst):
    name = lst.currentIndex().data()
    if categories.Category.delete_subcategory(name):
        print("Подкатегория " + name + " удалена")
    else:
        print("Подкатегория " + name + " не удалена")


class Ui_DictionaryCategories(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(Ui_DictionaryCategories, self).__init__(parent)

        self.grid = None
        self.cat_window = None
        self.cat_lst_view = None
        self.sub_cat_lst_view = None
        self.change_button_cat = QtWidgets.QPushButton("Изменить")
        self.del_button_cat = QtWidgets.QPushButton("Удалить")
        self.add_button_cat = QtWidgets.QPushButton("Добавить")

        self.change_button_subcat = QtWidgets.QPushButton("Изменить")
        self.del_button_subcat = QtWidgets.QPushButton("Удалить")
        self.add_button_subcat = QtWidgets.QPushButton("Добавить")

        self.categories_window = QtWidgets.QWidget()

        self.categories = categories.Category()
        self.change_window = ui_add_change_cat.Ui_AddChangeCategory()

    def show_sub_cat(self, lst):
        name = lst.indexes()[0].data()
        model = categories.Category.show_sub_cat(name)
        self.sub_cat_lst_view.setModel(model)
        return name

    def print_current(self, lst):
        old_name = lst.currentIndex().data()
        self.change_window.create_GUI("Изменить", "change",  old_name_cat=old_name)

    def create_gui_categories(self, name_window, id_type, statusBar):
        Ui_DictionaryCategories.count = + 1
        self.statusbar = statusBar

        self.categories_window.setWindowTitle(name_window)
        self.categories_window.setFixedSize(600, 450)

        self.cat_lst_view = QtWidgets.QListView(self.cat_window)
        self.sub_cat_lst_view = QtWidgets.QListView(self.cat_window)

        self.grid = QtWidgets.QGridLayout()
        self.grid.addWidget(self.cat_lst_view, 0, 0, 1, 3)
        self.grid.addWidget(self.sub_cat_lst_view, 0, 3, 1, 3)
        self.grid.addWidget(self.add_button_cat, 1, 0, 1, 1)
        self.grid.addWidget(self.change_button_cat, 1, 1, 1, 1)
        self.grid.addWidget(self.del_button_cat, 1, 2, 1, 1)
        self.grid.addWidget(self.add_button_subcat, 1, 3, 1, 1)
        self.grid.addWidget(self.change_button_subcat, 1, 4, 1, 1)
        self.grid.addWidget(self.del_button_subcat, 1, 5, 1, 1)

        self.categories_window.setLayout(self.grid)
        self.categories_window.setWindowModality(QtCore.Qt.ApplicationModal)

        self.categories_window.show()

        if self.categories.check_connect():
            statusBar.showMessage("Вы успешно подключились к БД Категории.", 5000)
        else:
            statusBar.showMessage("Не удалось подключиться к БД Категории.")

        self.cat_lst_view.setModel(categories.Category.show_cat(id_type))
        self.cat_lst_view.selectionModel().selectionChanged.connect(self.show_sub_cat)

        self.del_button_cat.clicked.connect(partial(delete_cat, self.cat_lst_view))
        self.add_button_cat.clicked.connect(partial(self.change_window.create_GUI, "Добавить категорию", "add"))
        self.change_button_cat.clicked.connect(partial(self.print_current, self.cat_lst_view))

        self.del_button_subcat.clicked.connect(partial(delete_sub_cat, self.sub_cat_lst_view))
        self.add_button_subcat.clicked.connect(partial(self.change_window.create_GUI, "Добавить подкатегорию", "add"))
        self.change_button_subcat.clicked.connect(partial(self.print_current, self.sub_cat_lst_view))

        # if "banks" in name_db:
        #     self.dict_tbl_view.setModel(bank.Bank.select_name_bank(connection))
        #     self.dict_tbl_view.setColumnWidth(0, 250)
        #     connection.close()
        # elif "credits" in name_db:
        #     self.dict_tbl_view.setModel(credit.Credit.select_type_calc(connection))
        #     self.dict_tbl_view.setColumnWidth(0, 250)
        #     connection.close()

        # if connection:
        #     if name_db == "banks.db":
        #         self.dict_tbl_view.setModel(bank.Bank.select_name_bank(connection))
        #         connection.close()
        #     else:
        #         model = database.Database.select_from_tables(connection, dictionary_tables["calc_types"], "type_name")
        #         self.dict_tbl_view.setModel(model)
        #         self.add_button.setEnabled(False)
        #         self.del_button.setEnabled(False)
        #         self.change_button.setEnabled(False)
        #         connection.close()
        # else:
        #     print("Error")

        # self.add_button.clicked.connect(partial(self.change_window.create_GUI, name_window="Добавить", name_click="add"))
