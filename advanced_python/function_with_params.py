def mood_checker(mood):
    if "sad" in mood:
        return "Oh, I'm sorry to hear that. Do you wanna hear a joke?"
    elif "happy" in mood:
        return "That's cool. Keep spreading the joy! 😊"
    else:
        return "Thanks for sharing. I'm here if you need anything!"
    
user_mood = input("How are you feeling today? ").lower()

print(mood_checker(user_mood))