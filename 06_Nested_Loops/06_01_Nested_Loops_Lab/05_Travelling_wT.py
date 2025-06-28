# 1.

while True:
    destination = input()  # 'End', or destination_as_str, e.g. 'Greece'

    if destination == 'End':
        break

    destination_cost = float(input())

    saved_amount = 0.0
    # while saved_amount < destination_cost:
    while True:
        current_amount = float(input())  # float('300.00') == 300.00
        saved_amount += current_amount

        if saved_amount >= destination_cost:
            break

    print(f'Going to {destination}!')
