import mysql.connector
import mysql.connector.errorcode
import pymssql
import pymysql


class ConexaoBancoDeDados:
    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database

    def conexaoMySql(self):
        try:
            self.conexao = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                port=self.port,
                database=self.database,
            )
        except mysql.connector.Error as err:
            print("Erro na conexão no MYSQL", err.msg)
            return None
        return self.conexao

    def conexaoSqlServer(self, host, database, user, password):
        try:
            self.conn = pymssql.connect(
                server=host,
                database=database,
                user=user,
                password=password,
            )
            print("A conexão SQL Server realizada com sucesso!")
            return self.conn
        except pymssql.OperationalError as err:
            print("Erro na conexão no SQL Server", err.msg)
            return None

