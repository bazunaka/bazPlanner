from modules.database import DatabaseCategories

class Category:
    def __init__(self):
        pass

    def check_connect(self):
        self.connection_sqlite = DatabaseCategories.sqlite_open_db(DatabaseCategories.check_string_connect()["categories"])
        self.connection_qtsql = DatabaseCategories.qsql_connect_db(DatabaseCategories.check_string_connect()["categories"])
        self.cursor = self.connection_sqlite.cursor()
        if self.connection_sqlite and self.connection_qtsql:
            return True
        else:
            return False

    def set_attr(self):
        pass

    @staticmethod
    def show_cat(id_type):
        query = DatabaseCategories.select("categories", "name_category", where_field="id_type",
                                          where_value=id_type, order_by=False)
        model = DatabaseCategories.view_model_new(query)
        return model

    @staticmethod
    def show_sub_cat(name):
        query = DatabaseCategories.select("categories", "sub_categories.name_sub_cat",
                                          where_field="categories.name_category", where_value="'" + name + "'", order_by=False, inner_join=True,
                                          inner_join_field="sub_categories",
                                          inner_join_value="categories.id_cat=sub_categories.id_cat")
        model = DatabaseCategories.view_model_new(query)
        return model

    def add_category(self, name_category, id_type):
        self.check_connect()
        lst_values = [
            {"name_category": name_category, "id_type": id_type}
        ]
        DatabaseCategories.insert(self.connection_sqlite, lst_values)

    def add_subcategory(self, name_sub_cat, id_cat):
        self.check_connect()
        name_table = "sub_categories"
        lst_values = [
            {"name_sub_cat": name_sub_cat, "id_cat": id_cat}
        ]
        DatabaseCategories.insert(self.connection_sqlite, lst_values,
                                  table_name=name_table)

    def change_category(self, old_value: str, new_value: str):
        self.check_connect()
        name_table = "categories"
        name_column = "name_category"
        DatabaseCategories.update_into_table(self.connection_sqlite, name_table, name_column, new_value, old_value)

    def change_subcategory(self, old_value: str, new_value: str):
        self.check_connect()
        name_table = "sub_categories"
        name_column = "name_sub_cat"
        DatabaseCategories.update_into_table(self.connection_sqlite, name_table, name_column, new_value, old_value)

    @staticmethod
    def delete_category(value: str) -> bool:
        name_table = "categories"
        name_column = "name_category"
        DatabaseCategories.delete_from_table(name_table, name_column, value)
        return True

    @staticmethod
    def delete_subcategory(value: str) -> bool:
        name_table = "sub_categories"
        name_column = "name_sub_cat"
        DatabaseCategories.delete_from_table(name_table, name_column, value)
        return True
