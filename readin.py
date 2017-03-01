### test input from the command line instead of using tests written into the code

import sys
import getopt

def readin():
    ### save each line of input to a list of lines, output them when the next input is an empty line
    ### print all previous lines before prompting for next line
    ### in future: add delete feature?
    lines=[]
    doread(lines)
    print("Your code input:")
    i=0
    while i<len(lines):
        print(lines[i])
        i=i+1
    return lines

def doread(lines):
    next=input("Input next line of code (hit ENTER to finish)\n")
    if len(next)==0:
        return
    lines.append(next)
    i=0
    while i<len(lines):
        print(lines[i])
        i=i+1
    doread(lines)

readin()