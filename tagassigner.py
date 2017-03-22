import sys
import main


class Equation(object):

    def __init__(self, equation):
        """
        Generate a list of terms in self.terms that represents the equation split by addition/subtraction.

        :param equation: String representation of an equation. Can contain macros.
        """

        self.originalequation = equation
        self.terms = []

        # Initial split into terms.
        strterms = self.additiontermsplit(equation)

        # Convert each strterm to a term object, save to formatted equation.
        for strterm in strterms:
            # Create postorder for term, and build term object.
            builder = main.ExpressionTreeBuilder()

            # Remove math from front of term temporarily.
            tempterm = strterm
            if tempterm[0] == '+' or tempterm[0] == '-':
                tempterm = tempterm[1:]

            postorder = builder.create_expression_tree(tempterm).get_postorder_result()
            self.terms.append(Term(strterm, postorder[:len(postorder)-1], postorder[len(postorder)-1]))

    def additiontermsplit(self, input):
        # Split the input into terms, based on addition and subtraction
        curridx = 0
        terms = []
        parencount = 0

        # Append to terms, counting parenthesis as 1 term.
        for idx in range(len(input)):
            # Identify parenthesis
            if input[idx] == '(':
                parencount += 1
            if input[idx] == ')':
                parencount -= 1
            if parencount == 0 and (input[idx] == '+' or input[idx] == '-'):
                terms.append("".join(input[curridx:idx].split()))
                curridx = idx

        # Append ending term
        terms.append(input[curridx:])
        return terms


class Term(object):
    def __init__(self, valueinput, postorder, attribute):
        """
        Construct a term, with a stored sign.
        Terms may have a tag, which better describes the term in the context of the problem.

        :param valueinput: String representation of an equation. Can contain macros. (TODO: OUTDATED)
        :param postorder: post order representation of an equation.
        :param attribute: Representation of "Value" of a term. * or / for mul and div, variable or integer for base
        value.
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
                self.attribute = stripvalue[1:]
            else:
                self.sign = "+"
                self.attribute = stripvalue

            if len(self.attribute) != 1:
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
        else:
            raise SystemError("Invalid attribute " + attribute + " provided!")

    def __str__(self):
        # Generate string representation of term.
        strrep = ""
        if len(self.terms) > 0:
            for term in self.terms:
                strrep += str(term)
                strrep += self.attribute
            strrep = strrep[:len(strrep) - 1]
        else:
            strrep = "(" + str(self.sign) + str(self.attribute) + ")"

        return strrep


def run_tests():
    """
    Run a series of tests to confirm valid token parsing from input.
    """

    equations = [
        "5x+20",
        "ax - 5b + c + d + 2005 + 20b",
        "5 + (1+2+3)/3 - (4+5+6)/(1+2+3)"
    ]

    easyequations = [
        "1 + 2",
        "1 + 3 -c + 5",
        "6 * b",
        "a + b + c*b + d + e * g * h",
        "a * b * c + 5 + c * b * a",
        "c * b / a"
    ]

    for equation in easyequations:
        formatequation = Equation(equation)
        print("------")
        print(equation)
        for term in formatequation.terms:
            print(term)

run_tests()