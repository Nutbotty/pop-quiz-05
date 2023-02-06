def calculate_pay(hours, wage):
    """
    Calculates pay


    :param hours: positive number
    :param wage: positive number
    :precondition: hours must be a positive number
    :precondition: wage must be a positive number
    :postcondition: returns the calculated pay of hours and wage
    :return: weekly_pay as a float
    >>> calculate_pay(0, 0)
    0
    >>> calculate_pay(40, 10)
    400
    >>> calculate_pay(45, 10)
    500
    """
    weekly_pay = 0
    if hours <= 0 or wage <= 0:
        return weekly_pay
    if hours <= 40:
        weekly_pay += hours*wage
    if hours-40 > 0:
        weekly_pay += ((hours-40)*wage*2) + 40*wage
    return weekly_pay


def main():

    if __name__ == "__main__":
        main()
