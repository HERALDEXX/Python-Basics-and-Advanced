color = ('Red', 'Green', 'Blue')
(c_1, c_2, c_3) = color

print(c_1)
print(c_3)
print(c_2)


color = ('Red', 'Green', 'Blue', 'Yellow', 'Purple')
(c_first, c_2nd, *c_3rd) = color

print(c_first)
print(c_2nd)
print(c_3rd)