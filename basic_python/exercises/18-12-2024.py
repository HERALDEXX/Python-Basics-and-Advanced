import random
import time
from colorama import Fore, Style, init

init(autoreset=True)

def christmas_tree(height):
    for i in range(1, height + 1):
        space = ' ' * (height - i)
        stars = '*' * (2 * i - 1)
        # Add random decorations
        decorated_stars = ''.join(random.choice([Fore.RED + '*', Fore.YELLOW + 'o', Fore.GREEN + '*']) for _ in stars)
        print(space + decorated_stars)
        time.sleep(0.5)
    print(' ' * (height - 1) + '|')

height = int(input("Enter the height of the Christmas tree: "))
christmas_tree(height)
