alunos = []
#NOME E CPF PRA SER JOGADO DENTRO DE ADICIONAR, APAGAR E ATUALIZAR
def nome_aluno():
    return input('Insira o nome do aluno: ')
def cpf_aluno():
    return input('Insira o CPF do aluno: ')

def add_aluno(): #ADICIONAR ALUNO
    nomealuno = nome_aluno()
    cpfaluno = cpf_aluno()
    arquivo = open('alunos.txt', 'a', encoding='utf-8')
    alunos = [nomealuno, cpfaluno]
    arquivo.write('{}#{}\n'.format(nomealuno,cpfaluno))
    arquivo.close()

def ler_aluno():   #VER LISTA DE ALUNOS
    arquivo = open('alunos.txt', 'r')
    for linha in arquivo.readlines():
        dados = linha.split('#')
        print('''
[----------------------------------------------------------------------------------------]
Aluno(a): %s // CPF: %s 
[----------------------------------------------------------------------------------------]
''' % (dados[0],dados[1]))


def del_aluno():    #APAGAR ALUNO
    try:
        arquivo = open('alunos.txt', 'r')
        cpf_antigo = cpf_aluno()
        encontrado = False
        alunos = []
        for i in arquivo.readlines():
            e = i.split('#')
            if e[1].strip() == cpf_antigo:
                print('\nAluno removido.')
                encontrado = True
            else:
                alunos.append(i)
        arquivo.close()
        if not encontrado:
            print('Aluno não encontrado')
        else:
            arquivo = open('alunos.txt', 'w')
            for i in alunos:
                arquivo.write('{}'.format(i))
            arquivo.close()
    except FileNotFoundError:
        print('Arquivo inexistente')
        

def att_aluno():   #ATUALIZAR DADOS DE UM ALUNO
    try:
        arquivo = open('alunos.txt', 'r')
        cpf_antigo = cpf_aluno()
        encontrado = False
        alunos =[]
        for i in arquivo.readlines():
            e = i.split('#')
            if e[1].strip() == cpf_antigo:
                print('\nAluno encontrado, insira os novos dados')
                alunos.append('{}#{}\n'.format(nome_aluno(),cpf_aluno()))
                encontrado = True
            else:
                alunos.append(i)
        arquivo.close()
        if not encontrado:
            print('Aluno não encontrado')
        else:
            arquivo = open('alunos.txt', 'w')
            for i in alunos:
                arquivo.write('{}'.format(i))
            arquivo.close()
    except FileNotFoundError:
        print('Arquivo inexistente')
        
        
def menu_alunos():      #MENU DOS ALUNOS
    while True:
        option = int(input('''
---------------------------------------------------------------
Adicionar aluno - 1
Alterar dados de um aluno - 2
Apagar dados de um aluno - 3
Lista de alunos - 4
Voltar ao menu inicial - 5
---------------------------------------------------------------
'''))
        if option == 5:
            break
        elif option == 1:
            add_aluno()
        elif option == 2:
            del_aluno()
        elif option == 3:
            del_aluno()
        elif option == 4:
            ler_aluno()







    
