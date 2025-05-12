import random
import time

def get_sad_response(name):
    responses = [
        f"I'm sorry you're feeling down, {name} 🫂. Would you like to hear a joke to cheer you up?",
        f"Hey {name}, remember that tough times don't last forever. Want to talk about it? ❤️",
        f"{name}, sending you a virtual hug! 🤗 How about we find something fun to do together?"
    ]
    return random.choice(responses)

def get_happy_response(name):
    responses = [
        f"That's wonderful {name}! Your happiness is contagious! 😊",
        f"Keep shining {name}! The world needs more positive energy like yours!",
        f"Amazing {name}! What's making you so happy today?"
    ]
    return random.choice(responses)

def get_stressed_response(name):
    responses = [
        f"Take a deep breath {name}. Let's do some relaxation exercises together.",
        f"{name}, stress is temporary. How about we take a 5-minute break?",
        f"Hey {name}, remember to be kind to yourself. Would you like some stress management tips?"
    ]
    return random.choice(responses)

def get_default_response(name):
    responses = [
        f"Thanks for sharing, {name}. How can I help make your day better?",
        f"I appreciate your honesty, {name}. I'm here to listen.",
        f"I understand, {name}. Would you like to talk more about it?"
    ]
    return random.choice(responses)

def typing_effect(text):
    """Creates a typing effect for more natural conversation"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def mood_checker():
    print("Welcome to HERALDEXX Assistant! 🤖✨")
    name = input("Hey there! What's your name? ")
    typing_effect(f"Nice to meet you, {name}! I'm HERALDEXX, your personal chat companion 😊")
    
    while True:
        mood = input("\nHow are you feeling today? (or type 'exit' to end) ").lower()
        
        if mood == 'exit':
            typing_effect(f"\nTake care of yourself, {name}! Remember, I'm here if you need someone to talk to! 👋 ❤️")
            break
            
        if "sad" in mood:
            response = get_sad_response(name)
        elif "happy" in mood:
            response = get_happy_response(name)
        elif "stressed" in mood:
            response = get_stressed_response(name)
        else:
            response = get_default_response(name)
            
        typing_effect(response)
        
        # Follow-up question
        if input("\nWould you like to tell me more about it? (yes/no) ").lower() == 'yes':
            typing_effect("I'm listening... 👂")
            user_story = input()
            typing_effect(f"Thank you for sharing that with me, {name}. Your feelings are valid. 💕")

if __name__ == "__main__":
    mood_checker()
