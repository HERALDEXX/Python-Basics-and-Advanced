def get_mood_rating():
    try:
        number = int(input("Rate your mood from 1 to 10: "))
        print(f"Thanks for sharing! Your rating is {number}.")
    except ValueError:
        print("Oops! That wasn't a valid number!")
        return get_mood_rating()
    if number < 1 or number > 10:
        print("Please enter a number between 1 and 10.")
        return get_mood_rating()
    
get_mood_rating()