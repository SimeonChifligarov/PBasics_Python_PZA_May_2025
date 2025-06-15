# Напишете програма, която чете n на брой цели числа. Принтирайте
# най-голямото и най-малкото число сред въведените.
# import math

num_count = int(input())

# num_s = math.inf  # requires import math
# num_b = -math.inf
num_s = float('inf')
num_b = float('-inf')
for i in range(num_count):
    number = int(input())
    if number < num_s:
        num_s = number
    if number > num_b:
        num_b = number

print(f'Max number: {num_b}')
print(f'Min number: {num_s}')
