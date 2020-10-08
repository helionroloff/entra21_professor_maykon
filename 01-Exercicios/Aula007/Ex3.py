#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
def media():
    nota1 = float(input('INFORME A NOTA 1: '))
    nota2 = float(input('INFORME A NOTA 2: '))
    nota3 = float(input('INFORME A NOTA 3: '))
    media = float((nota1 + nota2 + nota3)/3)
    print(f'A MÉDIA DAS TRÊS NOTAS É: {media:.1f}')

media()
