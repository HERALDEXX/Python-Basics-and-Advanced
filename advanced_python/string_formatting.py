name = input('Enter your name: ')
age = int(input('Enter your age: '))
txt = f'   Hi my name is {name} and I am {age} years old.   '
print(txt.strip())  # Remove leading and trailing whitespace


username = input('Enter your username: ').title().strip()
print(f'Hi {username}, welcome to HERALDEXX Assistant!')
