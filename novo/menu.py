import FuncionarioDao
import ServidorDao
import Coleta

CodigoServidor = ""
Email = ""
senha = ""
isLogado = False
servidor = False
listaFuncionario = []


def exibirMenu():
    print(
        """
            +--------------------------------------+
            | StockSafe Solutions                  |
            +--------------------------------------+
            | 1) Verificar Dados                   |
            | 2) Listar Processos                  |
            | 3) Mudar configurações de exibição   |
            | 4) Mostrar dados da RAM              |
            | 0) Sair                              |
            +--------------------------------------+
                """
    )


while isLogado is False:
    print("Autenticar máquina")
    while servidor is False:
        CodigoServidor = input("Digite o código: ")
        cod = ServidorDao.autenticarServidor(CodigoServidor)
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
        exibirMenu()
        escolha = input("Selecione uma opção: ")
        print(escolha)

        if int(escolha) == 1:
            print(123)
        else:
            print(456)
    else:
        print("Usuário inválido")
