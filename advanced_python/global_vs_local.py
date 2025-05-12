global_mood = "happy"

def change_mood():
    local_mood = "sad"
    print("Inside function:", local_mood)
    print("Outside function:", global_mood)

change_mood()