# На всеки ред ще получавате сумата,
# която трябва да внесете в сметката,
# до получаване на команда  "NoMoreMoney ".

# total_amount = 0.0
# while True:
#     command = input()  # 'NoMoreMoney' OR float_as_string, e.g. '3.56'
#
#     if command == 'NoMoreMoney':
#         break
#
#     current_amount = float(command)  # float('3.56') == 3.56
#
#     if current_amount < 0:
#         print('Invalid operation!')
#         break
#
#     total_amount += current_amount
#     print(f'Increase: {current_amount:.2f}')
#
# print(f'Total: {total_amount:.2f}')

total_amount = 0.0

command = input()  # 1. init
while command != 'NoMoreMoney':  # 2. check
    current_amount = float(command)  # float('3.56') == 3.56

    if current_amount < 0:
        print('Invalid operation!')
        break

    total_amount += current_amount
    print(f'Increase: {current_amount:.2f}')

    command = input()  # 3. potential change

print(f'Total: {total_amount:.2f}')
