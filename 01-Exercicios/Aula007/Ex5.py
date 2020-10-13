#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função

def calculo_raiz(numero,raiz):
    resultado_raiz=numero**(1/raiz)
    return resultado_raiz
  
numero = int(input('informe o número que deseja calcular a raiz: '))
raiz = int(input('informe o número que deseja calcular a raiz: '))

resultado=calculo_raiz(numero,raiz)

print(f'O resultado do numero {numero} pela raiz de {raiz} é: {resultado}')
