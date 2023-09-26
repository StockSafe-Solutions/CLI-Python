import psutil
from reportlab.pdfgen import canvas #biblioteca usada

#tamanho padrão de uma folha a4 = 595.27 / 841.89
def gerarPDF(nomePDF, relatorio):
    lista = []

    for process in psutil.process_iter(['name', 'memory_info']):
        informacoes_processo = process.info
        lista.append(informacoes_processo)

    lista.sort(key=lambda dicionario: dicionario['memory_info'].rss, reverse= True)
    try:
        # input para armazenar o nome desejado do arquivo pdf na variável
      
        nome_pdf = nomePDF
        #criação da variável que "representa" o pdf
        pdf = canvas.Canvas('{}.pdf'.format(nome_pdf))
        #define a fonte que será usada nas próximas strings
        pdf.setFont("Helvetica-Oblique", 12) 

        """ 
         A função drawString recebe três valores(x, y, "Texto")
         X e Y são referentes ao plano cartesiano, que começa a partir do canto inferior
         esquerdo da folha do pdf assim da para definir a altura e em que ponto vai começar o texto
        """
        pdf.drawString(245,775, 'Lista de aplicativos rodando') 
        pdf.drawString(100,750, f"{relatorio} com os seguintes")
        pdf.drawString(100,735, f"aplicativos rodando:")

        pdf.setFont("Helvetica-Oblique", 10)

        """ for para passar para o pdf as informações dos aplicativos que estão rodando """
        y = 720 #Definição da altura em que a lista de aplicativos vai começar
        """
        A função psutil.process_iter(['name']) tras um JSON, e o for é usado para passar cada elemeto
        para a variável "proc"
        """
        contador = 0
        for x in lista:
            contador = contador + 1
            nome = x['name']
            memoria = round(x['memory_info'].rss/(1024*1024),2)
           
            y -= 20     # A cada ocorrência o valor do y cai 20, e o texto é plotado um pouco mais baixo
            if y <= 50: #quando o valor de y for menor que 50 vai gerar uma nova página
                pdf.showPage()  #A função showPage()gera uma nova página
                y = 750 # na próxima pagina o texto começa em 750 de altura 
            pdf.drawString(100,y, '{}º - Nome: {} Memória: {} Mb'.format(contador, nome, memoria))
            # print(nome, memoria)
        
        pdf.setTitle(nome_pdf)# definição do nome do arquivo
        pdf.save()# Salva o pdf
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        #Se der errado mostrará esse erro
        print('Erro ao gerar {}.pdf'.format(nome_pdf))