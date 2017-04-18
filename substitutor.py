import readin
#equations = readin.readin()

class Substitutor(object):
    def __init__(self):
        #lines = ['x=AVG(y,     z,w)','p=b*    g/4','   ANS  =  x/p    ']     #testing
        lines = readin.readin()
        #strip white space
        for i, equation in enumerate(lines):
            equation = equation.replace(" ", "")
            equation = equation.replace("\t", "")
            lines[i] = equation
        self.equations = lines
        self.finalEquation = self.getFinalEquation(self.equations)

    def getFinalEquation(self,equations):
        for substitutor in equations:
            for substitutee in equations:
                if substitutor != substitutee:
                    torTokens = substitutor.split('=')  # this splits the equation into two parts
                    teeTokens = substitutee.split('=')
                    # Example:
                    # VAR1=x+y+6
                    # tokens = ['VAR1','x+y+6]
                    if len(torTokens) != 2 or len(teeTokens) != 2:  # make sure it is not an empty Equation object ie eq=Equation("")
                        raise Exception("Invalid equation!")
                    substitutorVar = torTokens[0] #the var to be substituted
                    if substitutorVar != 'ANS': #don't want to be substituting in ANS
                        i=0
                        while i < len(teeTokens[1]):
                            c = teeTokens[1][i]
                            if c == substitutorVar:
                                temp = teeTokens[1][:i] + teeTokens[1][i + 1:]  # string without the variable
                                # print("temp = " + temp)
                                teeTokens[1] = temp[:i] + '(' + torTokens[1] + ')' + temp[i:]  # string with var substituted
                                i+= len(torTokens[1])+1  #advance i until after the subsitution
                            else:
                                i +=1      #no substitute found, increment i by 1
                        equations[equations.index(substitutee)] = teeTokens[0] + '=' + teeTokens[1] #replace equation in list with new substituted equation
        #print(equations)
        return equations[len(equations)-1]

