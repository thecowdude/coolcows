'''
Before you run this for first time only
1. Open a command prompt
2. Install the coloroma module by typing
   > pip install colorama

Avaialble options
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
'''
# Import required modules
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style

# Test out the different colours!
print(Fore.RED + "This is RED Text")
print(Fore.GREEN + "This is GREEN Text")
print(Fore.BLUE + "This is BLUE Text")

# Change the background colour!
print(Back.GREEN + 'Green background')

# Now how about changing both foreground and background colours!
print(Back.GREEN + Fore.RED + 'Green background and RED Text')

# Dim the text!
print(Style.DIM + 'Dimmed Text')

# Reset things back to normal
# print(Style.RESET_ALL)

print('...back to normal now')
