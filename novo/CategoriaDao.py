import Conexao as conexao

conexao = conexao.ConexaoBancoDeDados(
    host="localhost", user="stockSafe", password="urubu100", port=3306, database="StockSafe"
)

conexao.conexaoMySql()
cursor = conexao.conexao.cursor()


def inserirDadosCategoria(tipoCategoria, uninade):
    contador = 40002
    cursor.execute(
        "INSERT INTO tb_categoria (id_cat, tipo_cat, unidade_cat) VALUES (%d, %s, %s);",
        (contador,tipoCategoria, uninade),
    )
    contador + 1
