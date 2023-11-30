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
        
    def conexaoMySql(host, user, password, port, database):
      try:
          conexao = mysql.connector.connect(
              host=host,
              user=user,
              password=password,
              port=port,
              database=database,
          )
      except mysql.connector.Error as err:
          print(err.msg)
          return None

      return conexao


    def conexaoSqlServer(host, user, database, password):
      try:
          conn = pymssql.connect(
              server=host,
              database=database,
              user=user,
              password=password,
          )
          cursor = conn.cursor()
          return conn, cursor
      except pymssql.OperationalError as err:
          print(err.msg)
          return None, None


    def fecharConexaoMySql():
      comando.close()
      conexao.close()

    def fecharConexaoSqlServer():
        cursor.close()
        conn.close()
