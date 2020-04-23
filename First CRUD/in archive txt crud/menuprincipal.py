import prof,alunos,disc   #importa todos os .py arquivados no mesmo diretório
while True:
    consulta = int(input('''
    ------------------------------------------------------------------
    QUAIS DADOS DESEJA CONSULTAR EM ARQUIVO?
    Dados de um professor - 1
    Dados de um aluno - 2
    Dados de uma disciplina - 3
    Dados de uma turma - 4
    Sair - 5
    ------------------------------------------------------------------
    '''))
    if consulta == 1:            #vai para o menu dos professores
        prof.menu_prof()
    elif consulta == 2:          #vai para o menu dos alunos
        alunos.menu_alunos()
    elif consulta == 3:         #vai para o menu das disciplinas
        disc.menu_disc()
    elif consulta == 5:
        print('Fim do programa!\nObrigado por acessar!\nFeito por Matheus Costa')
        break
    elif consulta == 4:
        print('Parte de turmas ainda não foi feita!')


        
                   
    
 
