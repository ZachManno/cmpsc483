"""""g = AVG(x,y,z)
ANS= AVG(g,b,p)

"g = x+y+z/3" , "**AVG**"
"(((x+y+z)/3),b,p)/3 " "**AVG**"

AVG(3,4,5)

(3+4+5/3 , **AVG**)

AVG((4*4),(5*5),(6/3))

(4*4)+(5*5)+(6/3) / 3 , AVG(x,y,z), AVG(g,b,p)

CONST x = 10
x=10
ANS = 3.3 * x


ANS = y * x


ANS = AVG(x,b,v)

"(y+z) = ( / 3" ""



AVG(4,6,z)



AVG(x,y,z)
AVG(x,y,z) ,

"x+y+z/3" , "**x=5**" , "**y=7**"

"main equation" "&& **AVG** ** x=5**  x number of flags, begins and ends with &&" "secondary equation"



ANS = 5+7
"5 + 7"

ANS = x + 5
"x + 5"

ANS = x + y
"x + y"

x=5
ANS = x+y
"5+y"


x=5
y=7
ANS = x+y
"5 + 7" "&& **x=5** **y=7** &&"

x=5
y=7
ANS = AVG(x,y,z)
"x+y+z/3" "&& **x=5** **y=7** &&"

x=5
y=7
z=x+y
ANS = AVG(x,y,z)
"x+y+(x+y)/3" "&& **x=5** **y=7** **AVG** &&" "z = x+y"



a = AVG(y,z)
b = AVG(x,y)
Ans = AVG(a, b)


ANS = AVG(a,b,c) + AVG(d,e,f)

ALGORITHM:

1. Scan through equations that do not begin with "ANS"
     -store each equation in a list
2. Scan equation that begins with ANS
    - scan each variable in ANS equation, substitute with other equations as necessary, add flags
3. Return final ANS equation and flags


INPUT REQUIREMENTS:
-All equation vars have lower case letters
-The final result must begin with the variable "ANS"
-Any equations that are unrelated to the "ANS" equation will be disregarded
-Any spaces and tabs are okay
-Variables should be 1 letter
-All macros are wrapped in brackets

VALID INPUT EXAMPLE:
"
    x=5+y
    z  = 6

    ANS = z * x
"
RESULT:
(6)*(5+y)

INVALID INPUT EXAMPLE:
"
    x=5+y
    z  = 6

    w = z * x
"
INVALID INPUT EXAMPLE:
"
    X=5+y
    Zeta  = 6

    white = Zeta * X
"

"""

import copy
import re

### CLASSES ###
class Equation:
        def __init__(self,value):
            self.value = value
            tokens = value.split('=')  # this splits the equation into two parts
            # Example:
            # VAR1=x+y+6
            # tokens = ['VAR1','x+y+6]
            if len(tokens) == 2: #make sure it is not an empty Equation object ie eq=Equation("")
                self.varName = tokens[0]
                self.expression = tokens[1] #part of equation after the equals sign
                self.flags = [] #flags such as AVG SQUARE etc
                if self.varName == "ANS":
                    self.isAns = True
                else:
                    self.isAns = False
            self.isVarDec = None #is a simple variable declaration such as x=5


        def __str__(self):
            return "Equation: " + self.value + '\n' + "varName: " + self.varName + '\n' + "expression: " + self.expression + '\n' + "Flags: " + ','.join(self.flags) + '\n' + "isAns: " + str(self.isAns)

### END CLASSES ###


def preproc_main(input):

    ### FUNCTIONS ###

    def substitute_helper(answer_string, i, equation_list):
        """
        Helper function for substitute
        :param answer_string:
        :param i:
        :param equation_list:
        :return: new answer string with substituted values
        """
        new_answer_string = ""
        # print("Answer string i = " + answer_string[i])
        for item in equation_list:
            if item.varName == answer_string[i]:  # found the variable to be substituted
                # print("Pre-slice: " + answer_string + "  , i = " + str(i) + " , answer[i]= " + answer_string[i])
                temp = answer_string[:i] + answer_string[i + 1:]  # answer string without the variable
                # print("temp = " + temp)
                new_answer_string = temp[:i] + '(' + item.expression + ')' + temp[i:]  # answer string with var substituted
                # print("NEW ANSWER STRING == " + new_answer_string)
                equation_list.remove(item)  # remove equation from temp list since it was already substituted
                return new_answer_string
        return answer_string

    def substitute(answer_string, equation_list):
        """
        Recursive function to substitute all given equations into one answer string
        :param answer_string:
        :param equation_list:
        :return: final answer string with all substitutions
        """
        # print("Len eq list = " + str(len(equation_list)))
        # print("TOP OF SUB FUNC, ANS STRING = " + answer_string)
        if len(equation_list) == 1:  # each time an equation is substituted, it will be deleted from the equation_list
            # print("A______S = " + answer_string)
            # print("type: " + str(type(answer_string)))
            return answer_string

        new_answer_string = answer_string
        # print("temp ans str = " + new_answer_string)
        temp_equation_list = list(equation_list)  # create temp list of equations bc we do not want to modify eq_list
        # output_line = line[:index] + 'Fu ' + line[index:] #haha

        for i, c in enumerate(answer_string):  # looking for equation variables
            if c.islower():  # equation variables can only be lower case letters, might have to change
                new_answer_string = substitute_helper(new_answer_string, i, temp_equation_list)  # substitute out variable
                    # print("new ans str[" + str(i) + "] = " + new_answer_string)

        # print("new ans str = " + new_answer_string)
        # print("Len eq list 1= " + str(len(equation_list)))
        return substitute(new_answer_string,temp_equation_list)  # call sub with new answer string until there are no more equations to substitute

    def other_equation(line,eq_list):
        eq = Equation(line)

        #check for flags in equation
        for flag in FLAGS:
            if flag in eq.expression:
                eq.flags.append(flag)

        eq_list.append(eq)


    #///////////// Macro Functions \\\\\\\\\\\\\\\\
    def macro_avg():
        print("AVG")
        return "SEEEVEN"

    def macro_square():
        return "SEEEVEN"

    def macro_sqrt():
        return "SEEEVEN"

    def macro_quadratic():
        return "SEEEVEN"

    def macro_area():
        return "SEEEVEN"

    def macro_area_triangle():
        return "SEEEVEN"

    macro_dispatcher = \
        {
            'AVG': macro_avg,
            'SQUARE': macro_square,
            'SQRT': macro_sqrt,
            'QUADRATIC': macro_quadratic,
            'AREA': macro_area,
            'AREA_TRIANGLE': macro_area_triangle,
        }
    # //////// End Macro Functions \\\\\\\\\\\\\\

    def macro_processing(flag,input_str,position):
        """

        :param flag: the flag to be processed
        :param input_str: the input string in which to process out the flag
        :param position: position in the string that the flag occurs
        :return: string with the flags processed out
        """
        print("Flag = " + flag + "\nInput = " + input_str + "\nPosition = " + str(position))
        #print("rest of string = " + input_str[position+len(flag):])



        return input_str[0:position] + macro_dispatcher[flag]() + input_str[position+len(flag):] #macro_dispatcher replaces the flag

    ### END FUNCTIONS ###

    ### VARIABLE DECLARATIONS ###

    #POSSIBLE IDEA FOR FLAGS IN FUTURE (BY JOSH): User can add their own flags and definitions for flags
    FLAGS = ['AVG','SQUARE','SQRT', 'QUADRATIC','AREA', 'AREA_TRIANGLE']
    eq_list = []  # list of Equations including the ANS equation (marked by the isAns member of class Equation)
    const_dec = []  # list of constant declarations

    ### END VARIABLE DECLARATIONS ###


    ### Stripping all white space, putting each line into a list ##
    print("----------------- Begin input string testing ------------------\n")
    print("Original input:\n\""+input+"\"")
    input = input.replace(" ", "")
    input = input.replace("\t", "")
    print("Input stripped:\n" + input)
    input = input.splitlines()
    print ("Input split:")
    print (input)
    print ("----------------- End input string testing ------------------\n")

    # Equation Procesessing #
    for line in input:
            # if line.startswith("CONST"): #test if line is a constant (not sure if needed, ask Dr. S)
            #    const_dec.append(line)
            other_equation(line, eq_list)  # call func to look for other equations, append to other_eq list

    # ANSWER PROCESSING #
    print("---------Begin answer processing debug printing-----------")
    print("Printout of all equations parsed:\n--------")
    for item in eq_list:
        print(item)
        print("--------")


    if len(eq_list) > 1:  # Check if ans has any substitutions
        for item in eq_list:
            if item.isAns is True:
                substituted_ans_string = substitute(item.expression, eq_list)  # substitute all equations in
        print("Substituted answer string ==" + substituted_ans_string)

    # PREPROCESSOR:  (decrypting any AVG, SQUARE, TRI etc)
    flagsExist = True
    while(flagsExist):
        flagsExist = False  # assume no flags exist, if one is found in the for loop below, reset back to true
        for flag in FLAGS:
            if flag in substituted_ans_string:
                substituted_ans_string =macro_processing(flag,substituted_ans_string,substituted_ans_string.find(flag))
                flagsExist = True



### TESTING ###
def run_tests(tests):
    for test in tests:
        preproc_main(test)
        print("====================================================")
        print("END TEST")
        print("====================================================")

### define test inputs ###
tests = [
"""x=5
        y=7
        z=x+y
ANS = z+9"""
,
"""x=6+g
   y=b*b
   z=x*y
ANS = z/4"""
,
"""x=5
        y=7
        z=AVG(x,y)
ANS = SQUARE(z,AREA(x,y))""",
"""x=2
    y=4
    z= 3
ANS = (x + y + z)/3"""
]


run_tests(tests)



#MISC:


#IS IT OKAY IF EQUATION VARIABLES CAN ONLY BE LOWER CASE LETTERS, OR SHOULD WE CONVERT THEM TO ALL LOWER CASE LETTERS FIRST

# RECURSIVE SUBSTITUTION ALGORITHM:
#  x=5
#  y=7
#  z=x+y
#  ANS=z+9

#        desired result:
#       ANS=(x+y)+9
#      ANS=((5)+y)+9
#     ANS =((5)+(7))+9

#    A_N_S_=_z_+_9
# z_+_9
# replace z with (x+y)

# ANS=(x+y)+9
# reevaluate
# same process for x

# ANS=((5)+y)+9
# reevaluate




def parse_nested(text, left=r'[(]', right=r'[)]', sep=r','):
    """ Based on http://stackoverflow.com/a/17141899/190597 (falsetru) """
    pat = r'({}|{}|{})'.format(left, right, sep)
    tokens = re.split(pat, text)
    stack = [[]]
    for x in tokens:
        if not x or re.match(sep, x): continue
        if re.match(left, x):
            stack[-1].append([])
            stack.append(stack[-1][-1])
        elif re.match(right, x):
            stack.pop()
            if not stack:
                raise ValueError('error: opening bracket is missing')
        else:
            stack[-1].append(x)
    if len(stack) > 1:
        print(stack)
        raise ValueError('error: closing bracket is missing')
    return stack.pop()


text = 'SQUARE((AVG((5),(7))),AREA(x,y+4))'
print("---------------------------")
print(parse_nested(text))
equations = parse_nested(text)
# def recursiveRef(li):
#     if len(idxList) > 1:
#         return recursiveRef(nested[idxList[0]], idxList[1:])
#     return nested[idxList[0]]




text = 'x+AVG(x,y+5,z)*SQUARE(x+y,z*f)'
print("---------------------------")
print(parse_nested(text))

text = 'x+AVG(x,y+5,z)*(x+y)'


test = 'x + AVG(w,y,z) * 5'

#"x + ((w+y+z)/3)*-b"
#"term + term * term"
#"        term:AVG,3 term:5 positivity:-1"
#   "class average with list of term classes"


print("---------------------------")
print(parse_nested(text))

text = 'p*AVG(x,AREA(y,z),AVG(a,b,c)) + j'
print("---------------------------")
print(parse_nested(text))


text = 'AVG(a,b,c) + AVG(x,y)'
print("---------------------------")
print(parse_nested(text))







