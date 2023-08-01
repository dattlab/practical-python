"""
One morning, you go out and place a dollar bill on the sidewalk by the Sears
tower in Chicago. Each day thereafter, you go out double the number of bills.
How long does it take for the stack of bills to exceed the height of the tower?
"""

def double_bills() -> None:
    bill_thickness = 0.11 * 0.001  # 0.11 mm converted to Meters
    tower_height = 442  # in Meters
    num_bills = 1
    day = 1

    while num_bills * bill_thickness <= tower_height:
        num_bills *= 2
        day += 1

    return day

