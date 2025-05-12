'''Create a program that takes a list of numbers and returns the sum of all the even numbers in the list.'''

def sum_of_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"The sum of even numbers in the list is: {sum_of_even_numbers(numbers_list)}")