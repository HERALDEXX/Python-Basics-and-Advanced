'''Python File Handling'''

# '''Opening a File'''
# # The open() function is used to open a file in Python
# file = open("students.txt", "r")

# print(file.read())
# # Close the file after reading
# file.close()

# with open("students.txt", "r") as file:
#     '''The with statement automatically closes the file after the block is executed'''    
#     # print(file.read())
#     # print(file.readlines())
#     # # The readlines() method reads all the lines in a file and returns them as a list
#     for f in file:
#         # The for loop iterates over each line in the file
#         print(f)


# '''Appending to a File'''
# # with open("students.txt", "a") as file:
# #     # The "a" mode opens the file for appending
# #     file.write("Paul, 75\n")

# # with open("students.txt", "r") as file:
# #     # The "r" mode opens the file for reading
# #     print(file.read())


'''File Overwriting'''
with open("overwrite_demo.txt", "w") as f:
    # The "w" mode opens the file for writing
    f.write("This is an overwriting test.\n")
    
with open("overwrite_demo.txt", "r") as f:

    print(f.read())
        