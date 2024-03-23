import os

from PyQt5.QtCore import Qt

from modules import database

path_to_db = database.Database.create_strings_connection("macos")


class Bank:

    name_bank = None

    def set_attr(self, lst_value):
        if lst_value[0].text() == "":
            pass
        else:
            self.name_bank = lst_value[0].text()

    def add_bank(self):
        lst_fields = [
            {"name_bank": self.name_bank}
        ]
        database.DatabaseBank.insert(lst_fields)


    @staticmethod
    def change_bank(connection, name_bank, new_name):
        model = database.Database.update_into_table(connection, name_table="name_banks", name_column="name_bank",
                                                    value=name_bank, new_value=new_name)
        return model

    def delete_bank(self):
        pass

    @staticmethod
    def select_name_bank() -> database.DatabaseBank.view_model:
        """
        Selects the name of the bank from the database and returns it as a view model.
        :return: The name of the bank as a view model.
        """
        query_name_bank = database.DatabaseBank.select("name_bank", table_name="name_banks", where=False, order_by=False)
        model = database.DatabaseBank.view_model(query_name_bank)
        model.setHeaderData(0, Qt.Orientation.Horizontal, "Название банка")
        return model

    @staticmethod
    def select_bank_acc() -> database.DatabaseBank.view_model:
        query_name_bank = database.DatabaseBank.select("name_bank", table_name="name_banks", where=False,
                                                       order_by=False)
        model = database.DatabaseBank.view_model(query_name_bank)
        model.setHeaderData(0, Qt.Orientation.Horizontal, "Название банка")
        return model
