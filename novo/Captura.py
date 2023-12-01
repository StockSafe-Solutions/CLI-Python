import Conexao as conexao

conexao = conexao.ConexaoBancoDeDados(
    host="localhost", user="aluno", password="sptech", port=3306, database="StockSafe"
)

conexao.conexaoMySql()
cursor = conexao.conexao.cursor()


def inserirRegistros(idServer, categoria, valor):
    valor = int(valor)
    print("Dados do insert: ", idServer, categoria, valor)
    # Convert string value to float
    cursor.execute(
        "INSERT INTO tb_registro VALUES (null, %d, %d, NOW(), %d);",
        (idServer, categoria, valor),
    )
    print("Registro inserido: ")
