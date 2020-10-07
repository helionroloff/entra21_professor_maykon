#--- Exercício 2  - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

opcao=int(input(F'''
{"*"*5} CADASTRO DE PESSOAS PARA EMPRESA PYTHONS{"*"*5}



1 - Cadastrar funcionário
2 - Listar funcionários
3 - Editar funcionário
4 - Deletar funcionário
5 - Sair



ESCOLHA A OPÇÃO DESEJADA: 
'''))
if opcao == 1:
    print(f'''{"*"*5} Cadastro de novo funcionário {"*"*5}
        Nome: 
        Sobrenome: 
        CPF: 
        RG: 
        Salário: 
    ''')
elif opcao == 2:
    print(f'''{"*"*5} Lista de funcionarios {"*"*5}
    funcionarios 
    ''')
elif opcao == 3:
    print(f'''{"*"*5} Edição de dados de funcionarios {"*"*5}
    ''')
elif opcao == 4:
    print(f'''{"*"*5} Deletar funcionario {"*"*5}
    ''')
elif opcao == 5:
    print(f'''{"*"*5} Obrigado. {"*"*5}
    ''')
else:
    print(''' OPÇÃO INVÁLIDA ''') 
