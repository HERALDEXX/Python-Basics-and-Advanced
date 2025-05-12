countries = ['Nigeria', 'Ghana', 'Cameroon', 'Chad', 'Togo']

print(countries[0]) # ==> Print only the item with index 0 (The first item)
print (countries[2]) # ==> Print only the item with index 2 (The third item)

'''
Negative Indexing:
'''
print(countries[-1]) # ==> Print only the item with index -1 (The last items)


'''
Range of indexes:
'''
print(countries[0:2]) # ==> Print only the items with index 0 and index 1 (The first and second items)
print(countries[:3]) # ==> Print only the items from the first item to the item before index 3 (The first, second and third items)


'''
Conditional Statements:
'''
if 'Mali' in countries:
    print('Yes, Mali is in countries!!!')
else:
    print('No, Mali does not exist in countries')
