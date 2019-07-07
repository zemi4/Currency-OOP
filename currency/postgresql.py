import psycopg2
from psycopg2 import sql


class PostgresQL:
    # открытие БД
    def __init__(self, db_name, user, password, host, port):
        self.DB_NAME = db_name
        self.USER = user
        self.PASSWORD = password
        self.HOST = host
        self.PORT = port
        self.DB = psycopg2.connect(dbname=self.DB_NAME, user=self.USER, password=self.PASSWORD,
                                   host=self.HOST, port=self.PORT)
        self.CURSOR = self.DB.cursor()
        self.DB.autocommit = True

    # Открывать и закрывает КУРСОР (дает право на внесение изменений)
    def open_or_close_cursor(self, status):
        if status == 'OPEN':
            self.CURSOR = self.DB.cursor()
        elif status == 'CLOSE':
            self.CURSOR.close()

    # Создание таблицы
    def create_table(self, name_table, table_settings):
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('CREATE TABLE ' + name_table + '(' + table_settings + ');'))
        self.open_or_close_cursor('CLOSE')

    # удаление таблицы
    def delete_table(self, name_table):
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('DROP TABLE ' + name_table + ';'))
        self.open_or_close_cursor('CLOSE')

    # Заполнение таблицы данными"
    def insert_data(self, name_table, values):
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('INSERT INTO ' + name_table + ' VALUES {}').format(
                                        sql.SQL(',').join(map(sql.Literal, values))))
        self.open_or_close_cursor('CLOSE')

    # Выводит СПИСОК, каждый элемент это КОРТЕЖ (таблица), в КОРТЕЖЕ элементы (параметры таблицы)
    def show_database(self):
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('SELECT * FROM information_schema.tables WHERE table_schema=\'public\''))
        list_of_table = self.CURSOR.fetchall()  # Возвращает список всех строк
        self.open_or_close_cursor('CLOSE')
        return list_of_table

    # Выводит СПИСОК, каждый элемент это КОРТЕЖ (строка из таблицы)
    def show_table(self, name_table):
        self.open_or_close_cursor('OPEN')
        self.CURSOR.execute(sql.SQL('SELECT * FROM ' + name_table))
        list_of_strings = self.CURSOR.fetchall()  # Возвращает список всех строк
        self.open_or_close_cursor('CLOSE')
        return list_of_strings

    # Возвращает True если таблица существует
    def check_table(self, name_table):
        for table in self.show_database():
            if table[2] == name_table:
                return True
        return False

    # Очистка всех строк из таблицы
    def clear_table(self, name_table):
        if self.check_table(name_table):
            self.open_or_close_cursor('OPEN')
            self.CURSOR.execute(sql.SQL('DELETE FROM ' + name_table))
            self.open_or_close_cursor('CLOSE')


