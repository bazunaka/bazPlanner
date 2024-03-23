from PyQt5.QtCore import (QMetaObject, Qt)

from PyQt5.QtWidgets import (QCheckBox, QComboBox, QGridLayout, QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
                             QWidget)

import modules.database
from modules import database


class Ui_ChangeBankAcc(QWidget):

    def __init__(self, parent=None):
        super(Ui_ChangeBankAcc, self).__init__(parent)

        self.change_bank_accounts_window = QWidget()

    def setupUi(self, name_window: str, name_click: str, lst_old_values=None) -> None:
        """
        Set up the UI with the provided window name, click name, and list of old values.
        """
        self.change_bank_accounts_window.setWindowTitle(name_window)
        self.change_bank_accounts_window.setWindowModality(Qt.ApplicationModal)
        self.change_bank_accounts_window.setMinimumSize(370, 155)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_bank_accounts_window.sizePolicy().hasHeightForWidth())
        self.change_bank_accounts_window.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.change_bank_accounts_window)
        self.verticalLayout = QVBoxLayout()
        self.combobox_change_bank = QComboBox(self.change_bank_accounts_window)

        self.verticalLayout.addWidget(self.combobox_change_bank)

        self.combobox_change_type_acc = QComboBox(self.change_bank_accounts_window)

        self.verticalLayout.addWidget(self.combobox_change_type_acc)

        self.edit_name = QLineEdit(self.change_bank_accounts_window)
        self.edit_name.setPlaceholderText("Введите имя счета")

        self.verticalLayout.addWidget(self.edit_name)

        self.edit_summary = QLineEdit(self.change_bank_accounts_window)
        self.edit_summary.setPlaceholderText("Введите сумму")

        self.verticalLayout.addWidget(self.edit_summary)

        self.check_active = QCheckBox(self.change_bank_accounts_window)
        self.check_active.setText("Счет закрыт")

        self.verticalLayout.addWidget(self.check_active)

        self.btn_save = QPushButton(self.change_bank_accounts_window)
        self.btn_save.setText("Сохранить")

        self.verticalLayout.addWidget(self.btn_save)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        QMetaObject.connectSlotsByName(self.change_bank_accounts_window)

        self.change_bank_accounts_window.show()

        self.combobox_change_bank.addItems(self.show_name_banks())
        self.combobox_change_type_acc.addItems(self.show_type_acc())
        self.btn_save.clicked.connect(self.add_record)

        if name_click == "change":
            self.btn_save.setText("Изменить")
            self.set_attr(lst_old_values)

    def show_name_banks(self):
        self.ui = modules.database.DatabaseBank()
        self.lst = self.ui.select_name_for_combobox('name_banks')
        self.lst.insert(0, "Выберите банк...")
        return self.lst

    def show_type_acc(self):
        self.ui = modules.database.DatabaseBank()
        self.lst = self.ui.select_name_for_combobox('type_bank_accounts')
        self.lst.insert(0, "Выберите тип счета...")
        return self.lst

    def add_record(self):
        lst_fields = [
            {"id_bank": str(self.combobox_change_bank.currentIndex()),
             "id_type": str(self.combobox_change_type_acc.currentIndex()),
             "name_bank_acc": "test", "summary": str(self.edit_summary.text()),
             "create_date": "01-01-2024", "isActive": "1"}
        ]

        modules.database.DatabaseBank.insert(lst_fields, table_name="bank_accounts")

    def set_attr(self, lst_values):
        name_bank = lst_values[1]
        self.combobox_change_bank.setCurrentIndex(lst_values.index(name_bank))
        # self.combobox_change_type_acc.setCurrentIndex(lst_values[2])
        self.edit_summary.setText(str(lst_values[3]))
        # self.check_active.setChecked(lst_values[4])
