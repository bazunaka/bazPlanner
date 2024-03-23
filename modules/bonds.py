
import requests
import os
from urllib import parse

from modules import database


class Bonds:
    def __init__(self):
        self.connection_sqlite = database.Database.sqlite_open_db(os.getcwd() + "/databases/credits.db")
        self.connection_qtsql = database.Database.qsql_connect_db(os.getcwd() + "/databases/credits.db")
        self.cursor = self.connection_sqlite.cursor()

    @staticmethod
    def query(method: str, **kwargs):
        """
        Отправляем запрос к ISS MOEX
        :param method:
        :param kwargs:
        :return:
        """
        try:
            url = "https://iss.moex.com/iss/%s.json" % method
            if kwargs: url += "?" + parse.urlencode(kwargs)
            r = requests.get(url)
            r.encoding = 'utf-8'
            j = r.json()
            print(j['securities']['columns'])
            print(j['securities']['data'])
            return j
        except Exception as e:
            print("Query error %s" % str(e))
            return None

