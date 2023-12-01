import psutil as ps


def conversaoMb(numero):
    return numero / 131072


def getPacotesEnviados():
    pacotesEnviados = ps.net_io_counters(pernic=False, nowrap=True)[2]
    print(pacotesEnviados)
    return pacotesEnviados


def getTaxaDeTransferencia():
    enviados = ps.net_io_counters(pernic=False, nowrap=True)[0]
    recebidos = ps.net_io_counters(pernic=False, nowrap=True)[1]
    total = conversaoMb((enviados + recebidos) / 2)
    print(total)
    return total


def getPorcentagemUsoCpu():
    per = ps.cpu_percent(interval=None)
    print(per)
    return per


def getPorcentagemUsoRam():
    mem = ps.virtual_memory()[2]
    print(mem)
    return mem


def getUsoRam():
    mem = ps.virtual_memory()[3]
    print(mem)
    return mem


def getUsoTotal():
    mem = ps.virtual_memory()[0]
    print(mem)
    return mem


def getDisponivelRam():
    mem = ps.virtual_memory()[1]
    print(mem)
    return mem

