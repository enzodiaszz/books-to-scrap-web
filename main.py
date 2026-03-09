
from models import procurar_preco, show_all

#storage.py usa as biblliotecas soup e requests pra obter o html da página. a partir disso, o nome e os preços são salvos num json, e posteriormente são lidos pelas funções do models.py.
print(f'Olá! Esse é um Web Scrapper feito a partir de um site demo de venda de livros! \n \n Essas são as opções disponíveis: {show_all()} ')
search_price = str(input('Digite o nome do livro para ver seu preço: '))
print(f'O preço de {search_price} é {procurar_preco(search_price)[2:]}')

