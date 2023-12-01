import FuncionarioDao
import ServidorDao
import Coleta


CodigoServidor = ""
idServer = ""
Email = ""
senha = ""
isLogado = False
servidor = False
listaFuncionario = []
resposta = ""


def exibirMenu():
    print(
        """
            +--------------------------------------+
            | StockSafe Solutions                  |
            +--------------------------------------+
            | 1) Verificar Dados                   |
            | 2) Listar Processos                  |
            | 3) Mostrar dados da RAM              |
            | 0) Sair                              |
            +--------------------------------------+
                """
    )


def exibirDados(idServer):
    Coleta.getPacotesEnviados(idServer)
    Coleta.getPorcentagemUsoCpu(idServer)
    Coleta.getPorcentagemUsoRam(idServer)
    Coleta.getTaxaDeTransferencia(idServer)


def listarProcessos():
    Coleta.getProcessos()

def dadosRam(idServer):
    #Coleta.getPorcentagemUsoRam(idServer)
    Coleta.getDisponivelRam(idServer)
    Coleta.getPorcentagemUsoRam(idServer)

while isLogado is False:
    print("Autenticar máquina")
    while servidor is False:
        CodigoServidor = input("Digite o código: ")
        cod = ServidorDao.autenticarServidor(CodigoServidor)
        idServer = cod[0][0]
        if len(cod) > 0:
            servidor = True
        else:
            print("Código inválido")
    print("Faça seu login")
    Email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    # Obtém o funcionário pelo login
    funcionario = FuncionarioDao.getFuncionarioPorLogin(Email, senha)
    if len(funcionario):
        isLogado = True
        while True:
            exibirMenu()
            escolha = input("Selecione uma opção: ")
            print(escolha)

            if int(escolha) == 1:
                exibirDados(idServer)
            elif int(escolha) == 2:
                listarProcessos()
            elif int(escolha) == 3:
                dadosRam(idServer) 
            elif int(escolha) == 4:
                print("Saindo...")
            else:
                print("Escolha inválida")
            resposta = input("Deseja continuar? [S/n]")
            if resposta == "n":
                print("Saindo...")
                break
    else:
        print("Usuário inválido")
