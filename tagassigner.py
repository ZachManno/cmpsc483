import sys
import main

class EquationConstructor(object):

    def __init__(self, equation):
        self.originalequation = equation
        self.terms = []

        # Initial split into terms.
        strterms = self.additiontermsplit(equation)

        # Convert each strterm to a term object, save to formatted equation.

        for strterm in strterms:
            # Create postorder for term, and build term object.
            builder = main.ExpressionTreeBuilder()

            # Remove math from front of term
            tempterm = strterm
            if tempterm[0] == '+' or tempterm[0] == '-':
                tempterm = tempterm[1:]

            postorder = builder.create_expression_tree(tempterm).get_postorder_result()
            self.terms.append(Term(strterm, postorder[:len(postorder)-1], postorder[len(postorder)-1]))


    def additiontermsplit(self, input):
        curridx = 0
        terms = []
        parencount = 0
        for idx in range(len(input)):
            # Identify parenthesis
            if input[idx] == '(':
                parencount += 1
            if input[idx] == ')':
                parencount -= 1


            if parencount==0 and (input[idx] == '+' or input[idx] == '-'):
                terms.append("".join(input[curridx:idx].split()) )
                curridx = idx
        terms.append(input[curridx:])
        return terms


class Term(object):
    def __init__(self, valueinput, postorder, attribute):
        """
        Construct a term, with a stored sign, accepts chars and ints
        """
        self.originalvalue = valueinput
        self.postorder = postorder
        self.attribute = attribute
        self.terms = []

        # Determine if an "attribute" is a char or a num.
        if attribute.isalpha() or attribute.isdigit():
            stripvalue = "".join(attribute.split())

            # Determine Sign
            if stripvalue[0] == "-" or stripvalue[0] == "+":
                self.sign = stripvalue[0]
                self.value = stripvalue[1:]
            else:
                self.sign = "+"
                self.value = stripvalue

            if len(self.value) != 1:
                raise SystemError("Error! " + valueinput + " not valid input!")
        elif attribute == '*' or attribute == '/':
            # Multiplication / Division Term. Break apart using postorder result.
            oppositeattribute = "/"
            if attribute == "/":
                oppositeattribute = "*"

            postorderidx = len(postorder) - 1
            if attribute == '*' or attribute == '/':
                for postorderval in reversed(postorder):
                    if postorderval == attribute:
                        postorderidx -= 1
                        continue

                    self.terms.append(Term("", postorder[:postorderidx], postorder[postorderidx]))

                    if postorderval == oppositeattribute:
                        break
                    postorderidx -= 1

                self.sign = "+"
            else:
                sys.exit("Invalid attribute!")

    def __str__(self):
        strrep = ""
        if len(self.terms) > 0:
            for term in self.terms:
                strrep += str(term)
                strrep += self.attribute
            strrep = strrep[:len(strrep) - 1]
        else:
            strrep = "(" + str(self.sign) + str(self.value) + ")"

        return strrep

equations = ["5x+20", "ax - 5b + c + d + 2005 + 20b", "5 + (1+2+3)/3 - (4+5+6)/(1+2+3)"]
easyequations = [
    "1 + 2",
    "1 + 3 -c + 5",
    "6 * b",
    "a + b + c*b + d + e * g * h",
    "a * b * c + 5 + c * b * a",
    "c * b / a"
]

for equation in easyequations:
    formatequation = EquationConstructor(equation)
    print("------")
    print(equation)
    for term in formatequation.terms:
        print(term)



