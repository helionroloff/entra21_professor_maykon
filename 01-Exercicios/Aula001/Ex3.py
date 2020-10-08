
#--- Exercício 3  - Variáveis
#--- Imprima dois parágrafos do último livro que você leu
#--- A impressão deve conter informações do livro, que deverão estar em variáveis
#--- As informações do Livro serão: 
#---    Título
#---    Edição
#---    Autor
#---    Data de publicação
#--- Os parágrafos devem estar formatados conforme a formatação do livro

titulo = 'Dom Casmurro'
edicao = 'Edição Especial Editora Carambaia'
autor = 'Machado de Assis'
data_de_publicacao = 1899

print('''Titulo: {}
Edição: {}
Autor: {}
Data de Publicação: {}

“Uma noite destas, vindo da cidade para o Engenho Novo, encontrei no trem da
Central um rapaz aqui do bairro, que eu conheço de vista e de chapéu.
Cumprimentou-me, sentou-se ao pé de mim, falou da Lua e dos ministros, e
acabou recitando-me versos. A viagem era curta, e os versos pode ser que não
fossem inteiramente maus. Sucedeu, porém, que, como eu estava cansado,
fechei os olhos três ou quatro vezes; tanto bastou para que ele interrompesse a
leitura e metesse os versos no bolso.
- Continue, disse eu acordando.
- Já acabei, murmurou ele.
- São muito bonitos.
Vi-lhe fazer um gesto para tirá-los outra vez do bolso, mas não passou do gesto;
estava amuado. No dia seguinte entrou a dizer de mim nomes feios, e acabou alcunhando-me Dom
Casmurro.”'''.format(titulo,edicao,autor,data_de_publicacao))
