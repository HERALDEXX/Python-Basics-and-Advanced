'''
ADDING SET ITEMS:
'''
our_set = {'Ade', 'James', 'Herald'}

# Adding a Single item to a set:
our_set.add('Sandra')
print(our_set)


# Adding multiple items to a set:
our_set_2 = {'Idara', 'Prosper', 'Mark'}
our_set.update(our_set_2)
print(our_set)



'''
REMOVING SET ITEMS:
'''
my_set = {'Ade', 'James', 'Herald', 'Tom'}

# Remove a single SPECIFIED item from a set:
my_set.discard('Tom')
print(my_set)
'''NOTE: discard() will NOT raise an error 
even if the specified item does not exist in the set
but remove() will raise an error in this case.
EXAMPLE:'''
my_set.discard('Paul')
print(my_set)

# Removes a Single random item from a set:
my_set.pop()
print(my_set)

