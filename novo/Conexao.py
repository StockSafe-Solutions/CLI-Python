import mysql.connector
import mysql.connector.errorcode
import pymssql


class Conexao:
    def __init__(self, host, user, password, port, database):
        self.host = host
        self.user = user
        self.password = password
        self.port = port
        self.database = database

    def conexaoMySql(self):
      try:
          conexao = mysql.connector.connect(
              host=self.host,
              user=self.user,
              password=self.password,
              port=self.port,
              database=self.database,
          )
          print("A conexão MYSQL realizada com sucesso!")
      except mysql.connector.Error as err:
          print("Erro na conexão no MYSQL",err.msg)
          return None
      return conexao

    def conexaoSqlServer(host, database, user,password):
      try:
          conn = pymssql.connect(
              server= host,
              database=database,
              user=user,
              password=password,
          )
          print("A conexão SQL Server realizada com sucesso!")
          return conn
      except pymssql.OperationalError as err:
          print("Erro na conexão no MYSQL",err.msg)
          return None

    def fecharConexaoMySql():
      comando.close()
      conexao.close()

    def fecharConexaoSqlServer():
        cursor.close()
        conn.close()
