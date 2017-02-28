### test input from the command line instead of using tests written into the code

import sys
import getopt

print(sys.argv)
def readin():
    ### save each line of input to a list of lines, output them when the next input is an empty line
    ### print all previous lines before prompting for next line
    ### in future: add delete feature?
    lines=[]
    next=input("Input next line of code (hit ENTER to finish)\n")
    lines.append(next)
    print(lines)



readin()