
### THIS IS THE OLD READIN FILE


### test input from the command line instead of using tests written into the code

import sys
import getopt


### get the options to only come up once all code has been input; until then, just read input code until first blank
### output should be a single string, each line separated by \n
### make it so user can put another line between existing lines

def readin_real():
    ### save each line of input to a list of lines, output them when the next input is an empty line
    ### print all previous lines before prompting for next line
    ansFlag = False
    lines = []

    intro = input("Enter the first line of code, or hit ENTER to quit:\n")
    if len(intro) == 0:
        return
    lines.append(intro)

    newline = 1;
    while newline > 0:
        next = input("Enter the next line of code followed by ENTER, or hit ENTER to finish:\n")
        newline = len(next)
        if len(next) != 0:
            lines.append(next)

    options(lines)

    print("Your code input:\n")
    i = 0
    while i < len(lines):
        print(str(i) + ".\t" + lines[i])
        i = i + 1
    for line in lines:
        if 'ANS' in line:
            ansFlag = True
    if not ansFlag:
        addedAnsLine = input("No \'ANS\' variable input, please add\n")
        lines.append(addedAnsLine)

    options(lines)
    print("Your code input:\n")
    i = 0
    while i < len(lines):
        print(str(i) + ".\t" + lines[i])
        i = i + 1

    return lines


def options(lines):
    next = input(
        "Choose from the following options to continue.\n" + "1.\t add a new line\n" + "2.\t modify a previous line\n"
        + "3.\t delete a line\n" + "4.\t finish input\n")
    if next == "1":
        doread(lines)
    elif next == "2":
        modify(lines)
    elif next == "3":
        delete(lines)
    elif next == "4":
        return
    else:
        print(next + " is not an option.")
    options(lines)


def doread(lines):
    next = input("Input next line of code:\n")

    tokens = next.split('=')  # this splits the equation into two parts
    # Example:
    # VAR1=x+y+6
    # tokens = ['VAR1','x+y+6]
    if len(tokens[0]>1):
        next = input('Variable names must be one letter. Enter line again')

    lines.append(next)
    i = 0
    while i < len(lines):
        print(lines[i])
        i = i + 1


def delete(lines):
    print("Enter the number of the line you want to delete.")
    i = 0
    while i < len(lines):
        print(str(i) + ".\t" + lines[i])
        i = i + 1
    print(str(i) + ".\tBACK TO OPTIONS")
    next = input("\n")

    if int(next) == i:
        return
    elif int(next) < len(lines):
        lines.remove(lines[int(next)])
        print("Line " + next + " successfully deleted.\n")
    else:
        print(next + " is not an option.\n")
        delete(lines)


def modify(lines):
    print("Enter the number of the line you want to modify.")
    i = 0
    while i < len(lines):
        print(str(i) + ".\t" + lines[i])
        i = i + 1
    print(str(i) + ".\tBACK TO OPTIONS")
    next = input("\n")

    x = 0
    while x < int(next):
        x = x + 1
    if x == i:
        return

    elif x < len(lines):
        mod = input("Re-enter line " + next + " as you see fit.\n")
        lines.remove(lines[x])
        if len(mod) != 0:
            lines.insert(x, mod)

        else:
            print("Line " + next + " deleted.\n")
        return
    else:
        print(next + " is not an option.\n")
        modify(lines)


