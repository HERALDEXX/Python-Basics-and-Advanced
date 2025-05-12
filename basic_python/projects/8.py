'''Write a function that takes a list of strings and returns a new list with all the vowels removed from each string.'''

def remove_vowels(str_list):
    vowels = "aeiouAEIOU"
    return [''.join([char for char in string if char not in vowels]) for string in str_list]

example_list = ["hello", "world", "example"]
print(remove_vowels(example_list))
