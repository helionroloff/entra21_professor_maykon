#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
#        a função deve retornar um endereço cadastrado na função do ex2 filtrando por 
#            id da pessoa


def enderecos_cadastrados(lista):
    print(f'{"*"*5}LISTA DE ENDEREÇOS CADASTRADOS{"*"*5}')
    for i in lista:
        print('\n')
        print('*'*10)
        print(f" id titular do registro do endereço: {i['id']}")
        print(f" rua: {i['rua']}")
        print(f" número: {i['numero']}")
        print(f" complemento: {i['complemento']}")
        print(f" bairro: {i['bairro']}")
        print(f" cidade: {i['cidade']}")
        print(f" estado: {i['estado']}")
        print('*'*10)
        print('\n')


def enderecos_por_id(lista):
    id = int(input('\n informe o id do endereço que deseja consultar: '))
    for endereco in lista:
        for chaves , valores in endereco.items():
            if chaves == 'id' and valores == id:
                print('\n')
                print('*'*10)
                print(f"rua: {endereco['rua']}")
                print(f"número: {endereco['numero']}")
                print(f"complemento: {endereco['complemento']}")
                print(f"bairro: {endereco['bairro']}")
                print(f"cidade: {endereco['cidade']}")
                print(f"estado: {endereco['estado']}")
                print('*'*10)
                print('\n')
            