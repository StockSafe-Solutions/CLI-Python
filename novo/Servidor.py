import Conexao as conexao

conexao = conexao.ConexaoBancoDeDados(
    host="localhost", user="aluno", password="sptech", port=3306, database="StockSafe"
)

conexao.conexaoMySql()
cursor = conexao.conexao.cursor()


def autenticarSerrvidor(codigo):
    cursor.execute(
        "SELECT id_servidor, codigo FROM tb_servidor WHERE codigo = %s", (codigo)
    )
    results = cursor.fetchall()
    for row in results:
        print(row)


def selecionarServidor(codigoFuncionario, codidoServidor):
    cursor.execute("UPDATE tb_servidor SET id_autenticador = %s WHERE codigo = %s", (codigoFuncionario, codidoServidor))
    results = cursor.fetchall()
    for row in results:
        print(row)
