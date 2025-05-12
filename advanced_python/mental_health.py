def mood_checker():
    name = input("Hey there, What is your name? ")
    mood = input("How are you feeling today? ").lower()

    if "sad" in mood:
        print(f"Oh {name}, I'm sorry to hear that. Do you wanna hear a joke?")
    elif "happy" in mood:
        print(f"That's cool {name}. Keep spreading the joy! 😊")
    elif "stressed" in mood:
        print(f"Take a deep breath {name}. I'm here to help you relax.\nYou might need some rest later.\nWant to try some breathing exercises for now?")
    else:
        print(f"Thanks for sharing {name}. I'm here if you need anything!")

mood_checker()