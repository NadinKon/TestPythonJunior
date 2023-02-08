import ccxt
#Задание 1: считывать текущую цену пары XRP/USDT

exchange = ccxt.binance()
symbol = 'XRP/USDT'

ohlcv = exchange.fetch_ohlcv(symbol, '1h', limit=2)
max_price_1h = ohlcv[-1][2]

while True:
    ticker = exchange.fetch_ticker(symbol)
    price = ticker['last']
    if price > max_price_1h:
        max_price_1h = price
    if price < (max_price_1h * 0.99):
        print(f"Price of {symbol} has fallen by 1% in the last hour: {price}")

#Задание 2:
#Ответ: как вариант доработать данную программу, можно создать список из пар, и в цикле запускать для каждой пары отдельный поток
