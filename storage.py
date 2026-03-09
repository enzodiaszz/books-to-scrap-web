from bs4 import BeautifulSoup
import requests
import json
def get_html():
    url = "https://books.toscrape.com/"
    resp = requests.get(url)
    if resp.status_code == 200:
        html_books = resp.text
        soup = BeautifulSoup(html_books, 'html.parser')
        return soup
    else:
        return ValueError
    

livros = get_html()
livros = livros.find_all('article', class_='product_pod')
def load_scrap():
    dados_salvar = []
    for livro in livros:
        titulo = livro.h3.a['title']
        preco = livro.find('p', class_='price_color').get_text()
        dados_salvar.append({"titulo": titulo, "preco": preco})
    with open('books.json', 'w') as arquivo:
        json.dump(dados_salvar, arquivo, indent=4)

load_scrap()
    