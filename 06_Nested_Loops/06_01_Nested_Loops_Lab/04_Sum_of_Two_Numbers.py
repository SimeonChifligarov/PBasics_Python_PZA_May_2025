interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

combination_number = 0
is_combination_found = False
for n1 in range(interval_start, interval_end + 1):
    for n2 in range(interval_start, interval_end + 1):
        combination_number += 1
        if n1 + n2 == magic_number:
            print(f'Combination N:{combination_number} ({n1} + {n2} = {magic_number})')
            is_combination_found = True
            break

    if is_combination_found:
        break

if not is_combination_found:
    print(f'{combination_number} combinations - neither equals {magic_number}')