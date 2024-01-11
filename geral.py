agenda = dict()
def incluirContato(n, t):
    if n == '' or t == '':
        print('Erro! Nome ou telefone não preenchido.')

    else:
        agenda[f'{n}'] = {
            'telefone':t
        } 
        agenda.copy()
        print(agenda)
        print('cadastro realizado com sucesso!')


def alterarContato(n, t):
    if n in agenda.keys():
        print(agenda[n])
        agenda[n].update({'telefone':t})
        print(agenda)

    else:
        print('''Pessoa não cadastrada!
              [ 1 ] - cadastrar
              [ 2 ] - sair
              ''')
        op = int(input('qual sua escolha: '))
        if op == 1:
            nome = str(input('seu nome: '))
            telefone = str(input('seu telefone: '))
            incluirContato(nome, telefone)
        
        elif op == 2:
            print('até logo!')

        


def excluirContato(n):
    if n in agenda.keys():
        agenda.pop(n)
        print(agenda)
        print('contato removido com sucesso!')
    
    else:
        print('Contato já exlcuido!')

def consultarContato(n):
    if n in agenda.keys():
        agenda[n]
        print(f'contato solicitado:{n}, {agenda[n]}')
    
    else:
        print('contato inexistente!')
        print('''Pessoa não cadastrada!
              [ 1 ] - cadastrar
              [ 2 ] - sair
              ''')
        op = int(input('qual sua escolha: '))
        if op == 1:
            nome = str(input('seu nome: '))
            telefone = str(input('seu telefone: '))
            incluirContato(nome, telefone)
        
        elif op == 2:
            print('até logo!')

def consultarContatos(a):
    if len(a.keys()) > 0:
        print(a.keys())

    else:
        print('agenda vazia!')
        print('''Pessoa não cadastrada!
              [ 1 ] - cadastrar
              [ 2 ] - sair
              ''')
        op = int(input('qual sua escolha: '))
        if op == 1:
            nome = str(input('seu nome: '))
            telefone = str(input('seu telefone: '))
            incluirContato(nome, telefone)
        
        elif op == 2:
            print('até logo!')
       

def limparAgenda(a):
    if len(a) == 0:
        print('agenda vazia!')
    
    else:
        a.clear()
        print(a)
        print('agenda exluida com sucesso!')
