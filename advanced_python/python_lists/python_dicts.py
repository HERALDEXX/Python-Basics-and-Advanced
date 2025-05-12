my_dict = {
    "name": "Herald",
    "age": 15,
    "gender": "M",    
    "height": 1.75,
    "courses": ['Innovator starter', 'Python Basic', 'Python Advanced'],
    "International": True
}

# print(my_dict)
# print(len(my_dict))  # Length of the dictionary
# print(type(my_dict))  # Type of data structure

# '''Dictionary Constructors'''
# my_dict_2 = dict(name = "Paul", 
#                  age = 20, 
#                  gender = "M", 
#                  height = 1.80)
# print(my_dict_2)

# '''Accessing Specific Dictionary Values'''
# name = my_dict.get("name")
# print(name)

# '''Accessing All Dictionary Keys'''
# print(my_dict.keys())

# '''Accessing All Dictionary Values'''
# print(my_dict.values())

# '''Adding New Key-Value Pairs'''
# my_dict["weight"] = 70
# print(my_dict)

# '''Verifying Key Existence'''
# if "state" in my_dict:
#     print("Key exists")
# else:
#     print("Key does not exist")

'''Updating Key-Value Pairs'''
my_dict["age"] = 16
print(my_dict)    