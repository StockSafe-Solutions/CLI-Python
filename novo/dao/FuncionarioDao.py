import Conexao

Banco = Conexao.Conexao(
    host="localhost", user="aluno", password="sptech", port=3306, database="StockSafe"
)

Banco.teste()
