#imports de bibliotecas
import tkinter as tk
from tkinter import *
import psutil
import threading
import dadosMaquina
#imports de outros arquivos
import time
import banco
import documento



janela = Tk()
janela.title("Dados atuais da maquina")

global qtd
global mensagem
global mensagem_final
global mediaCPU
global estaRodando
global thread2

estaRodando = False

texto = Label(janela, text="O que você deseja monitorar?")
texto.grid(column=15, row=0, padx=10, pady=3)

# Botão para monitoramento da CPU
botaoCPU = Button(janela, text="CPU", command=lambda: exibir_CPU())
botaoCPU.grid(column=15, row=5, padx=10, pady=3)

# Botão para monitoramento da RAM
botaoRAM = Button(janela, text="RAM", command=lambda: exibir_memoria())
botaoRAM.grid(column=15, row=6, padx=10, pady=3)

# botão para o monitoramento de disco
botaoDisco = Button(janela, text="Disco", command=lambda: exibir_disco())
botaoDisco.grid(column=15, row=7, padx=10, pady=10)


#Label para mostrar a mensagem de analise
mensagem = Label(janela, text='')
mensagem.grid(column= 15, row= 20, padx= 3, pady= 3)

#label para mostrar o andamento da CPU
label_CPU = Label(janela, text='')
label_CPU.grid(column=0, row=0, padx=3, pady=3)

#label para mostrar o andamento da memória
label_Mem = Label(janela, text='')
label_Mem.grid(column=0, row=1, padx=3, pady=3)

#label para mostrar o andamento do disco
label_disco = Label(janela, text='')
label_disco.grid(column=0, row=2, padx=3, pady=3)

#label para o input do nome do pdf
nome = tk.Entry(janela, width=30)
nome.insert(0,'nome')


mediaCPU = 0



def tempo_real():
    qtd = 0
    while True:

        #Captura dos dados
        cpu = psutil.cpu_percent(1)
        time.sleep(1)
        mem = psutil.virtual_memory()
        disco = psutil.disk_usage("/")

        #Plotagem das mensagens
        label_CPU.config(text=f"A porcentagem de uso do processador está em {cpu} % ")
        label_Mem.config(text=f"A porcentagem de memoria utilizada é de: {mem[2]}%")
        label_disco.config(text=f"O uso atual do disco é de: {disco[3]}%")
            
        if estaRodando == True:
            break
        if qtd == 100:
            break

        qtd += 1
        janela.update()

#criação e inicialização das threads para poder rodar mais de uma função ao mesmo tempo
thread = threading.Thread(target=tempo_real)
parar = False
thread2 = threading.Thread(target=dadosMaquina.maquina, args=(parar,))
thread.start()
thread2.start()


def limpar_Labels():
    label_disco.config(text='')
    label_Mem.config(text='')
    label_CPU.config(text='')

def gerar_pdf(relatorio):
    nomePDF = nome.get()
    documento.gerarPDF(nomePDF,relatorio)


def exibir_CPU():
    dadosMaquina.maquina(True)
    limpar_Labels()
    estaRodando = True
    mediaCPU = 0
    x = 0
    qtd = 0

    while True:
        cpu = psutil.cpu_percent(1)

        mensagem.config(text=f"A porcentagem de uso do processador está em {cpu} % ")
        mensagem.grid(row=20 + x)

        print(f"A porcentagem de uso do processador está em:{cpu}%")
        mediaCPU += cpu

        qtd += 1
        
        janela.update()
        if qtd == 10:
            break
    finalCPU = round(mediaCPU/qtd , 2)
    mensagem_final = Label(janela, text= f'A média final da CPU é de {finalCPU}%')
    mensagem_final.grid(column= 15, row= 26, padx= 3, pady= 3)
    
    relatorio = f"O percentual médio de CPU de sua analise foi de {finalCPU}% " 

    nome.grid(column=15, row=27, padx=3, pady=3)
    botaoPDF = Button(janela, text="Gerar PDF", command=lambda: gerar_pdf( relatorio))
    botaoPDF.grid(column=15, row=28, padx=10, pady=3)

    banco.inserirCPU(finalCPU)
    print(finalCPU)

def exibir_memoria():
    dadosMaquina.maquina(True)
    limpar_Labels()
    estaRodando = True

    mediaMem = 0
    x = 0
    qtd = 0
        
    while True:
        time.sleep(1)
        mem = psutil.virtual_memory()

        mensagem.config(text=f"A porcentagem de memória utilizada é de: {mem[2]}%")
        mensagem.grid(row=20 + x)

        print(f"A porcentagem de memoria utilizada é de: {mem[2]}%")
        mediaMem += float(mem[2])
        qtd += 1
        if qtd == 10:
            break
        janela.update()
    finalMem = round(mediaMem/qtd, 2)
    mensagem_final = Label(janela, text= f'A média final da memória é de {finalMem}%')
    mensagem_final.grid(column= 15, row= 26, padx= 3, pady= 3)

    relatorio = f"O percentual médio da memória RAM de sua analise foi de {finalMem}% " 

    nome.grid(column=15, row=27, padx=3, pady=3)
    
    botaoPDF = Button(janela, text="Gerar PDF", command=lambda: gerar_pdf( relatorio))
    botaoPDF.grid(column=15, row=28, padx=10, pady=3)
    banco.inserirMemoria(finalMem)
    print(finalMem)


def exibir_disco():
    dadosMaquina.maquina(True)
    limpar_Labels()
    estaRodando = True

    mediaDisk = 0
    x = 0
    qtd = 0
        
    while True:
        time.sleep(1)
        disco = psutil.disk_usage("/")

        mensagem.config(text=f"O uso atual do disco é de: {disco[3]}%")
        mensagem.grid(row=20 + x)

        print(f"o uso atual do disco é de: {disco[3]}%\n")
        mediaDisk += float(disco[3])

        qtd += 1
        if qtd == 10:
            break
        janela.update()
    finalDisk = round(mediaDisk/qtd, 2)
    mensagem_final = Label(janela, text= f'A média final do disco é de {finalDisk}%')
    mensagem_final.grid(column= 15, row=26, padx=3, pady=3)

    relatorio = f"O percentual médio do disco de sua analise foi de {finalDisk}% " 

    nome.grid(column=15, row=27, padx=3, pady=3)

    botaoPDF = Button(janela, text="Gerar PDF", command=lambda: gerar_pdf( relatorio))
    botaoPDF.grid(column=15, row=28, padx=10, pady=3)

    banco.inserirDisco(finalDisk)
    print(finalDisk)

janela.mainloop()


