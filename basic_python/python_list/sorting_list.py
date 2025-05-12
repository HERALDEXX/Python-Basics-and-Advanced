countries = ['Nigeria', 'Ghana', 'Cameroon', 'Chad', 'Togo']
countries.sort() # ==> Sorts the list items alpahbetically
print(countries)

numbers = [400, 20, 3, 500, 45]
numbers.sort() # ==> Sorts the lists items numerically in ascending order
print(numbers)

numbers.sort(reverse=True) # ==> Sorts the list items numerically, but in descending order
print(numbers)

'''
Reverse the arrangement of the list items:
'''
countries.reverse()
print(countries)