#--- Exercício 2  - Funções
#--- Escreva uma função para cadastro de endereço:
#---       a função deve receber sete parâmetros, id da pessoa, rua, numero, complemento, bairro, cidade e estado
#---       a função deve salvar os dados de endereço em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de endereços com todos os dados preenchidos
#---       a função deve retornar uma mensagem ao final de acordo com a situação
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada
enderecos =[]


def cadastro_enderecos(id_endereco,rua,numero,complemento,bairro,cidade,estado):
    banco_enderecos = open('banco_enderecos.txt','a')
    endereco = {}
    endereco['id'] = id_endereco
    endereco['rua'] = rua
    endereco['numero'] = numero
    endereco['complemento'] = complemento
    endereco['bairro'] = bairro
    endereco['cidade'] = cidade
    endereco['estado'] = estado
    banco_enderecos.write(f"{endereco['id']};{endereco['rua']};{endereco['numero']};{endereco['complemento']};{endereco['bairro']};{endereco['cidade']};{endereco['estado']}\n")
    banco_enderecos.close()
    enderecos.append(endereco)
    print('CADASTRO REALIZADO COM SUCESSO')


    