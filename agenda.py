import os

AGENDA = {}

def mostrar_contatos():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
            print('--------------------------------')
    else:
        print('>>>>Agenda vazia<<<<')

def buscar_contato(contato):
    try:
        print('Nome:',contato)
        print('Telefone:',AGENDA[contato]['telefone'])
        print('E-mail:',AGENDA[contato]['email'])
        print('Endereço:',AGENDA[contato]['endereco'])
    except KeyError:
        print('>>>>Contato inexistente!!<<<<')
    except Exception as error:
        print('>>>>Contato inexistente!!<<<<')
        print(error)

def ler_detalhes_contato():
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    endereco = input('Digite o endereço do contato: ')
    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA [contato]={
        'telefone':telefone,
        'email': email,
        "endereco": endereco,
    }
    salvar()
    print(f'\n>>>>Contato: {contato}, adicionado/editado com sucesso<<<<\n')

def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print(f'\n>>>>Contato: {contato}, excluido com sucesso<<<<\n')
    except KeyError:
        print('>>>>Contato inexistente!!<<<<')
    except Exception as error:
        print('>>>>Contato inexistente!!<<<<')
        print(error)

def exportar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'w') as arquivo:
            # arquivo.write('Nome, Telefone, E-mail, Endereço\n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco'] 
                arquivo.write(f'{contato},{telefone},{email},{endereco}\n')
        print('\n>>>>Agenda exportada com sucesso<<<<')        
    except Exception as error:
        print('>>>>Erro ao exportar arquivo<<<<')
        print(error)

def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)                
    except FileNotFoundError:
        print('>>>>Arquivo não encontrado<<<<')
    except IndexError:
        print('Arquivo invalido, verifique linhas no final do arquivo')
        raise TypeError('Erro, linhas em branco no final do arquivo!')
    except Exception as error:
        print('>>>>Erro inexperado <<<<')
        print(error)

def salvar():
    exportar_contatos('database.csv')

def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(',')
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA [nome]={
                    'telefone':telefone,
                    'email': email,
                    "endereco": endereco,
                }
        print('\n>>>>Dados carregados com sucesso!<<<<')
        print(f'{len(AGENDA)} contato{"s" if len(AGENDA)> 1 else ""} carregado{"s" if len(AGENDA)> 1 else ""}.')
    except FileNotFoundError:
        print('>>>>Arquivo não encontrado<<<<')
    except IndexError:
        print('Arquivo invalido, verifique linhas no final do arquivo')
        raise TypeError('Erro, linhas em branco no final do arquivo!')
    except Exception as error:
        print('>>>>Erro inexperado <<<<')
        print(error)

def imprimir_menu():
    print('-----------------------------------------')
    print('1 - Mostrar todos os contatos da agenda')
    print('2 - Buscar contato')
    print('3 - Incluir contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar contato para CSV')
    print('7 - Importar contato para CSV')
    print('0 - Fechar agenda')
    print('-----------------------------------------')

carregar()     
while True:
    # os.system('clear')
    imprimir_menu()

    opcao = input('\nDigite uma das opções: \n')
    # print(f'\nVocê escolheu:{opcao}\n')
    if opcao == '1':
        mostrar_contatos()
        
    elif opcao == '2':
        contato = input('Digite o nome do contato: ')
        buscar_contato(contato)
    
    elif opcao == '3':
        contato = input('Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print(f'>>>>Contato, {contato} já existe<<<<')
        except KeyError :
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    
    elif opcao == '4':
        contato = input('Digite o nome do contato: ')

        try: 
            AGENDA[contato]
            print(f'>>>>Editando contato: {contato}<<<<')
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco) 
        except KeyError :
            print(f'>>>>Contato, {contato} inexistente<<<<')

    elif opcao == '5':
        contato = input('Digite o nome do contato: ')
        excluir_contato(contato)
    
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)
    
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        importar_contatos(nome_do_arquivo)

    elif opcao == '0':
        print('Até mais!')
        break
    else:
        print('>>>>Opção invalida<<<<!! ')

