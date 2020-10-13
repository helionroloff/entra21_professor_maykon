# --- Exercício 3  - Funções
# --- Escreva uma função para listar pessoas cadastradas:
# ---    a função deve retornar todas as pessoas cadastradas na função do ex1
# --- Escreva uma função para exibi uma pessoa específica:
# a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id


def pessoas_por_id(lista):
    id = int(input('\n Informe o id pessoal para consulta: '))
    for pessoa in lista:
        for chaves, valores in pessoa.items():
            if chaves == 'id' and valores == id:
                print('\n')
                print('*'*10)
                print(f"nome: {pessoa['nome']}")
                print(f"sobrenome: {pessoa['sobrenome']}")
                print(f"idade: {pessoa['idade']}")
                print(f"id: {pessoa['id']}")
                print('\n')


def pessoas_cadastradas(lista):
    print('LISTA DE PESSOAS CADASTRADAS')
    for i in lista:
        print(f" id: {i['id']}")
        print(f" nome: {i['nome']}")
        print(f" sobrenome: {i['sobrenome']}")
        print(f" idade: {i['idade']}")
        print('\n')