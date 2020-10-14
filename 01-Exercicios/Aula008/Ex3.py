# --- Exercício 3  - Funções
# --- Escreva uma função para listar pessoas cadastradas:
# ---    a função deve retornar todas as pessoas cadastradas na função do ex1
# --- Escreva uma função para exibi uma pessoa específica:
# a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id



def pessoas_cadastradas_arquivo():

    arquivo = open('banco_pessoas.txt','r')
    for linha in arquivo:
        linha_limpa = linha.strip()
        lista_dados = linha_limpa.split(';')
        print(f"nome: {lista_dados[0]} - sobrenome: {lista_dados[1]} - idade: {lista_dados[2]} - id: {lista_dados[3]}")
    arquivo.close()


def pessoa_por_id_arquivo():
    #id = input('\n Informe o id pessoal para consulta: ')
    arquivo = open('banco_pessoas.txt','r')
    id = input('Informe o ID para consulta: ')
    for linha in arquivo:
        linha_limpa = linha.strip()
        linha_dados = linha_limpa.split(';')
        if linha_dados[3] == id:
            print(f'ID: {linha_dados[3]} - nome: {linha_dados[0]} - sobrenome: {linha_dados[1]} - idade {linha_dados[2]}')
    arquivo.close()




def pessoas_cadastradas(lista):
    for i in lista:
        print(f" id: {i['id']}")
        print(f" nome: {i['nome']}")
        print(f" sobrenome: {i['sobrenome']}")
        print(f" idade: {i['idade']}")
        print('\n')


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

    


