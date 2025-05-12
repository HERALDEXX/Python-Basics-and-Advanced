'''
    1. Syntax error
    2. Semantic error
    3. Runtime error
'''

print('Hello') # ==> Romoving one ' with result in syntax error


first = input ('First Input:')
second = input('Second Input:')
answer = first + second
print(answer)
'''
- Here, we want to add two numbers using the first and second output.
If we input numbers in both as the first and second input,
it won't add them both it will ONLY join or concatenate them.
this is a Semantic error. The code runs well but doesn't perform the desired operation.
'''


number_1 = int(input('Please enter a number:'))
number_2 = int(input('Please enter the second number'))
result = number_1 + number_2
print(result)
'''
- If you enter a number as the first input and a letter as the second input,
you will get a runtime error because you can't add a letter and a number.
This is a runtime error because it's ONLY evident in the output.
'''