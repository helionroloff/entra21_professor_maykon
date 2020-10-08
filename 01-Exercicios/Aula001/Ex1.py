#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome = input('INFORME SEU NOME: ')
sobrenome = input('INFORME SEU SOBRENOME: ')
cpf = input('INFORME SEU CPF: ')
rg = input('INFORME SEU RG: ')
salario = float(input('INFORME SEU SALÁRIO: '))

print('''Funcionario:
Nome: {}
Sobrenome: {}
CPF: {}
RG: {}
Salário: {} reais'''.format(nome,sobrenome,cpf,rg,salario))
