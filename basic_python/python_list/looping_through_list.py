tech_companies = ['Netflix', 'Microsoft', 'Amazon', 'Google', 'Apple']

'''
for Loop:
'''
for y in tech_companies:
    print(y.upper()) # ==> Prints each item of the list separately (and in Upper Case)

'''
while Loop:
'''
i = 0
while i < len(tech_companies):
    print(tech_companies[i])
    i = i + 1

'''
List Comprehension (Shortcut for "for" Loop):
'''    
[print(e.upper()) for e in tech_companies]