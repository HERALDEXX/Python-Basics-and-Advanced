'''Error Handling: Handles specific errors gracefully'''

while True:
    try: 
        num_1_input = int(input("Enter a number: "))
        num_2_input = int(input("Enter another number: "))
        if num_1_input or num_2_input == "":
            raise Exception("Input cannot be empty!") 
        num_1 = num_1_input
        num_2 = num_2_input

        division = num_1 / num_2
        print(f"The result of dividing {num_1} by {num_2} is: {division}")   
    except ValueError:
        print("Please enter a valid number for both inputs!")
        continue
    except ZeroDivisionError:
        print("Division by zero is not valid!\nPlease enter a non-zero number for the second input.")
        continue
    break # Exit the loop if no error occurs 


'''Handles any other unknown errors'''

# try: 
#     num_1 = int(input("Enter a number: "))
#     num_2 = int(input("Enter another number: "))

#     division = num_1 / num_2
#     print(f"The result of dividing {num_1} by {num_2} is: {division}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")


'''else...finally Block'''

# try: 
#     num_1 = int(input("Enter a number: "))
#     num_2 = int(input("Enter another number: "))

#     division = num_1 / num_2
#     print(f"The result of dividing {num_1} by {num_2} is: {division}")
# except ValueError:
#     print("Please enter a valid number for both inputs!")
# except ZeroDivisionError:
#     print("Division by zero is not valid!\nPlease enter a non-zero number for the second input.")
# else:
#     print("Division was successful! No errors occurred")    
# finally:
#     print("Execution of try-except block is completed (disregarding any errors).")    