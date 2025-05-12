import json

'''Function to read a JSON file'''
with open('json_file.json', 'r') as file:
    loaded_data = json.load(file) #==> Load JSON data
    print(loaded_data)

    

'''Convert a dictionary to a JSON string'''
my_dict = {
    "student": "Herald",
    "age": 16,
    "gender": "Male",
    "course": "Advanced Python",
}  

print(my_dict)

converted_json = json.dumps(my_dict) #==> Conversion
print(converted_json)

print(type(my_dict)) #==> dictionary
print(type(converted_json)) #==> JSON string



'''JSON string formatting'''
# Indenting JSON string
indented_json = json.dumps(my_dict, indent=4)
print(indented_json)

# Separating JSON string
separator_json = json.dumps(my_dict, indent=4, separators=(',', ' == '))
print(separator_json)

# Sorting JSON string
sorted_json = json.dumps(my_dict, indent=4, sort_keys=True)
print(sorted_json)