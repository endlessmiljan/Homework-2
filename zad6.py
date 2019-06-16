def stock_price(request):
    req = request.split()
    #ispod umesto float st
    return float(req[1]) * float(req[2])

#requests = "GOOG 300 542.0 B"
requests = "ZNG 1300 2.66 B,CH15.NY 50 56.32 B,OWW 1000 11.623 B,OGG 20 580.1 B"
price = 0

if requests.count == 1:
    price = stock_price(requests)
else:
    reqs = requests.split(",")
    price_of_each = map(stock_price, reqs)

    price = sum(price_of_each)

if requests.endswith("B"):
    print("Buy: " + str("{0:.2f}".format(price)) + " Sell: 0")

else: 
    print("Buy: 0 " + "Sell: " + str("{0:.2f}".format(price)))





