#--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada
pessoas =[]

def cadastro_pessoa(nome, sobrenome, idade):
  cadastro = {}
  cadastro['nome'] = nome
  cadastro['sobrenome'] = sobrenome
  cadastro['idade'] = idade
  if idade < 18:
    print('Erro no cadastro')
  elif idade >= 18:
    cadastro['id'] = len(pessoas)
    pessoas.append(cadastro)
    print(5*'-','CADASTRO REALIZADO COM SUCESSO',5*'-')
    print('O SEU ID É:',cadastro['id'] )
    return cadastro['id']
  else:
    print('Idade incompatível')
