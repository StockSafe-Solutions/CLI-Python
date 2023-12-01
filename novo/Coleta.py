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
    return conversaoMb((enviados+recebidos)/2)


getPacotesEnviados()
