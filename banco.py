import mysql.connector
import mysql.connector.errorcode


conexao = mysql.connector.connect(
    host= "localhost",
    user= "stockSafe",
    password= "urubu100",
    port= 3306,
    database="StockSafe"
)

comando = conexao.cursor()

#Função para inserir a memória
def inserirMemoria(finalMem):
    try:
        comando.execute(f"INSERT INTO tb_registro (fk_servidor, fk_cat, data_hora, uso_ram) VALUES (2000, 3, 2023-10-23 12:00:00, {finalMem});")
        conexao.commit()
    except mysql.connector.Error as Erro:
        print('Erro ao inserir os dados ', Erro)

#Função para inserir a CPU
def inserirCPU(finalCPU):
    try:
        comando.execute(f"INSERT INTO tb_registro (fk_servidor, fk_cat, data_hora, valor) VALUES (2000, 2, 2023-10-23 12:00:00, {finalCPU});")
        conexao.commit()
    except mysql.connector.Error as Erro:
        print('Erro ao inserir os dados ', Erro)    


