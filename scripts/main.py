from scraper import get_portfolio
from get_financials import get_total_acoes, get_total_moedas
from spreadsheet import create_table, insert_images
from get_qrcode import generate_qrcode
from plots import generate_plots

if __name__ == "__main__":

    url = input("Inserir URL da carteira de investimentos: \n")
    url = "https://luisfelipealeluia.github.io/carteira-investimentos/portfolios/portfolio-3"

    portfolio = get_portfolio(url)

    acoes = [x["Ação"] for x in portfolio["acao"]]
    acoes_quant = [int(x["Quantidade"]) for x in portfolio["acao"]]

    moedas = [x["Moeda"] for x in portfolio["moeda"]]
    moedas_quant = [int(x["Quantidade"]) for x in portfolio["moeda"]]

    tot_acoes = get_total_acoes(acoes, acoes_quant)
    tot_moedas = get_total_moedas(moedas, moedas_quant)

    total = tot_acoes + tot_moedas
    create_table(total)

    qrcode = round(sum([x[3] for x in total]), 2)
    generate_qrcode(f"R$ {qrcode:,.2f}")

    generate_plots()
    insert_images()
