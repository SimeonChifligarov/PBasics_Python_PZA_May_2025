age = float(input())
gender = input()

if gender == 'm':
    if age >= 16:
        print('Mr.')
    else:
        print('Master')
# if gender == 'f':  # else:
# else:
elif gender == 'f':
    if age >= 16:
        print('Ms.')
    else:
        print('Miss')
