#SLICING STRING:
herald_info = "This is a short bio about Herald"
'''
Print from the first character (index 0) to the sixth character (index 5):
'''
print(herald_info[0:6])
'''
Print from first character (index 0) to fifth character (index 4):
'''
print(herald_info[:5])


#MODIFYING STRING:
'''
Modify All Characters to Upper Case:
'''
print(herald_info.upper())
'''
Modify The First Character of Each Word to Upper Case:
'''
print(herald_info.title())


#CLEARING WHITESPACE:
testing = '     This is a test  '
'''
Clears all whitespaces from the both ends of the string:
'''
print(testing.strip())
'''
Clears all whitespaces from the right end of the string:
'''
print(testing.rstrip())


#CONVERTS THE STRING TO A LIST TYPE:
testing2 = "This is a test"
'''
Converts the string above to a list
'''
splitted = testing2.split()
print(type(splitted)) # ==> EVIDENCE
print(len(splitted)) # ==> NUMBER OF ITEMS IN LIST


#STRING FORMATTING:
surname = 'Inyang'
first_name = 'Herald'
age = 15
'''
String Formatting (f string):
'''
full_info = f'{surname}, {first_name} is {age} years old'
print(full_info)