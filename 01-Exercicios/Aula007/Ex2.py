
#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string

numero1 = int(input('INFORME O PRIMEIRO NÚMERO: '))
numero2 = int(input('INFORME O PRIMEIRO NÚMERO: '))

def divisao(a,b):
    if b == 0:
        resultado = 'não é possível realizar divisão por 0'
    else:
        resultado = int(a/b)
    return resultado
    
resultado=divisao(numero1,numero2)
print(f'o resultado da operação é {resultado}')