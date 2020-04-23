prof = []
#NOME, CPF E DEPARTAMENTO PRA SER JOGADO DENTRO DE ADICIONAR, APAGAR E ATUALIZAR
def nome_prof():
    return input('Insira o nome do professor: ')
def cpf_prof():
    return input('Insira o CPF do professor: ')
def dpt_prof():
    return input('Insira o departamento do professor: ')

def add_prof():  #ADICIONAR PROFESSOR
    nomeprof = nome_prof()
    cpfprof = cpf_prof()
    dptprof = dpt_prof()
    arquivo = open('professores.txt', 'a', encoding='utf-8')
    prof = [nomeprof, cpfprof, dptprof]
    arquivo.write('{}#{}#{}\n'.format(nomeprof,cpfprof,dptprof))
    arquivo.close()

def ler_prof():   #VER LISTA DE PROFESSORES
    arquivo = open('professores.txt', 'r')
    for linha in arquivo.readlines():
        dados = linha.split('#')
        print('''
[----------------------------------------------------------------------------------------]
Professor(a): %s // CPF: %s // Departamento: %s
[----------------------------------------------------------------------------------------]
''' % (dados[0],dados[1],dados[2]))


def del_prof():    #APAGAR PROFESSOR
    try:
        arquivo = open('professores.txt', 'r')
        cpf_antigo = cpf_prof()
        encontrado = False
        prof = []
        for i in arquivo.readlines():
            e = i.split('#')
            if e[1] == cpf_antigo:
                print('\nProfessor removido.')
                encontrado = True
            else:
                prof.append(i)
        arquivo.close()
        if not encontrado:
            print('Professor não encontrado')
        else:
            arquivo = open('professores.txt', 'w')
            for i in prof:
                arquivo.write('{}'.format(i))
            arquivo.close()
    except FileNotFoundError:
        print('Arquivo inexistente')
        

def att_prof():      #ATUALIZAR DADOS DE UM PROFESSOR
    try:
        arquivo = open('professores.txt', 'r')
        cpf_antigo = cpf_prof()
        encontrado = False
        prof =[]
        for i in arquivo.readlines():
            e = i.split('#')
            if e[1] == cpf_antigo:
                print('\nProfessor encontrado, insira os novos dados')
                prof.append('{}#{}#{}\n'.format(nome_prof(),cpf_prof(),dpt_prof()))
                encontrado = True
            else:
                prof.append(i)
        arquivo.close()
        if not encontrado:
            print('Professor não encontrado')
        else:
            arquivo = open('professores.txt', 'w')
            for i in prof:
                arquivo.write('{}'.format(i))
            arquivo.close()
    except FileNotFoundError:
        print('Arquivo inexistente')
        

def menu_prof():   #MENU DOS PROFESSORES QUE É IMPORTADO NO MENU PRINCIPAL
    while True:
        option = int(input('''
---------------------------------------------------------------
Adicionar professor - 1
Alterar dados de um professor - 2
Apagar dados de um professor - 3
Lista de professores - 4
Voltar ao menu inicial - 5
---------------------------------------------------------------
'''))
        if option == 5:
            break
        elif option == 1:
            add_prof()
        elif option == 2:
            att_prof()
        elif option == 3:
            del_prof()
        elif option == 4:
            ler_prof()

        






    
