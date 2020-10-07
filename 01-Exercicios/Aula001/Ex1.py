#--- Exercício 1  - Variáveis
#--- Crie 5 variáveis para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Deve ser usado apenas uma vez a função print()
#--- Cada dado deve ser impresso em uma linha diferente
#--- O salário deve ser de tipo flutuante

nome = 'Raul'
sobrenome = 'Silveira'
cpf = '03859258462'
rg = '6385372'
salario = 2.899

print('''Funcionario:
Nome: {}
Sobrenome: {}
CPF: {}
RG: {}
Salário: {} reais'''.format(nome,sobrenome,cpf,rg,salario))
