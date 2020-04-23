prof = []        #Listas de cada parte antes do while true para que quando ele volte
alunos = []      #ao menu principal não retorne listas vazias e não armazene
disc = []        #os dados corretamente na memória
turma = []


while True:

#Menu principal

    resposta = int(input('''
------------------------------------------------------------------
O que deseja consultar?
Dados de um professor - 1
Dados de um aluno - 2
Dados de uma disciplina - 3
Dados de uma turma - 4
Sair - 5
------------------------------------------------------------------
'''))


#Dados base de professor atribuídos e retornados embaixo nos if's de escolha
    if resposta == 1:
        def nome_prof():
            return input('Insira o nome do professor(a): ')
        def cpf_prof():
            return input('Insira o CPF do professor(a): ')
        def dep_prof():
            return input('Insira o departamento do professor(a): ')

        def add_prof():        #adicionar professor
            global prof
            nomeprof = nome_prof().upper()
            cpfprof = cpf_prof()
            depprof = dep_prof().upper()
            prof.append([nomeprof, cpfprof, depprof])
            print('\nProfessor adicionado.')
            
        def del_prof():      #apagar dados de um professor
            global prof
            cpfprof = cpf_prof()
            for n, i in enumerate(prof):
                if i[1] == cpfprof:
                    print('\nProfessor removido.')
                    del prof[n]
            else:
                print('')

        def att_prof():      #atualizar dados de um professor
            global prof
            cpfprof = cpf_prof()
            for n, i in enumerate(prof):
                if i[1] == cpfprof:
                    print('Este CPF remete ao professor {}'.format(i[0]))
                    novo_nome = input('\nInsira o novo nome para o professor(a): ')
                    novo_cpf = input('\nInsira o novo CPF para o professor(a): ')
                    novo_dep = input('\nInsira o novo departamento para o professor(a): ')
                    prof[n][0] = novo_nome
                    prof[n][1] = novo_cpf
                    prof[n][2] = novo_dep
                    print('\nDados do professor alterados com sucesso.')
            else:
                print('')


        if resposta == 1: #Menu dos professores
            while True:
                escolha = int(input('''
-------------------------------------------------------------------------
Adicionar professor - 1
Alterar dados de um professor - 2
Apagar dados de um professor - 3
Lista de professores - 4
Sair - 5
-------------------------------------------------------------------------
'''))
                if escolha == 5:      #sair do menu alternativo de professores
                    break
                elif escolha == 1:    #retorna a função de adicionar ao menu alternativo
                    add_prof()
                    continue
                elif escolha == 2:   #retorna a função de atualizar ao menu alternativo
                    att_prof()
                    continue
                elif escolha == 3:   #retorna a função de apagar ao menu alternativo
                    del_prof()
                    continue
                elif escolha == 4:                            #escolha 4 sendo a estrutura pra ler a lista de
                    for n, i in enumerate(prof):              #professores devidamente
                        print('''
    [------------------------------------------------------------------------]
     Professor(a): %s // CPF: %s // Departamento: %s
    [------------------------------------------------------------------------]
    ''' %(i[0], i[1], i[2]))
                        continue

#Dados base de aluno atribuídos e retornados embaixo nos if's de escolha
    if resposta == 2:
        def nome_aluno():
            return input('Insira o nome do aluno(a): ')
        def cpf_aluno():
            return input('Insira o CPF do aluno(a): ')

        def add_aluno():           #adicionar aluno
            global alunos
            nomealuno = nome_aluno().upper()
            cpfaluno = cpf_aluno()
            alunos.append([nomealuno, cpfaluno])
            print('Aluno adicionado.')

        def del_aluno():           #apagar aluno
            global alunos
            cpfaluno = cpf_aluno()
            for n, i in enumerate(alunos):
                if i[1] == cpfaluno:
                    print('\nAluno removido com sucesso.')
                    del alunos[n]
                else:
                    print('')

        def att_aluno():              #atualizar aluno
            cpfaluno = cpf_aluno()
            for n, i in enumerate(alunos):
                if i[1] == cpfaluno:
                    print('Este CPF remete ao aluno(a) {}'.format(i[0]))
                    novo_nome = input('\nInsira o novo nome para o(a) aluno(a): ')
                    novo_cpf = input('\nInsira o novo CPF para o(a) aluno: ')
                    alunos[n][0] = novo_nome
                    alunos[n][1] = novo_cpf
                    print('\nDados do aluno alterados com sucesso.')
                else:
                    print('')

        if resposta == 2: #Menu dos alunos
            while True:
                escolha = int(input('''
-------------------------------------------------------------------------
Adicionar aluno - 1
Alterar dados de um aluno - 2
Apagar dados de um aluno - 3
Lista de alunos - 4
Sair - 5
-------------------------------------------------------------------------
'''))
                if escolha == 5:          #sair do menu alternativo de alunos
                    break
                elif escolha == 1:        #retorna a função de adicionar aluno ao menu alternativo
                    add_aluno()
                    continue
                elif escolha == 2:        #retorna a função de atualizar aluno ao menu alternativo
                    att_aluno()
                    continue
                elif escolha == 3:        #retorna a função de apagar aluno ao menu alternativo
                    del_aluno()
                    continue
                elif escolha == 4:                    #escolha 4 sendo a estrutura pra ler a lista de alunos
                    for n, i in enumerate(alunos):
                        print('''
    [------------------------------------------------------------------------]
     Aluno(a): %s // CPF: %s 
    [------------------------------------------------------------------------]
    ''' %(i[0], i[1]))
                        continue

#Dados base de disciplinas atribuídos e retornados embaixo nos if's de escolha
    if resposta == 3:
        def nome_disc():
            return input('Insira o nome da disciplina: ')
        def cod_disc():
            return input('Insira o código da disciplina: ')

        def add_disc():        #adicionar disciplina
            global disc
            nomedisc = nome_disc().upper()
            coddisc = cod_disc()
            disc.append([nomedisc, coddisc])
            print('\nDisciplina adicionada.')

        def del_disc():        #apagar disciplina
            global disc
            coddisc = cod_disc()
            for n, i in enumerate(disc):
                if i[1] == coddisc:
                    print('\nDisciplina removida.')
                    del disc[n]
                else:
                    print('')

        def att_disc():              #atualizar disciplina
            coddisc = cod_disc()
            for n, i in enumerate(disc):
                if i[1] == coddisc:
                    print('Este código remete a disciplina de {}'.format(i[0]))
                    nova_disc = input('\nInsira o novo nome para a disciplina: ')
                    novo_cod = input('\nInsira o novo código para a disciplina: ')
                    disc[n][0] = nova_disc
                    disc[n][1] = novo_cod
                    print('\nDisciplina alterada com sucesso.')
                else:
                    print('')

        if resposta == 3: #Menu das disciplinas
            while True:
                escolha = int(input('''
-------------------------------------------------------------------------
Adicionar disciplina - 1
Alterar dados de uma disciplina - 2
Apagar dados de uma disciplina - 3
Lista de disciplinas - 4
Sair - 5
-------------------------------------------------------------------------
'''))
                if escolha == 5:          #sair do menu alternativo de disciplinas
                    break
                elif escolha == 1:        #retorna a função de adicionar disciplina ao menu alternativo
                    add_disc()
                    continue
                elif escolha == 2:       #retorna a função de atualizar disciplina ao menu alternativo
                    att_disc()
                    continue
                elif escolha == 3:       #retorna a função de apagar disciplina ao menu alternativo
                    del_disc()
                elif escolha == 4:                #escolha 4 sendo a estrutura pra ler a lista de disciplinas
                    for n, i in enumerate(disc):
                        print('''
    [------------------------------------------------------------------------]
     Disciplina: %s // Código: %s 
    [------------------------------------------------------------------------]
    ''' %(i[0], i[1]))
                        continue
#Dados base de disciplinas atribuídos e retornados embaixo nos if's de escolha
    if resposta == 4:
        def cod_turma():
            return input('Digite o código da turma: ')
        def peri_turma():
            return input('Digite o período da turma: ')
        def cdisc_turma():
            return input('Digite o código da disciplina da turma: ')
        def cpfprof_turma():
            return input('Digite o CPF de um do(s) professores: ')
        def cpfaluno_turma():
            return input('Digite o CPF de um dos(s) alunos: ')

        def add_turma():             #Adicionar turma
            global turma
            global prof
            global alunos
            global disc
            codturma = cod_turma()
            periturma = peri_turma()
            cdiscturma = cdisc_turma()
            for n, i in enumerate(disc):
                if cdiscturma == i[2]:
                    codturma = i[0]
                else:
                    codturma = 'naotem'
            np = int(input('Digite quantos professores deseja adicionar: '))  #delimitar a quantidade de professores
            na = int(input('Digite quantos alunos deseja adicionar: '))    #delimitar a quantidade de alunos
            cpfprof = []
            for k in range(np):
                cpfprofturma = cpfprof_turma()
                cpfprof.append(cpfprofturma)
            cpfaluno = []
            for k in range(na):
                cpfalunoturma = cpfaluno_turma()
                cpfaluno.append(cpfalunoturma)
            turma.append([codturma,periturma,cdiscturma,cpfprof,cpfaluno])
            for n, i in enumerate(turma):
                if cpfprof == []:
                    print('\nNÃO HÁ PROFESSORES NA TURMA. TURMA NÃO CADASTRADA.')
                    del turma[n]
                elif cpfaluno == []:
                    print('\nNÃO HÁ ALUNOS NA TURMA. TURMA NÃO CADASTRADA')
                    del turma[n]
                elif codturma == 'naotem':
                    print('\nNÃO HÁ DISCIPLINA NA TURMA, TURMA NÃO CADASTRADA')
                    del turma[n]
                else:
                    print('\nTurma criada.')

        def ler_turma():      #Ver lista de turmas
            global turma
            print('/\/\/\/\/\/\_LISTA DE TURMAS_/\/\/\/\/\/\n')
            encontrado = False
            for n, i in enumerate(turma):
                print('''Código da turma: %s // Período: %s // Código da disciplina: %s\n''' %(i[0],i[1],i[2]))
                print('''CPFs professores: %s\n'''%(i[3]))
                print('''CPFs alunos: %s\n'''%(i[4]))
                print('__________________________________________________________________________')
                encontrado = True
            if encontrado is False:
                print('Não há turmas cadastradas no sistema.')


        def del_turma():        #Apagar turma
            global turma
            codturma = cod_turma()
            for n, i in enumerate(turma):
                if i[0] == codturma:          #se o codigo informado for igual a um existente ele remove
                    print('\nTurma removida')
                    del turma[n]     #remove em definitivo a turma baseado no código
                else:
                    print('')

        def att_turma():        #Alterar turma
            global turma
            codturma = cod_turma()
            for n, i in enumerate(turma):
                if i[0] == codturma:
                    novo_codturma = input('\nInsira o novo código da turma: ')
                    novo_periturma = input('\nInsira o novo período da turma: ')
                    novo_cdiscturma = input('\nInsira o novo código da disciplina da turma: ')
                    turma[n][0] = novo_codturma
                    turma[n][1] = novo_periturma
                    turma[n][2] = novo_cdiscturma
                    turma.remove(i)
                    np = int(input('Digite a quantidade de professores presentes na lista para alterar: '))
                    na = int(input('Digite a quantidade de alunos presentes na lista para alterar: '))
                    cpfprof = []
                    for k in range(np):        #delimitar a quantidade de professores antes informada
                        cpfprofturma = cpfprof_turma()
                        cpfprof.append(cpfprofturma)
                    cpfaluno = []
                    for k in range(na):        #delimitar a quantidade de alunos antes informada
                        cpfalunoturma = cpfaluno_turma()
                        cpfaluno.append(cpfalunoturma)
                    turma.append([novo_codturma,novo_periturma,novo_cdiscturma, cpfprof, cpfaluno])
                    print('\nTurma alterada com sucesso.')
                    break


        if resposta == 4:      #Menu das turmas
            while True:
                escolha = int(input('''
--------------------------------------------------------------------------
Adicionar turma - 1
Alterar dados de uma turma - 2
Apagar dados de uma turma - 3
Ver lista de turmas - 4
Sair - 5
--------------------------------------------------------------------------
'''))
                if escolha == 5:     #Sair do menu alternativo de turmas
                    break
                elif escolha == 1:   #retorna a função de adicionar turma ao menu alternativo
                    add_turma()
                elif escolha == 4:   #retorna a função de ver lista de turmas no menu alternativo
                    ler_turma()
                elif escolha == 3:   #retorna a função de apagar turma ao menu alternativo
                    del_turma()
                elif escolha == 2:   #retorna a função de alterar dados da turma ao menu alternativo
                    att_turma()

    if resposta == 5:
        print('Fim do programa!\nObrigado por acessar!\nFeito por Matheus Costa')
        break
    
                    
            
                
            
            
            
            
        

                    
                    
                    

