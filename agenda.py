from geral import*

while True:
    print('''
    Agenda eletrônica:
    [ 1 ] - incluir contato
    [ 2 ] - alterar contato
    [ 3 ] - excluir contato
    [ 4 ] - consultar contato
    [ 5 ] - consultar todos contatos
    [ 6 ] - limpar agenda
    [ 7 ] - sair 


    ''')

    opção = int(input('qual sua opção: '))

    if opção == 1:
        nome = str(input('seu nome: '))
        telefone = str(input('seu telefone: '))
        incluirContato(nome, telefone)
        
            
    elif opção == 2:
        nome = str(input('procurar nome: '))
        telefone = str(input(' incluir telefone: '))
        alterarContato(nome, telefone)
    
    elif opção == 3:
        nome = str(input('qual nome para excluir: '))
        excluirContato(nome)

    elif opção == 4:
         nome = str(input('qual nome para consultar: '))
         consultarContato(nome)

    elif opção == 5:
        consultarContatos(agenda)

    elif opção == 6:
        limparAgenda(agenda)

    elif opção == 7:
        print('até logo!')
        break
        
    else:
        print('opção invalida!')

    