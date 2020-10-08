#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter 
#--- resultado esperado: -------------- Cadastro Serasa --------------------------
#--- O cabeçalho deve conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

empresa = input('INFORME O NOME DA EMPRESA QUE DEVERÁ SER IMPRESSO NO CABEÇALHO: ')

def cabecalho(nome):
    print(f'{"*"*14} Cadastro {nome} {"*"*14}')

cabecalho(empresa)
