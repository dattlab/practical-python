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


def compute_profit(stock_data_file: str, price_data_file: str) -> tuple:
    stock_data: list[dict] = read_portfolio(stock_data_file)
    price_data: dict = read_prices(price_data_file)
    portfolio_purchase_value = purchase_cost(stock_data_file)

    loss = 0
    gain = 0

    for stock in stock_data:
        purchase_price = float(stock["price"])
        curr_price = price_data[stock["name"]]

        stock_gain = (curr_price - purchase_price) / purchase_price

        if stock_gain > 0:
            gain += stock_gain
        else:
            loss += stock_gain

    portfolio_curr_value = portfolio_purchase_value * (loss + gain)

    return (
        round(portfolio_purchase_value, 2),
        round(portfolio_curr_value, 2),
        round(loss * 100, 2),
        round(gain * 100, 2),
    )


def make_report(stock_data_file: str, price_data_file: str) -> list[tuple]:
    stock_data: list[dict] = read_portfolio(stock_data_file)
    price_data: dict = read_prices(price_data_file)

    report = []
    for stock in stock_data:
        purchase_price = float(stock["price"])
        curr_price = price_data[stock["name"]]

        change = curr_price - purchase_price

        report.append((
            stock["name"], int(stock["shares"]),
            float(curr_price), float(change)
        ))

    return report


def display_price_change(stock_data_file: str, price_data_file: str) -> None:
    report = make_report(stock_data_file, price_data_file)

    print(f"{'Name':>10s} {'Shares':>10s} {'Price':>10s} {'Change':>10s}")
    print(f"{'':->10s} {'':->10s} {'':->10s} {'':->10s}")
    for stock_report in report:
        print("%10s %10d %10.2f %10.2f" % stock_report)

