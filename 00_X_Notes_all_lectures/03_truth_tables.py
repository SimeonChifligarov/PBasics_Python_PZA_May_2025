# from https://discuss.codecademy.com/t/what-is-the-order-of-operations-for-logical-operators/452126/3
# print(True or False and False)     # and has precedence
# print((True or False) and False)   # parentheses change precedence
#
# print(not False or True)        # not has precedence
# print(not (False or True))      # parentheses change precedence

print('Logical AND:')
print(f'T and T == {True and True}')
print(f'T and F == {True and False}')
print(f'F and T == {False and True}')
print(f'F and F == {False and False}')

print('----')
print('Logical OR:')
print(f'T or T == {True or True}')
print(f'T or F == {True or False}')
print(f'F or T == {False or True}')
print(f'F or F == {False or False}')

print('---')
print('Logical NOT')
print(f'not T == {not True}')
print(f'not F == {not False}')
