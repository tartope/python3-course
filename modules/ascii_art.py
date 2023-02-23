# install and import pyfiglet package to do ascii art
import pyfiglet
# import colored from termcolor to get the terminal colors
from termcolor import colored

#print(pyfiglet) <-- gives you a long manuel
# print(help(pyfiglet.figlet_format))  <-- gives you the format for the function


# this function takes in msg and color inputs
def print_art(msg, color):
    # place all valid colors in a tuple
    valid_colors = ("black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "light_grey", "dark_grey", "light_red", "light_green", "light_yellow", "light_blue", "light_magenta", "light_cyan")
    
    # make a default color, if input color is not found in valid colors
    if color not in valid_colors:
        color = "magenta"
    
    # make ascii art of the msg
    ascii_art = pyfiglet.figlet_format(msg)
    # color the ascii art, and pass it the default colors
    colored_ascii = colored(ascii_art, color=color)

    print(colored_ascii)

msg = input("What would you like to print? ")
color = input("What color? ")
# print_art(msg, color)