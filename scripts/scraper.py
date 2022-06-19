import requests
from bs4 import BeautifulSoup

from validate_url import validate_url

def table_to_dict(soup, css_class):
    """ 
    Encontra a tag com a classe especificada e cria um 
    dicionário com as informações da tabela no formato 
    key: value onde key é o header da coluna e value é 
    o valor na linha
    
    css_class (string): 
        classe que identifica a div contendo a tabela

    return:
        dados da tabela em formato de lista de dict
    """
    
    div = soup.find(class_=css_class)
    rows = []

    for tr in div.find_all("tr"):
        """
        Cria uma lista para cada linha da tabela
        e a insere em uma nova lista que guarda
        a informação de todas as linhas
        """
        row = [td.string for td in tr]
        row = list(filter(lambda a: a != '\n', row))

        rows.append(row)

    keys = rows.pop(0) # dados do cabeçalho (chaves do dict)

    return [dict(zip(keys, elem)) for elem in rows]


def get_portfolio(url):

    page = validate_url(url)
    soup = BeautifulSoup(page, "html.parser")

    portfolio = {
        "moeda": table_to_dict(soup, "moeda"),
        "acao": table_to_dict(soup, "acao")
    }

    return portfolio


if __name__ == "__main__":

    url = "https://luisfelipealeluia.github.io/carteira-investimentos/portfolios/portfolio-3"
    result = get_portfolio(url)

    print(result)