set1 = {1, 2,6}

set2 = {44, 7, 9}

my_tuple = (3, 8, 9)
'''
    1. union() and update()
    2. intersecton()
    3. difference()
    4. symmetric_difference
'''

set3 = set1.union(set2)
print(set3)

set4 = set1 | set2
print(set4)

merged = set1.union(my_tuple)
print(merged)