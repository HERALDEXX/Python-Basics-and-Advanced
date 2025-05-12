import random

treasures = ['Diamonds', 'Rubies', 'Emeralds', 'Sapphires', 'Pearls']
coordinates = ('(13.4567° S, 69.1234° W)', '(22.9876° N, 93.7654° E)', '(4.3211° N, 74.5678° W)', '(18.6543° S, 129.8765° E)', '(25.9845° N, 56.5432° E)')

def find_treasures(treasures, coordinates):
    for i in range(len(treasures)):
        print(f'{treasures[i]} has a coordinate of {coordinates[i]}')

def simulate_treasure_hunt(treasures, coordinates): 
    chosen_treasure = random.choice(treasures) 
    chosen_index = treasures.index(chosen_treasure) 
    chosen_coordinate = coordinates[chosen_index]
    print(f'You found {chosen_treasure} at {chosen_coordinate}!')       

find_treasures(treasures, coordinates)

print("\n")

simulate_treasure_hunt(treasures, coordinates)
