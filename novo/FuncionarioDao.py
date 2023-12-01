import Conexao as conexao

conexao = conexao.ConexaoBancoDeDados(
    host="localhost", user="aluno", password="sptech", port=3306, database="StockSafe"
)

conexao.conexaoMySql()
cursor = conexao.conexao.cursor()


def listar():
    cursor.execute("SELECT id_funcionario, nome, email FROM tb_funcionario;")
    results = cursor.fetchall()
    return results


def getFuncionarioPorLogin(email, senha):
    cursor.execute(
        f"SELECT * FROM tb_funcionario WHERE email = %s AND senha = %s", (email, senha)
    )
    results = cursor.fetchall()
    return results

