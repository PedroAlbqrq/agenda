import sys
argumentosCMD = sys.argv[1:]

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
YELLOW = "\033[0;33m"

arquivo = open('todo.txt','r')
listaArq = arquivo.readlines()
listaArquivo = [x for x in listaArq if x != '\n']
arquivo = open('todo.txt','w')
for item in listaArquivo:
  arquivo.writelines(item)
arquivo.close()

def printCores(texto, cor) :
  return cor + texto + RESET

def numeroString(string):
    #CHECA SE UM DIGITO É UM NÚMERO
    if string >= '0' and string <= '9':
        return True
    return False

def listaDeData(lista):
    #CRIA UMA LISTA COM A DATA NO FORMATO CERTO [DD,MM,AAAA]
    lista2 = [int(lista[0]+lista[1]),int(lista[2]+lista[3]),int(lista[4]+lista[5]+lista[6]+lista[7])] 
    return lista2

def listaDeHora(lista):
    #CRIA UMA LISTA COM A HORA NO FORMATO CERTO [HH,MM]
   lista2 = [int(lista[0]+lista[1]),int(lista[2]+lista[3])]
   return lista2

def dataValida(string):
    #CHECA SE UMA STRING É UMA DATA
    if len(string) != 8:
        return False
    else:
        lista = []
        for item in string:
            lista.append(item)
    for item in lista:
        if numeroString(item) == False:
            return False
    lista = listaDeData(lista)
    if lista[0] <= 0 or lista[0] >= 31:
        return False
    if lista[1] <= 0 or lista[1] >= 12:
        return False
    if lista[0] == 31 and lista[1] == 2 or lista[0] == 31 and lista[1] == 4 or lista[0] == 31 and lista[1] == 6 or lista[0] == 31 and lista[1] == 9 or lista[0] == 31 and lista[1] == 11:
        return False
    if lista[0] == 30 and lista[1] == 2:
        return False
    return True

def horaValida(string):
    #CHECA SE UMA STRING É UMA HORA
    if len(string) != 4:
        return False
    else:
        lista = []
        for item in string:
            lista.append(item)
    for item in lista:
        if numeroString(item) == False:
            return False
    lista = listaDeHora(lista)
    if lista[0] < 0 or lista[0] > 23:
        return False
    if lista[1] < 0 or lista[1] > 59:
        return False
    return True

def projetoValido(string):
    #CHECA SE UMA STRING TEM O '+' NO COMEÇO, E SE TEM AO MENOS 2 CARACTERES
    if len(string) < 2:
        return False
    if string[0] != '+':
        return False
    return True

def contextoValido(string):
    #CHECA SE UMA STRING TEM O '@' NO COMEÇO, E SE TEM A MENOS 2 CARACTERES
    if len(string) < 2:
        return False
    if string[0] != '@':
        return False
    return True

def prioridadeValida(string):
    #CHECA SE UMA STRING TEM O SEGUINTE FORMATO (X) ONDE X PODE SER QUALQUER LETRA EM 'A' E 'Z' OU 'a' E 'z'
    if len(string) != 3:
        return False
    if string[0] != '(':
        return False
    if string[2] != ')':
        return False
    if string[1] >= 'a' and string [1] <= 'z' or string[1] >= 'A' and string[1] <= 'Z':
        return True
    return False

def indexPalavra(lista,palavra):
    cont = 0
    while cont < len(lista):
        if lista[cont] == palavra:
            return cont
        cont += 1
    return False

def descricao(lista):
    #RECEBE UMA LISTA NO FORMATO QUE O USUARIO QUISER, E RETORNA TODO O TEXTO QUE É DESCRIÇÃO
    listaFlag = lista[:]
    if dataValida(listaFlag[0]) == True:
      listaFlag.pop(0)
    if horaValida(listaFlag[0]) == True:
      listaFlag.pop(0)
    if prioridadeValida(listaFlag[0]) == True:
      listaFlag.pop(0)
    if projetoValido(listaFlag[len(listaFlag) -1]) == True:
      listaFlag.pop(len(listaFlag) -1)
    if contextoValido(listaFlag[len(listaFlag) -1]) == True:
      listaFlag.pop(len(listaFlag) -1)
    descricaoFrase = ''
    for item in listaFlag:
        descricaoFrase += item
        descricaoFrase += ' '
    return descricaoFrase
  
def horaFlag(lista):
    #RECEBE UMA LISTA E RETORNA A STRING DESSA LISTA QUE ESTEJA NO FORMATO DE HORA, CASO NÃO TENHA RETORNA FALSE
    if dataValida(lista[0]) == True:
      if horaValida(lista[1]) == True:
        return lista[1]
    else:
      if horaValida(lista[0]) == True:
        return lista[0]
    return False

def dataFlag(lista):
    #RECEBE UMA LISTA E RETORNA A STRING DESSA LISTA QUE ESTEJA NO FORMATO DE DATA, CASO NÃO TENHA RETORNA FALSE
    if dataValida(lista[0]) == True:
      return lista[0]
    return False

def prioridadeFlag(lista):
    #RECEBE UMA LISTA E RETORNA A STRING DESSA LISTA QUE ESTEJA NO FORMATO DE PRIORIDADE, CASO NÃO TENHA RETORNA FALSE
    if dataValida(lista[0]) == True:
      if horaValida(lista[1]) == True:
        if prioridadeValida(lista[2]) == True:
          return lista[2].upper()
      else:
        if prioridadeValida(lista[1]) == True:
          return lista[1].upper()
    else:
      if horaValida(lista[0]) == True:
        if prioridadeValida(lista[1]) == True:
          return lista[1].upper()
      else:
        if prioridadeValida(lista[0]) == True:
          return lista[0].upper()
    return False

def contextoFlag(lista):
    #RECEBE UMA LISTA E RETORNA A STRING DESSA LISTA QUE ESTEJA NO FORMATO DE CONTEXTO, CASO NÃO TENHA RETORNA FALSE
    if projetoValido(lista[len(lista) -1]) == True:
       if contextoValido(lista[len(lista) -2]) == True:
         return lista[len(lista) -2]
    else:
      if contextoValido(lista[len(lista) -1]) == True:
        return lista[len(lista) -1]
    return False

def projetoFlag(lista):
    #RECEBE UMA LISTA E RETORNA A STRING DESSA LISTA QUE ESTEJA NO FORMATO DE PROJETO, CASO NÃO TENHA RETORNA FALSE
    if projetoValido(lista[len(lista) -1]) == True:
      return lista[len(lista) -1]
    return False

def data(lista):
  for item in lista:
    if dataValida(item) == True:
      return item
  return False

def hora(lista):
  for item in lista:
    if horaValida(item) == True:
      return item
  return False

def projeto(lista):
  for item in lista:
    if projetoValido(item) == True:
      return item
  return False

def prioridade(lista):
  for item in lista:
    if prioridadeValida(item) == True:
      return item
  return False

def contexto(lista):
  for item in lista:
    if contextoValido(item) == True:
      return item
  return False

def organizar(linha):
    #RECEBE UMA LINHA STRING, E ORGANIZA ELA NO FORMATO(DESC(DATA,HORA,PRI,CONT,PRO))
    linha = linha.strip()
    linha = linha.split()
    dataV = dataFlag(linha)
    horaV = horaFlag(linha)
    descricaoV = descricao(linha)
    prioridadeV = prioridadeFlag(linha)
    contextoV = contextoFlag(linha)
    projetoV = projetoFlag(linha)
    itens = (descricaoV.strip(),)
    itensFlag = []
    if dataV != False:
        itensFlag.append(dataV)
    if horaV != False:
        itensFlag.append(horaV)
    if prioridadeV != False:
        itensFlag.append(prioridadeV)
    if contextoV != False:
        itensFlag.append(contextoV)
    if projetoV != False:
        itensFlag.append(projetoV)
    if itensFlag == []:
        itensFlag = (''),
        itens += itensFlag,
        return itens
    else:
        itensFlag = tuple(itensFlag)
        itens += itensFlag,
        return itens

def adicionar(tupla):
    #ADICIONA AO ARQUIVO UMA LINHA NO FORMATO PEDIDO, APARTIR DE UMA TUPLA VINDA DA FUNÇÃO ORGANIZAR
    #lembrar de usar a função organizar no adicionar
    if tupla[0] == '':
      print('Você precisa de uma descrição')
      return
    arquivo = open ('todo.txt','r')
    conteudoDoArquivo = arquivo.readlines()
    if len(tupla) == 2:
        for x in tupla[1]:
            if dataValida(x) == True:
                conteudoDoArquivo.append(x + ' ')
            elif horaValida(x) == True:
                conteudoDoArquivo.append(x + ' ')
            elif prioridadeValida(x) == True:
                conteudoDoArquivo.append(x + ' ')
    conteudoDoArquivo.append(tupla[0] + ' ')
    if len(tupla) == 2:
        for item in tupla[1]:
            if contextoValido(item) == True:
                conteudoDoArquivo.append(item + ' ')
            elif projetoValido(item) == True:
                conteudoDoArquivo.append(item + ' ')              
    conteudoDoArquivo.append('\n')
    arquivo = open('todo.txt','w')
    arquivo.writelines(conteudoDoArquivo)
    arquivo.close
    return

def listaComTuplasQueTemPrioridade():
    #ABRE O ARQUIVO
    #RETORNA UMA LISTA COM TODAS AS TUPLAS DO ARQUIVO QUE TEM PRIORIDADE
    arquivo = open('todo.txt','r')
    lista = [organizar(x) for x in arquivo]
    arquivo.close
    listaFinal = []
    cont = 0
    while cont < len(lista):
        if type(prioridade(lista[cont][1])) == str:
            listaFinal.append(lista[cont])
        cont += 1
    return listaFinal

def listaComTuplasQueNÃOPrioridade():
    #ABRE O ARQUIVO
    #RETORNA UMA LISTA COM TODAS AS TUPLAS DO ARQUIVO QUE NÃO TEM PRIORIDADE
    arquivo = open('todo.txt','r')
    lista = [organizar(x) for x in arquivo]
    arquivo.close
    listaFinal = []
    cont = 0
    while cont < len(lista):
        if prioridade(lista[cont][1]) == False:
            listaFinal.append(lista[cont])
        cont += 1
    return listaFinal

def ordenarPorPrioridade(lista):
    #RECEBE UMA LISTA COM TUPLAS QUE TEM PRIORIDADE (VINDA DA FUNÇÃO ANTERIOR)
    #E RETORNA A LISTA ORGANIZADA POR PRIORIDADE
    cont = 0
    while cont < len(lista):
        cont2 = 0
        while cont2 < len(lista) - 1:
            if prioridade(lista[cont2][1])[1] > prioridade(lista[cont2+1][1])[1]:
                flag = lista[cont2]
                lista[cont2] = lista[cont2 +1]
                lista[cont2 +1] = flag
            cont2 += 1
        cont += 1
    return lista

def ListaComPrioridadesOrdenadasESeparadas(lista):
    #RETORNA UMA LISTA DE LISTAS COM PRIORIDADES SEPARADAS A,B,C,D
    listaDeIndex = []
    cont = 0
    flag = prioridade(lista[cont][1])
    while cont < len(lista):
        if prioridade(lista[cont][1]) != flag:
            listaDeIndex.append(cont)
            flag = prioridade(lista[cont][1])
        cont +=1
    listaFinal = [lista[:listaDeIndex[0]]]
    cont = 0
    while cont < len(listaDeIndex) -1:
        listaFinal.append(lista[listaDeIndex[cont]:listaDeIndex[cont +1]])
        cont += 1
    listaFinal.append(lista[listaDeIndex[cont]:])
    return listaFinal


def colocarSemDatasNoFinal(lista):
    #PEGA UMA LISTA COM LISTAS DE PRIORIDADES SEMLEHANTES [A,A,A]
    #RETORNA AS QUE TEM DATA NO COMEÇO E AS SEM DATA NO FIM
    listaFinal = []
    cont = 0
    while cont < len(lista):
        if data(lista[cont][1]) == False:
            listaFinal.append(lista[cont])
        else:
            listaFinal.insert(0,lista[cont])
        cont += 1
    return listaFinal

def ordenarPorDataComPrioridade(lista):
    #RECEBE UMA LISTA COM TODAS AS PRIORIDADES E ORDENA DE ACORDO COM A DATA E HORA
    listaFinal = lista[:]
    cont = 0
    while cont < len(lista) - 1:
        listaFinal[cont] = colocarSemDatasNoFinal(listaFinal[cont])
        cont += 1
    cont = 0
    while cont < len(listaFinal):
        cont2 = 0
        while cont2 < len(listaFinal[cont]):
            cont3 = 0
            while cont3 < len(listaFinal[cont]) -1 :
                if type(data(listaFinal[cont][cont3][1])) == str and type(data(listaFinal[cont][cont3 + 1][1])) == str:
                    if int(data(listaFinal[cont][cont3][1])[4:]) > int(data(listaFinal[cont][cont3 + 1][1])[4:]):
                        flag = listaFinal[cont][cont3]
                        listaFinal[cont][cont3] = listaFinal[cont][cont3 +1]
                        listaFinal[cont][cont3 +1] = flag
                    elif int(data(listaFinal[cont][cont3][1])[4:]) == int(data(listaFinal[cont][cont3 + 1][1])[4:]):
                        if int(data(listaFinal[cont][cont3][1])[2:4]) > int(data(listaFinal[cont][cont3 + 1][1])[2:4]):
                            flag = listaFinal[cont][cont3]
                            listaFinal[cont][cont3] = listaFinal[cont][cont3 +1]
                            listaFinal[cont][cont3 +1] = flag
                        elif int(data(listaFinal[cont][cont3][1])[2:4]) == int(data(listaFinal[cont][cont3 + 1][1])[2:4]):
                            if int(data(listaFinal[cont][cont3][1])[0:2]) > int(data(listaFinal[cont][cont3 + 1][1])[0:2]):
                                flag = listaFinal[cont][cont3]
                                listaFinal[cont][cont3] = listaFinal[cont][cont3 +1]
                                listaFinal[cont][cont3 +1] = flag
                            elif int(data(listaFinal[cont][cont3][1])[0:2]) == int(data(listaFinal[cont][cont3 + 1][1])[0:2]):
                                if type(hora(listaFinal[cont][cont3][1])) != str and type(hora(listaFinal[cont][cont3 + 1][1])) == str:
                                    flag = listaFinal[cont][cont3]
                                    listaFinal[cont][cont3] = listaFinal[cont][cont3 +1]
                                    listaFinal[cont][cont3 +1] = flag
                                elif type(hora(listaFinal[cont][cont3][1])) == str and type(hora(listaFinal[cont][cont3 + 1][1])) == str:
                                    if int(hora(listaFinal[cont][cont3][1])[2:]) > int(hora(listaFinal[cont][cont3 +1][1])[2:]):
                                        flag = listaFinal[cont][cont3]
                                        listaFinal[cont][cont3] = listaFinal[cont][cont3 +1]
                                        listaFinal[cont][cont3 +1] = flag
                                    elif int(hora(listaFinal[cont][cont3][1])[2:]) == int(hora(listaFinal[cont][cont3 +1][1])[2:]):
                                        if int(hora(listaFinal[cont][cont3][1])[0:2]) > int(hora(listaFinal[cont][cont3 +1][1])[0:2]):
                                            flag = listaFinal[cont][cont3]
                                            listaFinal[cont][cont3] = listaFinal[cont][cont3 +1]
                                            listaFinal[cont][cont3 +1] = flag
                cont3 += 1
            cont2 += 1
        cont += 1
    return listaFinal

def filtrarData(lista):
    #RETORNA UMA LISTA COM TUPLAS QUE TEM DATA SEMELHANDO A QUE RETORNA UMA COM PRIORIDADES
    listaFinal = []
    cont = 0
    while cont < len(lista):
        if type(data(lista[cont][1])) == str:
            listaFinal.append(lista[cont])
        cont += 1
    return listaFinal

def ordenarPorDataEHoraSemPrioridade(lista):
    #COMO JA ORDENEI AS QUE TEM PRIORIDADE, ESSA ORDENA AS QUE TEM DATA, E ORDENA POR DATA E HORA(QUANDO TIVER HORA)
    #RETORNA ORDENADO POR DATA E HORA
    listaFinal = lista[:]
    cont = 0
    while cont < len(listaFinal):
        cont2 = 0
        while cont2 < len(listaFinal) - 1:
            #listaFinal[cont2][1]
            if int(data(listaFinal[cont2][1])[4:]) > int(data(listaFinal[cont2 + 1][1])[4:]):
                flag = listaFinal[cont2]
                listaFinal[cont2] = listaFinal[cont2 +1]
                listaFinal[cont2 +1] = flag
            elif int(data(listaFinal[cont2][1])[4:]) == int(data(listaFinal[cont2 + 1][1])[4:]):
                if int(data(listaFinal[cont2][1])[2:4]) > int(data(listaFinal[cont2 + 1][1])[2:4]):
                    flag = listaFinal[cont2]
                    listaFinal[cont2] = listaFinal[cont2 +1]
                    listaFinal[cont2 +1] = flag
                elif int(data(listaFinal[cont2][1])[2:4]) == int(data(listaFinal[cont2 + 1][1])[2:4]):
                    if int(data(listaFinal[cont2][1])[:2]) > int(data(listaFinal[cont2 + 1][1])[:2]):
                        flag = listaFinal[cont2]
                        listaFinal[cont2] = listaFinal[cont2 +1]
                        listaFinal[cont2 +1] = flag
                    elif int(data(listaFinal[cont2][1])[:2]) == int(data(listaFinal[cont2 + 1][1])[:2]):
                        if type(hora(listaFinal[cont2][1])) != str and type(hora(listaFinal[cont2 + 1][1])) == str:
                            flag = listaFinal[cont2]
                            listaFinal[cont2] = listaFinal[cont2 +1]
                            listaFinal[cont2 +1] = flag
                        elif type(hora(listaFinal[cont2][1])) == str and type(hora(listaFinal[cont2 + 1][1])) == str:
                            if int(hora(listaFinal[cont2][1])[2:]) > int(hora(listaFinal[cont2+1][1])[2:]):
                                flag = listaFinal[cont2]
                                listaFinal[cont2] = listaFinal[cont2 +1]
                                listaFinal[cont2 +1] = flag
                            elif int(hora(listaFinal[cont2][1])[2:]) == int(hora(listaFinal[cont2+1][1])[2:]):
                                if int(hora(listaFinal[cont2][1])[:2]) > int(hora(listaFinal[cont2+1][1])[:2]):
                                    flag = listaFinal[cont2]
                                    listaFinal[cont2] = listaFinal[cont2 +1]
                                    listaFinal[cont2 +1] = flag          
            cont2 += 1
        cont += 1
    return listaFinal

def filtrarNãoTemData(lista):
    #COMO ANTERIORMENTE EU JA ORDENEI OQ TEM PRIORIDADE E O QUE TEM HORA, AGORA VOU FILTAR APENAS AS TUPLAS QUE NÃO TEM DATA
    listaFinal = []
    cont = 0
    while cont < len(lista):
        if data(lista[cont][1]) == False:
            listaFinal.append(lista[cont])
        cont += 1
    return listaFinal

def filtrarQueTemHora(lista):
    #COMO ANTERIORMENTE EU JA ORDENEI OQ TEM PRIORIDADE E QUE TEM DATA, AGORA VOU FILTRAR OQ NAO TEM NEM PRIORIDADE NEM DATA
    listaFinal = []
    cont = 0
    while cont < len(lista):
        if type(hora(lista[cont][1])) == str:
            listaFinal.append(lista[cont])
        cont += 1
    return listaFinal

def filtrarQueNãoTemNada(lista):
    #COMO ANTERIORMENTE JA FILTREI TUDO QUE EU QUERIA, NESSA EU PEGO AS TUPLAS QUE NÃO TEM NEM PRIORIDADE NEM DATA NEM HORA, OU SEJA OQ NÃO PRECISA ORDENAR
    listaFinal = []
    cont = 0
    while cont < len(lista):
        if hora(lista[cont][1]) == False:
            listaFinal.append(lista[cont])
        cont += 1
    return listaFinal

def ordenarPorHora(lista):
    #RECEBE UMA LISTA COM TUPLAS, E ORDENA ELAS POR HORA
    listaFinal = lista[:]
    cont = 0
    while cont < len(listaFinal):
        cont2 = 0
        while cont2 < len(listaFinal) -1:
            if int(hora(listaFinal[cont2][1])[2:]) > int(hora(listaFinal[cont2 +1][1])[2:]):
                flag = listaFinal[cont2]
                listaFinal[cont2] = listaFinal[cont2 +1]
                listaFinal[cont2 +1] = flag
            elif int(hora(listaFinal[cont2][1])[2:]) == int(hora(listaFinal[cont2 +1][1])[2:]):
                if int(hora(listaFinal[cont2][1])[:2]) > int(hora(listaFinal[cont2 +1][1])[:2]):
                    flag = listaFinal[cont2]
                    listaFinal[cont2] = listaFinal[cont2 +1]
                    listaFinal[cont2 +1] = flag
            cont2 +=1
        cont += 1
    return listaFinal

def printBonitinho(tupla):
    #PRINTA DO JEITO QUE O PROFESSOR QUER
    #FALTA PRINTAR POR CORES
    stringDoPrint = ''
    if type(data(tupla[1])) == str:
        stringDoPrint += data(tupla[1])[:2] + '/' + data(tupla[1])[2:4] + '/' + data(tupla[1])[4:]
        stringDoPrint += ' '
    if type(hora(tupla[1])) == str:
        stringDoPrint +=  hora(tupla[1])[:2] + ':' + hora(tupla[1])[2:]
        stringDoPrint += ' '
    if type(prioridade(tupla[1])) == str:
        stringDoPrint += prioridade(tupla[1])
        stringDoPrint += ' '
    stringDoPrint += tupla[0]
    stringDoPrint += ' '
    if type(contexto(tupla[1])) == str:
        stringDoPrint += contexto(tupla[1])
        stringDoPrint += ' '
    if type(projeto(tupla[1])) == str:
        stringDoPrint += projeto(tupla[1])
    stringDoPrint = stringDoPrint.strip()
    if prioridade(tupla[1]) == '(A)':
        return printCores(stringDoPrint,RED)
    if prioridade(tupla[1]) == '(B)':
        return printCores(stringDoPrint,YELLOW)
    if prioridade(tupla[1]) == '(C)':
        return printCores(stringDoPrint,BLUE)
    if prioridade(tupla[1]) == '(D)':
        return printCores(stringDoPrint,GREEN)
    return stringDoPrint

def listar():
    #PRINTA TODAS AS TAREFAS DO TODO.TXT EM ORDEM E BONITINHO
    listaOrdenada = listaComTuplasQueTemPrioridade()
    listaOrdenada = ordenarPorPrioridade(listaOrdenada)
    listaOrdenada = ListaComPrioridadesOrdenadasESeparadas(listaOrdenada)
    cont = 0
    while cont < len(listaOrdenada):
        listaOrdenada[cont] = colocarSemDatasNoFinal(listaOrdenada[cont])
        cont += 1
    listaOrdenada = ordenarPorDataComPrioridade(listaOrdenada)
    
    listaOrdenada2 = listaComTuplasQueNÃOPrioridade()
    listaOrdenada2 = filtrarData(listaOrdenada2)
    listaOrdenada2 = ordenarPorDataEHoraSemPrioridade(listaOrdenada2)

    listaOrdenada3 = listaComTuplasQueNÃOPrioridade()
    listaOrdenada3 = filtrarNãoTemData(listaOrdenada3)
    listaOrdenada3 = filtrarQueTemHora(listaOrdenada3)
    listaOrdenada3 = ordenarPorHora(listaOrdenada3)

    listaOrdenada4 = listaComTuplasQueNÃOPrioridade()
    listaOrdenada4 = filtrarNãoTemData(listaOrdenada4)
    listaOrdenada4 = filtrarQueNãoTemNada(listaOrdenada4)
    
    listaCompleta = []
    
    for item in listaOrdenada:
        for itenzinho in item:
            listaCompleta.append(itenzinho)
    for item in listaOrdenada2:
        listaCompleta.append(item)
    for item in listaOrdenada3:
        listaCompleta.append(item)
    for item in listaOrdenada4:
        listaCompleta.append(item)
    
    cont = 0
    while cont < len(listaCompleta):
        print('{} {}'.format(cont + 1,printBonitinho(listaCompleta[cont])))
        cont += 1
    return

def listar2():
    #É O MESMO ESQUEMA DA FUNÇÃO LISTAR ANTERIOR, SÓ QUE EM VEZ DE PRINTAR AS TAREFAS
    #ELE RETORNA UMA LISTA COM TODAS AS TAREFAS E O NÚMERO DE CADA UMA
    #PRA EU PODER REMOVER USANDO O MESMO INDEX DO LISTAR
    listaOrdenada = listaComTuplasQueTemPrioridade()
    listaOrdenada = ordenarPorPrioridade(listaOrdenada)
    listaOrdenada = ListaComPrioridadesOrdenadasESeparadas(listaOrdenada)
    cont = 0
    while cont < len(listaOrdenada):
        listaOrdenada[cont] = colocarSemDatasNoFinal(listaOrdenada[cont])
        cont += 1
    listaOrdenada = ordenarPorDataComPrioridade(listaOrdenada)
    
    listaOrdenada2 = listaComTuplasQueNÃOPrioridade()
    listaOrdenada2 = filtrarData(listaOrdenada2)
    listaOrdenada2 = ordenarPorDataEHoraSemPrioridade(listaOrdenada2)

    listaOrdenada3 = listaComTuplasQueNÃOPrioridade()
    listaOrdenada3 = filtrarNãoTemData(listaOrdenada3)
    listaOrdenada3 = filtrarQueTemHora(listaOrdenada3)
    listaOrdenada3 = ordenarPorHora(listaOrdenada3)

    listaOrdenada4 = listaComTuplasQueNÃOPrioridade()
    listaOrdenada4 = filtrarNãoTemData(listaOrdenada4)
    listaOrdenada4 = filtrarQueNãoTemNada(listaOrdenada4)
    
    listaCompleta = []
    
    for item in listaOrdenada:
        for itenzinho in item:
            listaCompleta.append(itenzinho)
    for item in listaOrdenada2:
        listaCompleta.append(item)
    for item in listaOrdenada3:
        listaCompleta.append(item)
    for item in listaOrdenada4:
        listaCompleta.append(item)
    cont = 0
    listaFinal = []
    while cont < len(listaCompleta):
        listaFinal.append([cont + 1,listaCompleta[cont]])
        cont += 1
    return listaFinal

def listarOpicional(string):
  lista = listar2()
  if len(string) == 1:
    if string >= 'a' and string <= 'z' or string >= 'A' and string <= 'Z':
      string = '(' + string.upper() + ')'
      if prioridadeValida(string) == True:
        printeiALgum = False
        for item in lista:
          if type(prioridade(item[1][1])) == str:
            if prioridade(item[1][1]) == string:
              print('{} {}'.format(item[0],printBonitinho(item[1])))
              printeiALgum = True
        if printeiALgum == False:
          print(' Você digitou um paramêtro válido para o listar, porém não existe nenhuma atividade com esse parâmetro')
        return
    else:
      print('Você digitou um paramêtro inválido para o listar')
      return
  elif contextoValido(string) == True:
    printeiALgum = False
    for item in lista:
      if contexto(item[1][1]) == string:
        print('{} {}'.format(item[0],printBonitinho(item[1])))
        printeiALgum = True
    if printeiALgum == False:
      print(' Você digitou um paramêtro válido para o listar, porém não existe nenhuma atividade com esse parâmetro')
    return
  elif projetoValido(string) == True:
    printeiALgum = False
    for item in lista:
      if projeto(item[1][1]) == string:
        print('{} {}'.format(item[0],printBonitinho(item[1])))
        printeiALgum = True
    if printeiALgum == False:
      print(' Você digitou um paramêtro válido para o listar, porém não existe nenhuma atividade com esse parâmetro')
    return
  else:
    print(' Você não digitou um parâmetro inválido para o listar')
    return
def indexRemoverCorreto(lista,index):
    #CHECA SE O INDEX QUE O USUÁRIO QUER REMOVER É UM INDEX DE FATO
    for item in lista:
        if str(item[0]) == index:
            return True
    return False

def remover(index):
    #RECEBE UM INDEX REMOVE A TAREFA DO ARQUIVO
    lista = listar2()
    if indexRemoverCorreto(lista,index) == True:
        listaFinal = []
        for item in lista:
            if str(item[0]) != index:
                listaFinal.append(item[1])
        arquivo = open('todo.txt','w')
        arquivo.close
        for item in listaFinal:
            adicionar(item)
        return
    else:
        print('O número da tarefa que você quer remover não existe!')

def priorizar(index,priori):
    priori = '(' + priori + ')'
    if prioridadeValida(priori) == False:
        print('Essa prioridade não é valida')
        return
    
    lista = listar2()
    if indexRemoverCorreto(lista,index) == True:
        listaFinal = []
        for item in lista:
            if str(item[0]) != index:
                listaFinal.append(item[1])
            elif str(item[0]) == index:
                tuplaFinal = ()
                tuplaFinal += item[1][0],
                tuplaFlag = ()
                if type(data(item[1][1])) == str:
                    tuplaFlag += data(item[1][1]),
                if type(hora(item[1][1])) == str:
                    tuplaFlag += hora(item[1][1]),
                tuplaFlag += priori,
                if type(contexto(item[1][1])) == str:
                    tuplaFlag += contexto(item[1][1]),
                if type(projeto(item[1][1])) == str:
                    tuplaFlag += projeto(item[1][1]),
                tuplaFinal += tuplaFlag,
                listaFinal.append(tuplaFinal)
        arquivo = open('todo.txt','w')
        arquivo.close
        for item in listaFinal:
            adicionar(item)
        return
    else:
        print('O número da tarefa que você quer remover não existe!')


def adicionarFAZER(tupla):
    #ADICIONA AO ARQUIVO UMA LINHA NO FORMATO PEDIDO, APARTIR DE UMA TUPLA VINDA DA FUNÇÃO ORGANIZAR
    #lembrar de usar a função organizar no adicionar
    arquivo = open ('done.txt','r')
    conteudoDoArquivo = arquivo.readlines()
    if len(tupla) == 2:
        for x in tupla[1]:
            if dataValida(x) == True:
                conteudoDoArquivo.append(x + ' ')
            elif horaValida(x) == True:
                conteudoDoArquivo.append(x + ' ')
            elif prioridadeValida(x) == True:
                conteudoDoArquivo.append(x + ' ')
    conteudoDoArquivo.append(tupla[0] + ' ')
    if len(tupla) == 2:
        for item in tupla[1]:
            if contextoValido(item) == True:
                conteudoDoArquivo.append(item + ' ')
            elif projetoValido(item) == True:
                conteudoDoArquivo.append(item + ' ')              
    conteudoDoArquivo.append('\n')
    arquivo = open('done.txt','w')
    arquivo.writelines(conteudoDoArquivo)
    arquivo.close
    return

def fazer(index):
    #RECEBE UM INDEX REMOVE A TAREFA DO ARQUIVO E MOVE ELA A O ARQUIVO FEITO
    lista = listar2()
    if indexRemoverCorreto(lista,index) == True:
        listaFinal = []
        for item in lista:
            if str(item[0]) != index:
                listaFinal.append(item[1])
            if str(item[0]) == index:
                feita = item[1]
        arquivo = open('todo.txt','w')
        arquivo.close
        for item in listaFinal:
            adicionar(item)
        adicionarFAZER(feita)
        return
    else:
      if numeroString(index) == True:
        print(' O número da tarefa que você quer dar como feita não existe!')
      else:
        print(' Você tem que digitar um número de uma atividade para ser dada como feita, não uma string')

def processarComandos(lista):
    #FUNÇÃO QUE RECEBE UM PARAMETRO E EXECUTA ELE EXEMPLO: A = ADICIOANR
    if lista[0] == 'a':
      try:
        if len(lista) >= 2:
            listaAdicionar = lista[1:]
            stringAdicionar = ''
            for item in listaAdicionar:
                stringAdicionar += item
                stringAdicionar += ' '
            stringAdicionar = stringAdicionar.strip()
            adicionar(organizar(stringAdicionar))
        else:
            print(' A tarefa que você quer adicionar tem que ter pelo menos uma descrição')
      except:
        print('Você tem que digitar pelo menos uma descrição')
    elif lista[0] == 'l':
        if len(lista) == 1:
          listar()
        else:
          listarOpicional(lista[1])
    elif lista[0] == 'r':
        if len(lista) == 1:
            print(' Você tem que digitar uma tarefa para remover ')
        else:
            remover(lista[1])
    elif lista[0] == 'p':
      if len(lista) == 3:
        if lista[2] >= 'a' and lista[2] <= 'z' or lista[2] >= 'A' and lista[2] <= 'Z':
            priorizar(lista[1],lista[2].upper())
        else:
          print(' Prioridade inválida ')
      else:
        print(' Você tem que dar o número de uma atividade e uma prioridade no paramêtro p')
    elif lista[0] == 'f':
        if len(lista) == 2:
                fazer(lista[1])
        else:
            print(' Você tem que digitar uma atividade para ser dada como feita')
    elif lista[0] == 'h':
        print('\n               !!Você acaba de entrar no HELP!!\n \n Os comandos disponíveis na agenda está na lista que segue abaixo:\n \n Lista De Comandos:\n \n a = adicionar\n l = listar\n r = remover\n p = priorizar\n f = fazer\n \n Uma breve explicação de cada um:\n \n o comando "a" é seguido de uma frase, que obrigatoriamente tem que conter pelo menos uma palavra/letra\n o comando "l" lista todas as atividades que você possui na agenda de forma ordenada\n o comando "r" remove uma atividade da agenda, ele precisa ser seguido do número da atividade que você quer remover\n o comando "p" altera a prioridade de alguma tarefa ele é seguido de um número de uma atividade, seguido de uma nova prioridade de A á Z\n o comando "f" é seguido de um número de uma atividade ele remove essa atividade da agenda e salva em um arquivo done.txt \n ')
    else:
        print(' COMANDO INVÁLIDO\n \n Lista De Comandos:\n a = adicionar\n l = listar\n r = remover\n p = priorizar\n f = fazer\n')
    return
if len(argumentosCMD) == 0:
    print('               !!Você acaba de abrir o agenda.py!! \n Agenda.py é um programa de agenda que funciona por linha de comando\n     caso você queira saber os comandos disponíveis na agenda\n          e como eles funcionam digite o parâmetro h')
else:
    processarComandos(argumentosCMD)
