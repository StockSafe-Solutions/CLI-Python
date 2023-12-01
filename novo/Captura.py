import Conexao as conexao

conexao = conexao.ConexaoBancoDeDados(
    host="localhost", user="aluno", password="sptech", port=3306, database="StockSafe"
)

conexao.conexaoMySql()
cursor = conexao.conexao.cursor()

def inserirRegistros(idServer, categoria, valor):
    valor = int(valor)
    cursor.execute(
        "INSERT INTO tb_registro VALUES (null, %s, %s, NOW(), %s);",
        (idServer, categoria, valor),
    )
    conexao.conexao.commit()

