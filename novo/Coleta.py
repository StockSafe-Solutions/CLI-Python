import psutil as ps
import Captura


def conversaoMb(numero):
    return numero / 131072


def getPacotesEnviados(idServer):
    pacotesEnviados = ps.net_io_counters(pernic=False, nowrap=True)[2]
    print("Pacotes enviados: ", pacotesEnviados)
    Captura.inserirRegistros(idServer, 1, float(pacotesEnviados))
    return pacotesEnviados


def getTaxaDeTransferencia(idServer):
    enviados = ps.net_io_counters(pernic=False, nowrap=True)[0]
    recebidos = ps.net_io_counters(pernic=False, nowrap=True)[1]
    total = round(conversaoMb((enviados + recebidos) / 2), 0)
    print("Taxa de transferência: ", round(total, 0))
    Captura.inserirRegistros(idServer, 4, total)
    return round(total, 0)


def getPorcentagemUsoCpu(idServer):
    per = ps.cpu_percent(interval=2)
    if int(per) == 0:
        per = ps.cpu_percent(interval=2)
    else:
        Captura.inserirRegistros(idServer, 2, per)
        print("Porcentagem de CPU: ", per)
        return per


def getPorcentagemUsoRam(idServer):
    mem = ps.virtual_memory()[2]
    print("Porcentagem de RAM: ", mem)
    Captura.inserirRegistros(idServer, 3, mem)
    return mem


def getUsoTotal(idServer):
    mem = ps.virtual_memory()[0]
    Captura.inserirRegistros(idServer, 5, mem)
    print("Uso total da RAM: ", mem)
    return mem


def getDisponivelRam(idServer):
    mem = conversaoMb(ps.virtual_memory()[1])
    print("Memória disponivel RAM: ", mem)
    Captura.inserirRegistros(idServer, 6, mem)
    return mem


def getProcessos():
    processos = []
    for proc in ps.process_iter(["pid", "name", "username"]):
        processos.append(proc.info)
        print(proc.info)
    return processos
