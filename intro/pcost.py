"""
The columns in data/portfolio.csv correspond to the stock name, number of shares,
and purchase price of a single stock holding. Write a program called pcost.py
that opens this file, reads all lines, and calculates how much it cost to
purchase all of the shares in the portfolio.
"""


def purchase_cost() -> None:
    with open("data/portfolio.csv") as list_stocks:
        total_cost = 0

        next(list_stocks)
        for stock in list_stocks:
            _, num_shares, purchase_price = stock.split(",")
            total_cost += (float(purchase_price) * int(num_shares))

    return total_cost 
