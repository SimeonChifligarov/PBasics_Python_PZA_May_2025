# 1.

destination = input()  # 'End' or destination_as_str, e.g. 'Spain'
while destination != 'End':
    destination_cost = float(input())  # float('1200.00') == 1200.00

    saved_amount = 0.0
    while saved_amount < destination_cost:
        current_amount = float(input())  # float('300.00') == 300.00
        saved_amount += current_amount

    print(f'Going to {destination}!')

    destination = input()  # 3.

