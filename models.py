import json
from storage import load_scrap
def show_all():
    load_scrap()
    lista_livros = []
    with open('books.json', 'r') as arquivo:
        dados = json.load(arquivo)
        for j in dados:
            nome_livro = j["titulo"]
            lista_livros.append(nome_livro)
    return lista_livros






def procurar_preco(livro):
    load_scrap()
    with open('books.json', 'r') as arquivo:
        dados = json.load(arquivo)
        for preco in dados:
            if livro == preco["titulo"]:
                preco_livro = preco["preco"]
                return preco_livro
