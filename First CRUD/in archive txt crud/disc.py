disc = []
#NOME E CÓDIGO PRA SER JOGADO DENTRO DE ADICIONAR, APAGAR E ATUALIZAR
def nome_disc():
    return input('Insira o nome da disciplina: ')
def code_disc():
    return input('Insira o código da disciplina: ')

def add_disc():  #ADICIONAR DISCIPLINA
    nomedisc = nome_disc()
    codedisc = code_disc()
    arquivo = open('disciplinas.txt', 'a', encoding='utf-8')
    disc = [nomedisc, codedisc]
    arquivo.write('{}#{}\n'.format(nomedisc,codedisc))
    arquivo.close()

def ler_disc():    #VER LISTA DE DISCIPLINAS
    arquivo = open('disciplinas.txt', 'r')
    for linha in arquivo.readlines():
        dados = linha.split('#')
        print('''
[------------------------------------------------------------------------------]
Disciplina(a): %s // Código: %s 
[------------------------------------------------------------------------------]
''' % (dados[0],dados[1]))

def del_disc():     #APAGAR DISCIPLINA
    try:
        arquivo = open('disciplinas.txt', 'r')
        codant = code_disc()
        encontrado = False
        disc = []
        for i in arquivo.readlines():
            e = i.split('#')
            if e[1].strip() == codant:
                print('\nDisciplina removida.')
                encontrado = True
            else:
                disc.append(i)
        arquivo.close()
        if not encontrado:
            print('Disciplina não encontrada')
        else:
            arquivo = open('disciplinas.txt', 'w')
            for i in disc:
                arquivo.write('{}'.format(i))
            arquivo.close()
    except FileNotFoundError:
        print('Arquivo inexistente')

def att_disc():      #ATUALIZAR DADOS DE UMA DISCIPLINA
    try:
        arquivo = open('disciplinas.txt', 'r')
        codant = code_disc()
        encontrado = False
        disc = []
        for i in arquivo.readlines():
            e = i.split('#')
            if e[1].strip() == codant:
                print('\nDisciplina encontrada, insira os novos dados')
                disc.append('{}#{}\n'.format(nome_disc(),code_disc()))
                encontrado = True
            else:
                disc.append(i)
        arquivo.close()
        if not encontrado:
            print('Disciplina não encontrada')
        else:
            arquivo = open('disciplinas.txt', 'w')
            for i in disc:
                arquivo.write('{}'.format(i))
            arquivo.close()
    except FileNotFoundError:
        print('Arquivo inexistente')

def menu_disc():      #MENU DAS DISCIPLINAS
    while True:
        option = int(input('''
---------------------------------------------------------------
Adicionar disciplina - 1
Alterar dados de uma disciplina - 2
Apagar dados de uma disciplina - 3
Lista de disciplinas - 4
Voltar ao menu inicial - 5
---------------------------------------------------------------
'''))
        if option == 5:
            break
        elif option == 1:
            add_disc()
        elif option == 2:
            att_disc()
        elif option == 3:
            del_disc()
        elif option == 4:
            ler_disc()











