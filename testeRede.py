import time as t # tipo um setInterval
import psutil as ps
import pandas as pd
import os # compatibilidade com os sistemas

while True:
    for i in range(1):
        #Coletar dados dos pacotes na rede.
        pacotesRecebidos = ps.net_io_counters(pernic=False, nowrap=True)[3]
        pacotesErros = ps.net_io_counters(pernic=False, nowrap=True)[4]
        pacotesDescartados = ps.net_io_counters(pernic=False, nowrap=True)[6]
        pacotesTotal = (pacotesRecebidos + pacotesErros)
        pctPerda = pacotesRecebidos*(pacotesErros+pacotesDescartados)/100

        #Coletar dados da memória RAM.
        memoriaRamTotal = round((ps.virtual_memory()[0])*10**-9,2)
        memoriaRamDisponivel = round((ps.virtual_memory()[1])*10**-9,2)
        memoriaRamPercentual = round((ps.virtual_memory()[2])*10**-9,2)
        memoriaRamAtiva = round((ps.virtual_memory()[5])*10**-9,2)
        memoriaRamPartilhada = round((ps.virtual_memory()[9])*10**-9,2)

        
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
