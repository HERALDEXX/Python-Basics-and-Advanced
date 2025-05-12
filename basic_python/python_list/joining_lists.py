tech_companies = ['Netflix', 'Microsoft', 'Amazon', 'Apple']
new_list = ['IBM', 'NVIDIA', 'NOKIA']

# Using Concatenation:
joined_list = tech_companies + new_list
print(joined_list)

# Using for loop:
for company in new_list:
    tech_companies.append(company)
print(tech_companies)