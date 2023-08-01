"""
A rubber ball is dropped from a height of 100 meters and each time it hits the
ground, it bounces back up to 3/5 the height it fell. Write a program bounce.py
that prints a table showing the height of the first 10 bounces.
"""


def bouncing_ball() -> None:
    height = 100

    for n_bounce in range(1, 11):
        height -= ( height * 2 ) / 5
        print(f"{ n_bounce= }, height={ round(height, 4) }")

