'''
Text = str ==> "Herald", "Cat"
Numeric = int (4, 5, 2), float (2.1, 3.1), complex
Sequence Type = list [1, 2.5, "Herald"], tuple (1, "Inyang", 5.7), range
Mapping Type = dict {name: "Herald", age: 15, height: 1.65}
Set Types = set {1, 2, 3}, frozenset
Boolean Types: bool (True, False)
Binary: bytes, bytearray, memoryview
None Type = nonetype
'''

name = "Herald"
number = 1
num_2 = 4.5
random_value = "5"
student_details = {"name": "Herald", "age": 15, "height": 1.75}
num_3 = str(5)

print(type(name))
print(type(number))
print(type(num_2))
print(type(random_value))
print(type(student_details))
print(type(int("5")))
print(type(num_3))