import mysql.connector
import mysql.connector.errorcode
import time as t # tipo um setInterval
import psutil as ps
import pandas as pd
import os # compatibilidade com os sistemas

conexao = mysql.connector.connect(
            host= "localhost",
            user= "aluno",
            password= "sptech",
            port= 3306,
            database="portoes_do_inferno"
)
comando = conexao.cursor()

while True:
    for i in range(1):
        #Coletar dados dos pacotes na rede.
        pacotesRecebidos = ps.net_io_counters(pernic=False, nowrap=True)[3]
        pacotesErros = ps.net_io_counters(pernic=False, nowrap=True)[4]
        pacotesDescartados = ps.net_io_counters(pernic=False, nowrap=True)[6]
        pacotesTotal = (pacotesRecebidos + pacotesErros)
        pctPerda = pacotesRecebidos*(pacotesErros+pacotesDescartados)/100

        #Coletar dados da memória RAM.
        memoriaRamTotal =  1 #round((ps.virtual_memory()[0])*10**-9,2)
        memoriaRamDisponivel = 1 #round((ps.virtual_memory()[1])*10**-9,2)
        memoriaRamPercentual = 1 #round((ps.virtual_memory()[2])*10**-9,2)
        memoriaRamAtiva = 1 #round((ps.virtual_memory()[5])*10**-9,2)
        memoriaRamPartilhada = 1 #round((ps.virtual_memory()[9])*10**-9,2)

        
        #Cria dataframe para visualização
        dataPacotes = {
            "Dados": [f"{pacotesRecebidos:,.0f}", f"{pacotesErros:,.2f}", f"{pacotesDescartados:,.2f}", f"{pacotesTotal:,.0f}", f"{(round(pctPerda/100000,2))}"],
        }
        dataRam = {
            "Dados": [f"{memoriaRamTotal:,.2f}", f"{memoriaRamDisponivel:,.2f}", f"{memoriaRamPercentual:,.2f}", f"{memoriaRamAtiva:,.2f}", f"{memoriaRamPartilhada:,.2f}"]
        }


        dfRede = pd.DataFrame(dataPacotes, index = ["Pacotes recebidos:", "pacotes com erro:", "Pacotes descartados:", "Total:", "Percentual de perda:"])#Cria os titulos da tabela
        dfRam = pd.DataFrame(dataRam, index=["Memória RAM total", "Memória RAM disponível", "Memória RAM percentual", "Memória RAM ativa", "Memória RAM compartilhada"])


        print(f"{'Monitoramento da rede'}\n{'='*50}\n{dfRede}\n{'='*50}\n") # printa os dados no console
        print(f"{'Monitoramento da memória RAM'}\n{'='*50}\n{dfRam}\n{'='*50}\n") # printa os dados no console
        t.sleep(5)
        os.system('cls' if os.name == 'nt' else 'clear')#Limpa dados do console

           #Inserção de valores da CPU
        try:
                comando.execute(f"""INSERT INTO registro VALUES (NULL,NOW(), {pacotesRecebidos}, 2004, 3),
                                                                (NULL,NOW(), {pacotesErros}, 2004, 3),
                                                                (NULL,NOW(),{pacotesDescartados}, 2004, 3)
                                                                ;""")
                conexao.commit()
                print("Foi [acotes]")
        except mysql.connector.Error as Erro:
                    print('Erro ao inserir os dados ', Erro)
        try:
                comando.execute(f"""INSERT INTO registro VALUES (NULL, NOW(), {memoriaRamTotal}, 2000, 1),
                                                                (NULL, NOW(), {memoriaRamDisponivel}, 2001, 1),
                                                                (NULL, NOW(), {memoriaRamPercentual}, 2001, 1),
                                                                (NULL, NOW(), {memoriaRamAtiva}, 2001, 1),
                                                                (NULL, NOW(), {memoriaRamPartilhada}, 2001, 1)
                                                                ;""")
                conexao.commit()
                print("Foi memoria")
        except mysql.connector.Error as Erro:
                print('Erro ao inserir os dados1 ', Erro)
