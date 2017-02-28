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
    - scan each variable in ANS equation, subsitute with other equations as necessary, add flags
4. Return final ANS equation and flags
5. Return all other equations and flags

"""

#Should maybe have an "equation" class. One equation with list of flags/information for each equation

def preproc_main(input):
    class Equation:
        def __init__(self,value):
            self.value = value
            tokens = value.split('=')  # this splits the equation into two parts
            # Example:
            # VAR1=x+y+6
            # tokens = ['VAR1','x+y+6]
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

    ### Variable declarations ###

    FLAGS = ['AVG','SQUARE','SQRT', 'QUADRATIC','AREA', 'AREA_TRIANGLE']
    eq_list = []  # list of Equations including the ANS equation (marked by the isAns member of class Equation
    variable_dec = []  # list of variable declarations (might not need idk yet)
    const_dec = []  # list of constant declarations
    answer = ""  # final answer string after substitutions

    ### End Variable Declarations ###

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

    def other_equation(line,eq_list):
        """
        :param input,eq_list:
        :return:
        parse out any keywords, return equation and keyword flags
        """
        eq = Equation(line)

        #check for flags in equation
        for flag in FLAGS:
            if flag in eq.expression:
                eq.flags.append(flag)

        eq_list.append(eq)

        #possibly add in isVarDec



    for line in input:
            if line.startswith("CONST"): #test if line is a constant
                const_dec.append(line)
            if line.startswith("ANS"):  # test if line is answer equation
                answer = line
            other_equation(line, eq_list)  # call func to look for other equations, append to other_eq list



    ### ANSWER PROCESSING ###
    print ("---------Begin answer processing debug printing-----------")

    print("Printout of all equations parsed:\n--------")
    for item in eq_list:
        print(item)
        print("--------")


#Don't know if necessary to separate out variable dec
#def var_dec(input, variable_dec):
 #   """
  #  :param input:
   # append to variable dec if it is a variable dec
    #somehow need to figure out a way to determine if it is a variable dec vs equation, but a var dec is an equation
    #"""
#











### TESTING ###
def run_tests(tests):
    for test in tests:
        preproc_main(test)

### define test inputs ###
tests = [
"""x=5
        y=7
ANS = x+y"""
,
"""x=5
        y=7
        z=AVG(x,y)
ANS = SQUARE(z,AREA(x,y))"""
]

run_tests(tests)
