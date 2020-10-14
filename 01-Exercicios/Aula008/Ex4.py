#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
#        a função deve retornar um endereço cadastrado na função do ex2 filtrando por 
#            id da pessoa


def enderecos_cadastrados_arquivo():
    arquivo = open('banco_enderecos.txt','r')
    for linha in arquivo:
        linha_limpa = linha.strip()
        lista_dados = linha_limpa.split(';')
        print(f"""id: {lista_dados[0]} - rua: {lista_dados[1]} - número: {lista_dados[2]} - complemento: {lista_dados[3]}
        bairro: {lista_dados[4]} - cidade: {lista_dados[5]} - estado: {lista_dados[6]}""")
    arquivo.close()

def endereco_por_id_arquivo():
    arquivo = open('banco_enderecos.txt','r')
    id = input('Informe o ID para consulta: ')
    for linha in arquivo:
        linha_limpa = linha.strip()
        linha_dados = linha_limpa.split(';')
        
        if linha_dados[0] == id:
            print(f"""id: {linha_dados[0]} - rua: {linha_dados[1]} - número: {linha_dados[2]} - complemento: {linha_dados[3]} - bairro: {linha_dados[4]} - cidade: {linha_dados[5]} - estado: {linha_dados[6]}""")
    arquivo.close()
    


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
            