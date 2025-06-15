# name = 'Alexander'
#
# for ch in name:  # ['A', 'l', 'e', 'x', 'a', 'n', 'd', 'e', 'r']
#     print(f'Current char is {ch}')
import math
import sys

# import time
#
# for i in range(1, 101, 2):  # [1, 3, 5, ... 99]
#     print(i * 100)
#     time.sleep(1)
#     print('still here')
#     time.sleep(1)

# for i in range(10):  # [0; 10) == [0; 9]
#     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(i)

# for i in range(75, 79):  # [75, 76, 77, 78] ; 79-75==4
#     print(i)

# for i in range(13, 25, 3):  # [13, 13+3==16, 19...]
#     print(i)


# range(1, 10, 3) => [1, 1+3 == 4, 4+3 == 7] => [1, 4, 7]
# for i in range(1, 10, 3):
#     print(i)

# print(list(range(13, 1337, 37)))

# range(1, 10, 77) => [1]  # [1,]
# print(list(range(1, 10, 77)))

# range(100, 10, 5) => []  # 100... 105... 110...
# print(list(range(100, 10, 5)))

# for i in range(100, 9, -5):
#     print(i)


# range(10, 29, -5) => []
# range(39, 29, -5) => [39, 34]
# print(list(range(39, 29, -5)))
# num1 = int(input())
# num2 = int(input())
#
# for i in range(num1, num2, 2):
#     print(i)


# for n in range(2, 12, 2):
#     print(n)
#
#     if n == 6:
#         print('will continue with 6')
#         continue
#
#     print('line 1')
#     # if n == 6:
#     #     print('will break the for-loop')
#     #     break
#
# import time
#
# for attempt in range(1, 7):  # [1, 2, 3, 4, 5, 6]
#     print(f'Attempt No: {attempt}!')
#     time.sleep(1)
#     print('   -> Trying to connect to DataBase...')
#     time.sleep(1)
#
#     # if attempt == 3:
#     #     print('      -> SUCCESS!')
#     #     break
#
#     if attempt == 3:
#         print('continue...')
#         continue
#
#     print('   ->SOME_COMMAND<- (Will skip on attempt 3)')
#     time.sleep(1)
#
# time.sleep(1)
# print('outside for-loop!')

# for num in range(10):
#     if num == 2 or num == 4 or num == 5:
#         continue
#
#     print(num)

# text = 'Anelia'  # ['A'...]
#
# # print(len(text))
# #
# # print(text[0])
# # print(text[1])
# # print(text[2])
#
# for i in range(len(text)):  # range(6) => [0, 1, 2, 3, 4, 5]
#     if i % 2 == 0:
#         print(text[i])  # text[0]; text[2]; text[4]


# print(f'{sys.maxsize:,}')
# print(type(sys.maxsize))  # <class 'int'>
#
# max_num = math.inf
# print(max_num)
# print(type(max_num))
#
# print(sys.maxsize > math.inf)

# for i in range(10_000):
#     print(i)
#
# print(10_000)
# print(type(10_000))


my_inf_value_1 = math.inf
my_inf_value_2 = float('inf')

print(my_inf_value_2)  # inf
print(type(my_inf_value_2))  # <class 'float'>

print(my_inf_value_1 == my_inf_value_2)  # True
print(my_inf_value_1 > my_inf_value_2)  # False
