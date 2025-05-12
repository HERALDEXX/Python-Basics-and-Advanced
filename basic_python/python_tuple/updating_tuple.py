fruits = ('pineapple', 'avocado', 'banana', 'apple', 'avocado')
fruits_2 = ('kiwi',)
'''
Work-arounds to update a tuple:
    1. Convert the tuple to list.
    2. Make your modifications to the list.
    3. Convert the list back to a tuple.
EXAMPLE:    
'''
# Step 1:
fruit_list = list(fruits)

# Step 2:
fruit_list[-1] = 'PawPaw'

# Step 3:
fruits = tuple(fruit_list)
print(fruits)


'''
Joining Tuples:
'''
fruits += fruits_2
print(fruits)
