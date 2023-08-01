import csv


def purchase_cost(filename: str) -> float:
    """Computes the total cost (shares * price) of a portfolio file"""
    total_cost = 0

    with open(filename) as list_stocks:
        list_stocks = csv.reader(list_stocks)
        next(list_stocks)
        for stock in list_stocks:
            try:
                _, num_shares, purchase_price = stock
                total_cost += (float(purchase_price) * int(num_shares))
            except ValueError:
                print("There are some missing fields. Skipping them...")

    return total_cost 


def read_portfolio(filename: str) -> list[dict]:
    portfolio_list = []

    with open(filename) as stocks:
        list_stocks = csv.reader(stocks)

        next(list_stocks)
        for stock in list_stocks:
            portfolio_list.append(
                {
                    "name": stock[0],
                    "shares": stock[1],
                    "price": stock[2]
                }
            )

    return portfolio_list


def read_prices(filename: str) -> dict:
    prices_dict = {}

    with open(filename) as f:
        list_prices = csv.reader(f)

        for price in list_prices:
            if len(price):
                prices_dict[price[0]] = float(price[1])

    return prices_dict

