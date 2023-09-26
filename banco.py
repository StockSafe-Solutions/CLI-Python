import mysql.connector
import mysql.connector.errorcode


conexao = mysql.connector.connect(
    host= "localhost",
    user= "stockSafe",
    password= "urubu100",
    port= 3306,
    database="StockSafe"
);

comando = conexao.cursor();

#Função para inserir a memória
def inserirMemoria(finalMem):
    try:
        comando.execute(f"INSERT INTO registro VALUES (NULL, NOW(), {finalMem}, 2000, 1);")
        conexao.commit()
    except mysql.connector.Error as Erro:
        print('Erro ao inserir os dados ', Erro)
#função para inserir o disco
def inserirDisco(finalDisk):
    try:
        comando.execute(f"INSERT INTO registro VALUES (NULL, NOW(), {finalDisk}, 2000, 2);")
        conexao.commit()
    except mysql.connector.Error as Erro:
        print('Erro ao inserir os dados ', Erro)
#Função para inserir a CPU
def inserirCPU(finalCPU):
    try:
        comando.execute(f"INSERT INTO registro VALUES (NULL, NOW(), {finalCPU}, 2000, 3);")
        conexao.commit()
    except mysql.connector.Error as Erro:
        print('Erro ao inserir os dados ', Erro)    


# comando.execute("SELECT * FROM registro");
# resultado = comando.fetchall()
# print(resultado);