# # 1.
#
# for n in range(2, 7, 2):  # [2, 4, 6]
#     print(n)

# # 2.
# for ch in 'Simo':  # ['S', 'i', 'm', 'o']
#     print(ch)

# name = input()  # 1. init
#
# while name != 'End':
#     if name == 'Nakov':
#         print('will skip with Nakov')
#         name = input()
#         continue
#
#
#     print(f'Hello mr. {name}!')
#
#     name = input()  # 3. potential change

# while True:
#     name = input()
#
#     if name == 'End':
#         break
#
#     print(f'Hello mr. {name}!')

# import time
#
# should_break = False
# for week in range(1, 5):  # [1, 2, 3, 4]
#     time.sleep(1)
#     print(f'current week - {week}!')
#
#     for day in range(1, 8):  # [1, 2, 3, 4, 5, 6, 7]
#         if week == 2 and day == 3:
#             should_break = True
#             break
#
#         time.sleep(1)
#         print(f'   -> current day - {day}!')
#
#     if should_break:
#         break
#
#     print(' ! END OF CURRENT WEEK !')
# print(' ! END OF CURRENT WEEK !')

# should_break = False
# for i in range(5):  # [0, 1, 2, 3, 4]
#     for j in range(3):  # [0, 1, 2]
#
#         if i == 2 and j == 1:
#             should_break = True
#             break
#
#         print(f'i={i}, j={j}')
#
#     if should_break:
#         break
#
#

name = 'Simeon'
# name[0]  # 'S'

# pos = 0
# for ch in name:
#     print(f'char is {ch}, position is - {pos}')
#     pos += 1

# for idx, char in enumerate(name):  # [ (0, 'S'), (1, 'i'), ... (5, 'n')]
#     print(f'char is {char}, position is - {idx}')

num = 1234

num_as_str = str(num)  # str(1234) == '1234'

for digit in num_as_str:
    print(digit)
    digit_as_in = int(digit)  # int('1') == 1
    print(digit_as_in * 10)  # '1' * 10  # '1' + '1'


