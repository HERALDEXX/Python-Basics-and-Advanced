'''Create a program that takes a list of strings and returns the longest string in the list'''

def longest_string(strings):
    if not strings:
        return None
    
    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest

# Example usage
strings_list = ["apple", "banana", "cherry", "date"]
print(f"The longest string in the list is: {longest_string(strings_list)}")