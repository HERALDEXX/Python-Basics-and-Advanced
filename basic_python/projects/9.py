'''Write a program that calculates the sum of all even numbers between 1 and a given number.'''

def sum_of_evens(n):
    return sum(number for number in range(2, n + 1, 2))

# Example usage
given_number = int(input("Enter a number (Upper Limit): "))
print(sum_of_evens(given_number))
