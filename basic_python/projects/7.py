'''Write a function that takes a list of integers and returns a new list with all the duplicate values removed.'''

def remove_duplicates(int_list):
    return list(set(int_list))

example_list = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(example_list))