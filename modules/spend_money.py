from modules.database import DatabaseProfits

class SpendMoney:
    def __init__(self):
        pass

    def check_connect(self):
        self.connection_sqlite = DatabaseProfits.sqlite_open_db(DatabaseProfits.check_string_connect()["profits"])
        self.connection_qtsql = DatabaseProfits.qsql_connect_db(DatabaseProfits.check_string_connect()["profits"])
        self.cursor = self.connection_sqlite.cursor()
        if self.connection_sqlite and self.connection_qtsql:
            return True
        else:
            return False