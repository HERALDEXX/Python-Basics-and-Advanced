'''
int
float
complex
'''

num_1 = 5 # ==> int
num_2 = 2.343398567 # ==> float
num_3 = 7j + 3 # ==> complex
print(type(num_1))
print(type(num_2))
print(type(num_3))


'''
Type Conversion:
'''

number_1 = 5
number_1 = float(number_1)
print(type(number_1))
print(number_1)


'''
Generate a random number between 1 and 7:
'''

import random
print(random.randint(1,7))
'''
Generate 5 numbers from the given set:
'''
print(random.sample((1,2,3,4,5,6,7,8,9,10), 5))