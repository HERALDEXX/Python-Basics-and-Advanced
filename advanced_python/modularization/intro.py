'''To display all the available Python modules in your system'''
# print(help("modules"))



'''Datetime Module'''
# # The datetime module supplies classes for manipulating dates and times.
# import datetime

# my_date = datetime.date(2023, 10, 1)

# print("Date passed as an argument:", my_date)
# print(my_date)
# print(type(my_date))



'''Tkinter Module'''
# # Tkinter is the standard GUI toolkit for Python.
# import tkinter as tk

# username = input("Enter your username: ")
# root = tk.Tk()
# root.title("HERALDEXX HABIT TRACKER")
# root.geometry("500x400")

# label = tk.Label(root, text=f"Welcome {username} to HERALDEXX HABIT TRACKER", font=("Arial", 16))
# label.pack(pady=20)

# root.mainloop()



'''Custom Module'''
# # Import all functions from a custom module named Heraldmath:
# import Heraldmath

# # # Specify the function(s) to import from the custom module:
# # from Heraldmath import multiply_num

# multiplication_result = Heraldmath.multiply_num(5, 10)
# print(multiplication_result)

# Using alias 
import Heraldmath as hm

addition_result = hm.add_num(176, 10)
print(addition_result)
