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

1. scan through variable declarations, store
2. Scan through equations that do not begin with "ANS"
     -parse out any keywords (ie AVG)
     -store all information
3. Scan equation that begins with ANS
    - scan each variable in ANS equation, substitute with other equations as necessary, add flags
4. Return final ANS equation and flags
5. Return all other equations and flags

"""

import copy


def preproc_main(input):
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

        # print("45454new ans str = " + new_answer_string)
        # print("Len eq list 1= " + str(len(equation_list)))
        return substitute(new_answer_string,temp_equation_list)  # call sub with new answer string until there are no more equations to substitute

    def other_equation(line,eq_list):
        eq = Equation(line)

        #check for flags in equation
        for flag in FLAGS:
            if flag in eq.expression:
                eq.flags.append(flag)

        eq_list.append(eq)
    ### END FUNCTIONS ###

    ### VARIABLE DECLARATIONS ###

    #POSSIBLE IDEA FOR FLAGS IN FUTURE (BY JOSH): User can add their own flags and definitions for flags
    FLAGS = ['AVG','SQUARE','SQRT', 'QUADRATIC','AREA', 'AREA_TRIANGLE']
    eq_list = []  # list of Equations including the ANS equation (marked by the isAns member of class Equation
    variable_dec = []  # list of variable declarations (might not need idk yet)
    const_dec = []  # list of constant declarations
    ans_string = ""  # final answer string after substitutions

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




        #possibly add in isVarDec


    # Equation Procesessing #
    for line in input:
            if line.startswith("CONST"): #test if line is a constant (not sure if needed, ask Dr. S)
                const_dec.append(line)
            if line.startswith("ANS"):  # test if line is answer equation
                answer_string = line
            other_equation(line, eq_list)  # call func to look for other equations, append to other_eq list

    # ANSWER PROCESSING #
    print ("---------Begin answer processing debug printing-----------")
    print("Printout of all equations parsed:\n--------")
    for item in eq_list:
        print(item)
        print("--------")



    substituted_answer_string = ""

    #Check if ans has any substitutions
    if len(eq_list) > 1:
        for item in eq_list:
            if item.isAns is True:
                answer_equation = copy.copy(item)
                ans_string = answer_equation.expression #storing answer equation expression
        substituted_answer_string = substitute(ans_string,eq_list)
        print("|||||||||||||||||||")
        print("Substituted answer string ==" + substituted_answer_string)
        print("|||||||||||||||||||")





#Don't know if necessary to separate out variable dec
#somehow need to figure out a way to determine if it is a variable dec vs equation, but a var dec is an equation


#possible idea: Since we assume all input is valid. the equations further down the eq_list can have variables from
#equations in the beginning of the eq_list. If not there, assume variable is on its own
#Example:
#x=y+7
#z=a+b
#ANS=z+k
#Look for variable dec that match "z"
#Found z=a+b
#ANS=(a+b)+k
#Look for variable dec that match "k"
#None found
#End




#ANS=(z*(x+y))/4


#other idea: preprocessor must minify all vars except for ANS. Will help with equation parser


#should we spend time on input validation (syntax checker etc) or is that not worth it - focus only on the actual problem


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
ANS = SQUARE(z,AREA(x,y))"""
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