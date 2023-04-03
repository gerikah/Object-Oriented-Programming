# Alday, Gerikah L.             BSCPE 1-5
# Object Oriented Programming
# CMPE-103 LAB EXERCISE No. 1 : Problem 3

import pyfiglet
border = "-" * 184
title = ("\n\n" + border + "\n\n" + "\033[95m" + pyfiglet.figlet_format("Decryption\n", justify = "center", font = "isometric1", width = 175) + "\n")
print(title)

# input from user
print(border + "\033[95m" + pyfiglet.figlet_format("\nEnter a string to decrypt", justify = "center", font = "cybermedium", width = 175))
input_string = input("".center(68))
output_string = ""
# check each character
for i in range(len(input_string)):
    # if * , change to a
    if input_string[i] == "*":
        output_string += "a"
# if & , change to e
    elif input_string[i] == "&":
        output_string += "e"
# if # , change to i
    elif input_string[i] == "#":
        output_string += "i"
# if + , change to o
    elif input_string[i] == "+":
        output_string += "o"
# if ! , change to u
    elif input_string[i] == "!":
        output_string += "u"
    else:
        output_string += input_string[i]
# print output
print(border + "\033[95m" + pyfiglet.figlet_format("\nDecrypted string", justify = "center", font = "cybermedium", width = 175))
print(("\033[7m" + "\n\n\n" + border + output_string.center(180) + border + "\n\n\n" ))
