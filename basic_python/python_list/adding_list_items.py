tech_companies = ['Netflix', 'Microsoft', 'Amazon']

'''
    1. append() ==> add a single item to the end of a list.
    2. insert() ==> add a single item at a SPECIFIED position in a list.
    3. extend() ==> add multiple items at the end of a list.
'''

tech_companies.append('Google')
print(tech_companies)

tech_companies.insert(0, 'Nokia')
print(tech_companies)

health_companies = ['ALICO', 'Bastion', 'AVON Medical']
tech_companies.extend(health_companies)
print(tech_companies)