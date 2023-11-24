import mysql.connector
import mysql.connector.errorcode
from time import sleep
import psutil
import botSlack

def maquina(flag):
        parar = flag
        contador = 0
        conexao = mysql.connector.connect(
            host= "localhost",
            user= "StockSafe",
            password= "urubu100",
            port= 3306,
            database="StockSafe"
        )
        comando = conexao.cursor()
        mediaCPU = 0
        while True:
            sleep(1)
            freqCPU = psutil.cpu_percent()
            usoDisco = psutil.disk_usage("/")
            mem = psutil.virtual_memory()
            print(mem)
            
            freqCPU2 = freqCPU + (freqCPU * 0.1)
            mem2 = mem[2] + (mem[2] * 0.1)
            usoDisco2 = usoDisco[3] + (usoDisco[3] * 0.1)

            mediaCPU += freqCPU
            contador += 1
           

            if contador == 10:
                mediaCPU = mediaCPU / contador;
                if mediaCPU >= 60:
                 botSlack.abrir_chamado(round(mediaCPU,2))
                contador = 0
                mediaCPU = 0


            #Inserção de valores da CPU
            try:
                comando.execute(f"""INSERT INTO tb_registro (fk_servidor, fk_cat, data_hora, valor) VALUES (2000, 2, 2023-10-23 14:00:00, {freqCPU - 0.1}),
                                                                                                           (2001, 2, 2023-10-23 14:00:00, {freqCPU2 - 0.1});""")
                conexao.commit()
            except mysql.connector.Error as Erro:
                    print('Erro ao inserir os dados ', Erro)
            try:
                comando.execute(f"""INSERT INTO tb_registro (fk_servidor, fk_cat, data_hora, valor) VALUES (2000, 3, 2023-10-23 14:00:00, {mem[2]}),
                                                                                                           (2001, 3, 2023-10-23 14:00:00, {mem2})""")
                conexao.commit()
            except mysql.connector.Error as Erro:
                print('Erro ao inserir os dados1 ', Erro)
            if parar:
                break
     