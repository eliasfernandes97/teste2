import sqlite3

class AppBD():
    def __init__(self):
        self.creat_table()
    def abrirConexão(self):
        try:
            self.connection = sqlite3.connect('database.db')
        except sqlite3.Error as error:
            print("Falha ao se conectar ao banco de dados error", error)
    def creat_table(self):
        self.abrirConexão()
        create_table_query = """
        CREATE TABLE IF NOT EXISTS products(
            id INTERGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        );"""
        try:
         cursor= self.connection.cursor()
         cursor.execute(create_table_query)
         self.connection.commit()
        except sqlite3.Error as error:
            print("Falha ao criar a tabela",error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o sqlite foi fechado")
    def inserirDados(self,name,price):
        self.abrirConexão()
        insert_query=""" INSER INTO products(name, price) VALUES(?,?"""
        try:
            cursor = self.connection.cursor()

''''''


