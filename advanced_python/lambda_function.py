# lambda arguments : expression

x = lambda a : a + 10

print(x(5))

multiply_nums = lambda a, b : a * b

# print(multiply_nums(5, 6))

positive_check = lambda mood : "happy" in mood or "excited" in mood

user_mood = input("How do you feel? ").lower()
if positive_check(user_mood):
    print("That's great to hear!")
else:
    print("I hope your day gets better!")
