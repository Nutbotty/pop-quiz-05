def calculate_pay(hours, wage):
    weekly_pay = 0
    if hours <= 0 or wage <= 0:
        return weekly_pay
    count = 1
    while count <= hours:
        if count <= 40:
            weekly_pay += wage
        if count > 40:
            weekly_pay += wage*2
        count += 1
    return weekly_pay


def main():
    example_result = calculate_pay(45, 1)
    print(example_result)

    example_result = calculate_pay(0, 1)
    print(example_result)

    example_result = calculate_pay(30.67, 1)
    print(example_result)


if __name__ == "__main__":
    main()
