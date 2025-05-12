tech_companies_1 = ['Netflix', 'Microsoft', 'Amazon', 'Apple']
# Using the copy() method:
tech_companies_2 = tech_companies_1.copy()
#Using the list() function:
tech_companies_3 = list(tech_companies_1)
# Using the slicing operator:
tech_companies_4 = tech_companies_1[:]

tech_companies_2.append('Nokia')
tech_companies_2.append('IBM')
tech_companies_2.remove('Netflix')
tech_companies_3.append('NVIDIA')

print(tech_companies_1)
print(tech_companies_2)
print(tech_companies_3)
print(tech_companies_4)