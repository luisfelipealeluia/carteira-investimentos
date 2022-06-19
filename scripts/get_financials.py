import yfinance as yf

def get_total_acoes(cod, quant):
    
    tickers = yf.Tickers(cod)
    tickers = tickers.tickers
    
    prices = []
    names = []
    currencies = []
    
    for elem in cod:
        data = tickers[elem].info
        
        if data["currency"] == "BRL":
            exchange = 1
        else:
            exchange = yf.Ticker(f"BRL{data['currency']}=X").info["previousClose"]
        
        prices.append(round(data["previousClose"] * exchange, 2))
        names.append(data["shortName"])
        currencies.append(data["financialCurrency"])
        
    total = list(zip(prices, quant))
    total = [x * y for x, y in total]
    
    return list(zip(names, cod, currencies, total))


def get_total_moedas(cod, quant):
    
    tickers = yf.Tickers(cod)
    tickers = tickers.tickers
    
    prices = []
    names = []
    currencies = []
    
    for elem in cod:
        data = tickers[elem].info
        prices.append(data["previousClose"])
        names.append(data["shortName"])
        currencies.append(data["currency"])
        
    total = list(zip(prices, quant))
    total = [x * y for x, y in total]
    
    return list(zip(names, cod, currencies, total))

