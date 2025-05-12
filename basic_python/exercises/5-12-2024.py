my_tuple = (1, 2, 3, 4, 5)

my_list = list(my_tuple)
my_list.remove(3)
my_tuple = tuple(my_list)

print(my_tuple)


fruits = ('pineapple', 'avocado', 'banana', 'apple', 'avocado')

fruit_list = list(fruits)
fruit_list.append('Mango')
fruits = tuple(fruit_list)

print(fruits)


color = ('Red', 'Green', 'Blue', 'Yellow', 'Purple')

del color

print(color)
