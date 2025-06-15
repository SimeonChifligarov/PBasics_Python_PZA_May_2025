# буква	a	e	i	o	u
# стойност	1	2	3	4	5

word = input()

total_sum = 0
for ch in word:
    if ch == 'a':
        total_sum += 1
    elif ch == 'e':
        total_sum += 2
    elif ch == 'i':
        total_sum += 3
    elif ch == 'o':
        total_sum += 4
    elif ch == 'u':
        total_sum += 5

print(total_sum)
