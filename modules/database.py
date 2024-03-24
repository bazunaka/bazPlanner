import datetime
import os
import sqlite3
import sys

from PyQt5 import QtSql, QtWidgets
from PyQt5.QtCore import QSettings
from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QMessageBox

connection = QtSql.QSqlDatabase.addDatabase("QSQLITE")  # Driver for database.

# Path for settings.ini and create empty variable for connection strings.
settings_file_path = os.getcwd() + "/config/settings.ini"
settings = QSettings(settings_file_path, QSettings.IniFormat)
settings_connection_strings = ""

# Dictionaries for connection_strings from INI-file.
dict_settings_string = {"win32": "connection_strings_win32", "macos": "connection_strings"}
dict_connection_strings = {"main": ""}


class Database:

    @staticmethod
    def create_strings_connection(name_os: str) -> dict:
        """
        Create and insert connection strings from INI-file to dict_connection_strings.
        :arg: Name operating system: win32 or macOS.
        :return: Dictionary with connections strings from INI-file.
        """
        setting_string = dict_settings_string[name_os]
        dict_connection_strings["main"] = settings.value(setting_string + '/connection_string_maindb')
        return dict_connection_strings

    @staticmethod
    def check_string_connect() -> dict:
        """
        Check connections to database in INI-file.
        :arg: None.
        :return: Dictionary with connections strings from INI-file.
        """
        if os.path.exists(settings_file_path):
            if sys.platform == "win32":
                return Database.create_strings_connection("win32")
            else:
                return Database.create_strings_connection("macos")
        else:
            dialog = QMessageBox(QtWidgets.QMessageBox.Critical, "Ошибка", "Отсутствует файл настроек",
                                 buttons=QtWidgets.QMessageBox.Ok)
            dialog.exec()

    @staticmethod
    def qsql_connect_db(path_to_db_file) -> QtSql.QSqlDatabase:
        """
        Try to connect to databases using standard module QSQLDatabase.
        :param path_to_db_file:
        :return: connection.
        """
        try:
            connection.setDatabaseName(path_to_db_file)
            return connection
        except (FileNotFoundError, FileExistsError) as err:
            error = QMessageBox(QtWidgets.QMessageBox.Critical, err.__class__.__name__, str(err),
                                buttons=QtWidgets.QMessageBox.Ok)
            error.exec()

    @staticmethod
    def sqlite_open_db(path_to_db_file) -> sqlite3.connect:
        """
        Try to connect to databases using module sqlite3.
        :param path_to_db_file:
        :return: connection.
        """
        try:
            connect = sqlite3.connect(path_to_db_file)
            return connect
        except (FileNotFoundError, FileExistsError) as err:
            error = QMessageBox(QtWidgets.QMessageBox.Critical, err.__class__.__name__, str(err),
                                buttons=QtWidgets.QMessageBox.Ok)
            error.exec()

    @staticmethod
    def select(table_name, *fields_name, where=True, where_field="",
               where_value="", order_by=True, order_field="", order_value="ASC") -> str:
        """
        Create query string for function select from database.
        :param table_name:
        :param fields_name: list str
        :param where: bool
        :param where_field:
        :param where_value:
        :param order_by: bool
        :param order_field:
        :param order_value: default ASC
        :return: string query.
        """
        fields_format = ", ".join(fields_name)

        if where and order_by:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}" \
                    f"ORDER BY {order_field} {order_value}"
        elif where and not order_by:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}"
        elif not where and order_by:
            query = f"SELECT {fields_format} FROM {table_name} ORDER BY {order_field} {order_value}"
        else:
            query = f"SELECT {fields_format} FROM {table_name}"

        return query

    @staticmethod
    def view_model(dict_connection: str, query: str) -> QSqlQueryModel:
        """
        Create model for show in table_view.
        :param dict_connection: change name for database connection.
        :param query: string query.
        :return: model from query.
        """
        Database.qsql_connect_db(dict_connection_strings[dict_connection]).open()
        model = QSqlQueryModel()
        model.setQuery(query)
        return model

    @staticmethod
    def insert(connect, table_name, rows: list) -> None:
        """
        Insert data to database.
        :param connect: connection to database.
        :param table_name: change table.
        :param rows: list data for insert.
        :return: None.
        """
        fields_names = rows[0].keys()
        assert all(row.keys() == fields_names for row in rows[1:])

        fields_format = ", ".join(fields_names)
        values_placeholder_format = ", ".join([f'({", ".join(["?"] * len(fields_names))})'] * len(rows))
        query = f"INSERT INTO {table_name} ({fields_format}) VALUES {values_placeholder_format}"

        params = list()
        for row in rows:
            row_values = [row[field_name] for field_name in fields_names]
            params += row_values

        cursor = connect.cursor()
        cursor.execute(query, params)
        connect.commit()

    @staticmethod
    def select_all_from_tables_where(connection_db, table_name, column_name, condition):
        connection_db.open()
        model = QSqlQueryModel()
        query = QSqlQuery("select * from " + table_name + " where " + column_name + "=" + condition)
        model.setQuery(query)
        return model

    @staticmethod
    def insert_into_table(connect, table_name, value):
        cursor = connect.cursor()
        cursor.execute(f"INSERT INTO {table_name} VALUES ({value})")

    @staticmethod
    def update_into_table(connection_db, name_table, name_column, new_value, value):
        connection_db.open()
        update_str = "UPDATE {0} SET {1}=\'{2}\' WHERE {1}=\'{3}\'".format(name_table, name_column, new_value, value)
        model = QSqlQueryModel()
        query = QSqlQuery(update_str)
        model.setQuery(query)
        return model

    @staticmethod
    def delete_from_table(name_table: str, name_column: str, value: str):
        query = QSqlQuery("PRAGMA foreign_keys = ON")
        query.exec()
        delete_str = "DELETE FROM {0} WHERE {1}=\'{2}\'".format(name_table, name_column, value)
        query = QSqlQuery(delete_str)
        query.exec()


class DatabaseProject(Database):

    connection = Database.qsql_connect_db(dict_connection_strings["main"])

    @staticmethod
    def insert_month_payments(connect, month_count, month_pay, last_id):
        cursor = connect.cursor()
        i = 0
        now = datetime.datetime.now() + datetime.timedelta(days=30)
        while i < month_count:
            cursor.execute('INSERT INTO month_payments(date_payment, payment, id_calculation) VALUES(?, ?, ?)',
                           (now.strftime('%d-%m-%Y'), month_pay, last_id))
            connect.commit()
            now = now + datetime.timedelta(days=30)
            i += 1

    @staticmethod
    def insert(connect, rows: list, table_name="calculation_monthly_payment"):
        fields_names = rows[0].keys()
        assert all(row.keys() == fields_names for row in rows[1:])

        fields_format = ", ".join(fields_names)
        values_placeholder_format = ", ".join([f'({", ".join(["?"] * len(fields_names))})'] * len(rows))
        query = f"INSERT INTO {table_name} ({fields_format}) VALUES {values_placeholder_format}"

        params = list()
        for row in rows:
            row_values = [row[field_name] for field_name in fields_names]
            params += row_values

        cursor = connect.cursor()
        cursor.execute(query, params)
        connect.commit()

    @staticmethod
    def view_model(query, dict_connection="main") -> QSqlQueryModel:
        Database.qsql_connect_db(dict_connection_strings[dict_connection]).open()
        model = QSqlQueryModel()
        model.setQuery(query)
        return model

    @staticmethod
    def select(*fields_name, where=True, where_field="",
               where_value="", order_by=True, order_field="", order_value="ASC", table_name="projects"):
        fields_format = ", ".join(fields_name)

        if where and order_by:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}" \
                    f"ORDER BY {order_field} {order_value}"
        elif where and not order_by:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}"
        elif not where and order_by:
            query = f"SELECT {fields_format} FROM {table_name} ORDER BY {order_field} {order_value}"
        else:
            query = f"SELECT {fields_format} FROM {table_name}"

        return query

    @staticmethod
    def select_last_el() -> str:
        """
        Select last element for insert monthly_payment.
        :param
        :param
        :return: last element from table.
        """

        connection.open()
        query = QtSql.QSqlQuery()
        query.exec("select id_calc_per_month from calculation_monthly_payment order by id_calc_per_month DESC LIMIT 1")
        while query.next():
            last_el = query.value(0)
            return str(last_el)


class DatabaseBank(Database):

    @staticmethod
    def insert(rows: list, dict_connection="banks", table_name="name_banks"):

        connection = Database.qsql_connect_db(dict_connection_strings[dict_connection])
        connection.open()
        fields_names = rows[0].keys()
        assert all(row.keys() == fields_names for row in rows[1:])

        fields_format = ", ".join(fields_names)
        values_placeholder_format = ", ".join([f'({", ".join(["?"] * len(fields_names))})'] * len(rows))
        query_string = f"INSERT INTO {table_name} ({fields_format}) VALUES {values_placeholder_format}"

        query = QSqlQuery()
        query.prepare(query_string)

        for row in rows:
            for field_name in fields_names:
                query.addBindValue(row.get(field_name))
            query.exec()

    @staticmethod
    def select(*fields_name, table_name, where=True, where_field="",
               where_value="", order_by=True, order_field="", order_value="ASC") -> str:
        """
        Create query string for function select from database.
        :param table_name: change table.
        :param fields_name: list str.
        :param where: bool
        :param where_field:
        :param where_value:
        :param order_by: bool
        :param order_field:
        :param order_value: default ASC
        :return: string query.
        """
        fields_format = ", ".join(fields_name)

        if where and order_by:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}" \
                    f"ORDER BY {order_field} {order_value}"
        elif where and not order_by:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}"
        elif not where and order_by:
            query = f"SELECT {fields_format} FROM {table_name} ORDER BY {order_field} {order_value}"
        else:
            query = f"SELECT {fields_format} FROM {table_name}"

        return query

    @staticmethod
    def view_model(query: str, dict_connection="banks") -> QSqlQueryModel:
        """
        A static method to retrieve a QSqlQueryModel based on the provided query and database connection.

        Args:
            query (str): The SQL query to be executed.
            dict_connection (str): The key to look up the database connection string in dict_connection_strings. Default is "banks".

        Returns:
            QSqlQueryModel: The QSqlQueryModel containing the results of the provided query.
        """
        connection = Database.qsql_connect_db(dict_connection_strings[dict_connection])
        connection.open()
        model = QSqlQueryModel()
        model.setQuery(query)
        return model

    def select_name_for_combobox(self, name_table) -> list:
        lst_names = []
        dic = Database.create_strings_connection("macos")
        Database.qsql_connect_db(dic["banks"])
        self.model = QtSql.QSqlTableModel()
        self.model.setTable(name_table)
        self.model.select()
        for i in range(self.model.rowCount()):
            lst_names.append(self.model.record(i).value(1))
        return lst_names

    @staticmethod
    def update_into_table(connection_db, name_table, name_column, new_value, value):
        """
        Update into table.
        :param connection_db:
        :param name_table:
        :param name_column:
        :param new_value:
        :param value:
        :return:
        """
        connection_db.open()
        update_str = "update {0} set {1}=\'{2}\' where {1}=\'{3}\'".format(name_table, name_column, new_value, value)
        model = QSqlQueryModel()
        query = QSqlQuery(update_str)
        model.setQuery(query)
        return model

    def insert_combobox(self, name_table):
        pass

    @staticmethod
    def export_data() -> list:
        conn = Database.sqlite_open_db(dict_connection_strings["banks"])
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bank_accounts")
        results = cursor.fetchall()
        return results

    @staticmethod
    def delete_from_table(name_table: str, name_column: str, value: str):
        Database.qsql_connect_db(dict_connection_strings["banks"]).open()
        query = QSqlQuery("PRAGMA foreign_keys = ON")
        query.exec()
        delete_str = "DELETE FROM {0} WHERE {1}=\'{2}\'".format(name_table, name_column, value)
        query = QSqlQuery(delete_str)
        query.exec()

class DatabaseMortgage(Database):

    @staticmethod
    def insert(connect, rows: list, table_name="calculation_monthly_payment"):
        fields_names = rows[0].keys()
        assert all(row.keys() == fields_names for row in rows[1:])

        fields_format = ", ".join(fields_names)
        values_placeholder_format = ", ".join([f'({", ".join(["?"] * len(fields_names))})'] * len(rows))
        query = f"INSERT INTO {table_name} ({fields_format}) VALUES {values_placeholder_format}"
        print(query)

        params = list()
        for row in rows:
            row_values = [row[field_name] for field_name in fields_names]
            params += row_values

        cursor = connect.cursor()
        cursor.execute(query, params)
        connect.commit()

    @staticmethod
    def select(table_name, *fields_name, where=True, where_field="",
               where_value="", order_by=True, order_field="", order_value="ASC"):
        fields_format = ", ".join(fields_name)

        if where and order_by:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}" \
                    f"ORDER BY {order_field} {order_value}"
        elif where and not order_by:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}"
        elif not where and order_by:
            query = f"SELECT {fields_format} FROM {table_name} ORDER BY {order_field} {order_value}"
        else:
            query = f"SELECT {fields_format} FROM {table_name}"

        return query


class DatabaseDeposits(Database):

    @staticmethod
    def insert(connect, rows: list, table_name="calculate_deposits"):
        fields_names = rows[0].keys()
        assert all(row.keys() == fields_names for row in rows[1:])

        fields_format = ", ".join(fields_names)
        values_placeholder_format = ", ".join([f'({", ".join(["?"] * len(fields_names))})'] * len(rows))
        query = f"INSERT INTO {table_name} ({fields_format}) VALUES {values_placeholder_format}"
        print(query)

        params = list()
        for row in rows:
            row_values = [row[field_name] for field_name in fields_names]
            params += row_values

        cursor = connect.cursor()
        cursor.execute(query, params)
        connect.commit()

    @staticmethod
    def select(table_name="calculate_deposits", *fields_name, where=True, where_field="",
               where_value="", order_by=True, order_field="", order_value="ASC"):
        fields_format = ", ".join(fields_name)

        if where and order_by:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}" \
                    f" ORDER BY {order_field} {order_value}"
        elif where and not order_by:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}"
        elif not where and order_by:
            query = f"SELECT {fields_format} FROM {table_name} ORDER BY {order_field} {order_value}"
        else:
            query = f"SELECT {fields_format} FROM {table_name}"

        return query


class DatabaseCategories(Database):

    @staticmethod
    def select(table_name, *fields_name, where=True, where_field="",
               where_value="", order_by=True, order_field="", order_value="ASC", inner_join=False, inner_join_field="",
               inner_join_value=""):

        fields_format = ", ".join(fields_name)

        if where and order_by:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}" \
                    f" ORDER BY {order_field} {order_value}"
        elif where and not order_by and inner_join:
            query = f"SELECT {fields_format} FROM {table_name} INNER JOIN {inner_join_field} ON {inner_join_value}" \
                     f" WHERE {where_field}={where_value}"
        elif where and not order_by and not inner_join:
            query = f"SELECT {fields_format} FROM {table_name} WHERE {where_field}={where_value}"
        elif not where and order_by and inner_join:
            query = f"SELECT {fields_format} FROM {table_name} ORDER BY {order_field} {order_value}"
        else:
            query = f"SELECT {fields_format} FROM {table_name}"

        return query

    @staticmethod
    def view_model_new(query):
        """
        Static method to create and return a QSqlQueryModel based on the given query.
        """
        Database.qsql_connect_db(dict_connection_strings["categories"]).open()
        model = QSqlQueryModel()
        model.setQuery(query)
        return model

    @staticmethod
    def insert(connect, rows: list, table_name="categories"):
        fields_names = rows[0].keys()
        assert all(row.keys() == fields_names for row in rows[1:])

        fields_format = ", ".join(fields_names)
        values_placeholder_format = ", ".join([f'({", ".join(["?"] * len(fields_names))})'] * len(rows))
        query = f"INSERT INTO {table_name} ({fields_format}) VALUES {values_placeholder_format}"

        params = list()
        for row in rows:
            row_values = [row[field_name] for field_name in fields_names]
            params += row_values

        cursor = connect.cursor()
        cursor.execute(query, params)
        connect.commit()

    @staticmethod
    def update_into_table(connection_db, name_table, name_column, new_value, value):
        connection_db.open()
        update_str = "update {0} set {1}=\'{2}\' where {1}=\'{3}\'".format(name_table, name_column, new_value, value)
        model = QSqlQueryModel()
        query = QSqlQuery(update_str)
        model.setQuery(query)
        return model

    @staticmethod
    def delete_from_table(name_table: str, name_column: str, value: str):
        Database.qsql_connect_db(dict_connection_strings["categories"]).open()
        query = QSqlQuery("PRAGMA foreign_keys = ON")
        query.exec()
        delete_str = "DELETE FROM {0} WHERE {1}=\'{2}\'".format(name_table, name_column, value)
        query = QSqlQuery(delete_str)
        query.exec()


class DatabaseProfits(Database):
    pass
