'''
Process of creating function:
1. Start with a keyword def
2. name of the function (only allows letters, numbers and underscores)
    - You cannot start a function name with a number
    - Function name cannot have a space
    - You cannot use python keywords as function names
3. Open and close parenthesis e.g ()
4. Colon e.g :
5. Body of the function    
'''


def add_numbers(num1, num2):
    sum = num1 + num2
    print('This is the result of your summation')
    return sum

result = add_numbers(26, 34)
print(result)

def christmas_tree(height):
    for i in range(1, height + 1):
        space = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        print(space + stars)
    print(' ' * (height - 1) + '|')

christmas_tree(6)
    