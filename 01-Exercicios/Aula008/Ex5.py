#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---       o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---       o programa deve solicitar os dados de endereços utilizados na função do ex2
#---       o programa deve passar o id obtido na função do ex1 para a função do ex2
#---       o programa deve mostrar ao final os dados de todos as pessoas cadastradas 
#                com seus respectivos endereços utilizando as funções do ex3 e ex4




#variaveis em escopo global:
from Ex1 import pessoas
from Ex2 import enderecos

opcao = '0'


#importando funções de outros arquivos:
from Ex1 import cadastro_pessoa
from Ex2 import cadastro_enderecos
from Ex3 import pessoas_cadastradas , pessoas_por_id
from Ex4 import enderecos_cadastrados , enderecos_por_id

#inicio do programa:
while opcao != '6':               
    opcao = input(f'''
    {"*"*50}
    MENU DE CADASTRO DE PESSOAS E ENDEREÇOS:
    1 - CADASTRO DE PESSOAS
    2 - CONSULTA TOTAL DE PESSOAS CADASTRADAS
    3 - CONSULTA POR IP PESSOAS CADASTRADAS
    4 - CONSULTA DE ENDEREÇOS CADASTRADOS
    5 - CONSULTA POR IP DE ENDEREÇOS CADASTRADOS
    6 - SAIR
    {"*"*50}
    INFORME O NÚMERO DA OPÇÃO DESEJADA: ''')
    if opcao == '1':
        # cadastro de nome, sobrenome, idade
        print('\n')
        nome = input('Digite o seu nome: ').strip().title()
        sobrenome = input('Digite seu sobrenome: ').strip().title()
        idade = int(input('Digite sua idade: '))
        print('\n')
        id_pessoa = int(cadastro_pessoa(nome, sobrenome, idade))
        
        
        # cadastro de dados residenciais
        vazio = True
        while vazio == True:
            id_endereco = id_pessoa
            rua = input('Informe o nome da rua: ').strip().title()
            numero = input('Informe o numero do imóvel: ').strip().title()
            complemento = input('Informe o complemento (caso não haja coloque 0): ').strip().title()
            bairro = input('Informe o bairro: ').strip().title()
            cidade = input('Informe a cidade: ').strip().title()
            estado = input('Informe o estado: ').strip().title()
            if rua == '' or numero == '' or complemento == '' or bairro == '' or cidade == '' or bairro == '' or estado == '':
                print('Dados em branco, refaça o cadastro de endereço\n')
                
            else:
                vazio = False
                cadastro_enderecos(id_endereco,rua,numero,complemento,bairro,cidade,estado)
                print('\n')
      

    elif opcao == '2':
        pessoas_cadastradas(pessoas)


    elif opcao == '3':
        pessoas_por_id(pessoas)
        

    elif opcao == '4':
        enderecos_cadastrados(enderecos)
        

    elif opcao == '5':
        enderecos_por_id(enderecos)
            
    
    elif opcao == '6':
        print('OBRIGADO POR UTILIZAR NOSSA APLICAÇÃO')
    
    else:
        print('Opção Inválida')