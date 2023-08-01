"""
Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with
Guido’s Mortgage, Stock Investment, and Bitcoin trading corporation. The
interest rate is 5% and the monthly payment is $2684.11. Calculate the total
amount that Dave will have to pay over the life of the mortgage.
"""

def dave_mortgage() -> None:
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0

    while principal > 0:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment 

    return round(total_paid, 2)


def extra_payments() -> None:
    """
    Suppose Dave pays an extra $1000/month for the first 12 months of the
    mortgage?

    Modify the first function to incorporate this extra payment and have it print the
    total amount paid along with the number of months required.
    """
    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0

    additional_pay = 1000
    curr_month = 1
    end_month = 12

    while principal > 0:
        if curr_month > end_month:
            additional_pay = 0
        curr_month += 1

        principal = principal * (1+rate/12) - (payment + additional_pay)
        total_paid = total_paid + payment + additional_pay

    return round(total_paid, 2)


def extra_payment_calculator() -> None:
    """
    Modify the program so that extra payment information can be more generally
    handled
    """
    extra_payment_start_month = 61
    extra_payment_end_month = 108
    extra_payment = 1000

    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0

    curr_month = 1

    while principal > 0 and principal > payment:
        # Additional `and` condition for Exercise 1.11 Bonus
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment

        if extra_payment_start_month <= curr_month <= extra_payment_end_month:
            principal -= extra_payment
            total_paid += extra_payment

        print(f"{curr_month} {round(total_paid, 2)} {round(principal, 2)}")

        curr_month += 1

    print(f"Total paid {round(total_paid, 2)}")
    print(f"Months {curr_month - 1}")

