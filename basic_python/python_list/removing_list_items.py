players_life = [1, 2, 3, 4, 5, 6]
tech_companies = ['Netflix', 'Microsoft', 'Amazon', 'Google', 'Apple']
'''
    1. remove() ==> remove a SPECIFIED item from a list.
    2. pop() ==> remove a SPECIFIED ITEM by Index.
    3. del ==> remove a SPECIFIED ITEM by Index and 
                can also delete the list completely.
    4. clear ==> clears all content from a list.
'''

tech_companies.remove('Microsoft')
print(tech_companies)

tech_companies.pop(3) # ==> will remove 'Apple'.
print(tech_companies)

tech_companies.clear()
print(tech_companies)

del(tech_companies) # ==> This will raise an error because the list has been deleted from the memory.
print(tech_companies)