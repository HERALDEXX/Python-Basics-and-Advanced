countries = ['Nigeria', 'Ghana', 'Cameroon', 'Chad', 'Togo']

countries[-1] = 'Mali' # ==> Replaces the item with index -1 (the last item) with 'Mali'
print(countries)

countries[:2] = ['Morocco', 'Rwanda']
'''Replaces the items within the range (Items from the first item to the item with index 1) 
   with the items in the given list'''
print(countries)   


'''
Using insert() method:
'''
countries.insert(0, 'South Africa') 
'''Inserts 'South Africa' at the postion of index 0 without replacing any existing items'''
print (countries)