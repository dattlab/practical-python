"""
The columns in data/portfolio.csv correspond to the stock name, number of shares,
and purchase price of a single stock holding. Write a program called pcost.py
that opens this file, reads all lines, and calculates how much it cost to
purchase all of the shares in the portfolio.
"""

import gzip
import csv


def purchase_cost(filename: str) -> float:
    # Uncomment to open the gzip file instead
    # with gzip.open(filename, "rt") as list_stocks:
    with open(filename) as list_stocks:
        total_cost = 0
        list_stocks = csv.reader(list_stocks)
        next(list_stocks)
        for stock in list_stocks:
            try:
                _, num_shares, purchase_price = stock
                total_cost += (float(purchase_price) * int(num_shares))
            except ValueError:
                print("There are some missing fields. Skipping them...")

    return total_cost 

