import sys
import main
import random

def parenthesize_postorder_equation(postorder):
    representation = [")"]
    sincelastsign = -1
    for postorderval in reversed(postorder):
        if sincelastsign == 0 and is_sign(postorderval):
            representation.append(")")
            representation.append(postorderval)
            sincelastsign = 0

    return representation



def is_sign(char):
        return char == '/' or char == '*' or char == '+' or char == '-'


class Equation(object):

    def __init__(self, equation):
        """
        Generate a list of terms in self.terms that represents the equation split by addition/subtraction.
        :param equation: String representation of an equation. Can contain macros.
        """

        self.originalequation = equation
        self.tag = "ANS"
        terms = []

        # Convert each term, split by addition, to a term object, save to formatted equation.
        strterms = self.additiontermsplit(equation)
        for strterm in strterms:
            builder = main.ExpressionTreeBuilder()
            oldsign = tempterm[0]
            tempterm = tempterm[1:]
            postorder = builder.create_expression_tree(tempterm).get_postorder_result()

            # Add back old sign.
            if oldsign != "":
                postorder[0] = oldsign + postorder[0]

            # Save term to list.
            terms.append(Term(strterm, postorder[:len(postorder)-1], postorder[len(postorder)-1]))

        # Save terms as term object.
        if len(terms) > 1:
            self.terms = [Term(terms, "+")]
        else:
            self.terms = [Term(terms, terms[0].attribute)]


class Term(object):
    def __init__giventerms(self, terms, attribute):
        self.terms = terms
        self.attribute = attribute
        self.tag = None
        self.sign = "+"  # Todo this has to be fixed.
        self.identify_and_deconstruct_macro(attribute)

    def __init__(self, valueinput, postorder, attribute=None):
        """
        Construct a term, with a stored sign.
        Terms may have a tag, which better describes the term in the context of the problem.

        :param valueinput: String representation of an equation. Can contain macros. (TODO: OUTDATED)
        :param postorder: post order representation of an equation.
        :param attribute: Representation of "Value" of a term. * or / for mul and div, variable or integer for base
        value.
        """

        if attribute is None:
            self.__init__giventerms(valueinput, postorder)
        else:
            self.originalvalue = valueinput
            self.postorder = postorder
            self.attribute = attribute
            self.terms = []
            self.tag = None
            self.identify_and_deconstruct_macro(attribute)


    def identify_and_deconstruct_macro(self, attribute):
        """
        Check to see if the given attribute contains a macro.
        :param attribute:
        :return:
        """

        if len(attribute) > 1 and self.is_sign(attribute[0]):
            attribute = attribute[1:]

        macrocheck = attribute.find('[')
        if macrocheck > -1:

            # Term is a macro.
            self.tag = attribute[:macrocheck]

            # Evaluate Macro.
            endmacro = attribute.rfind(']')
            if endmacro == -1:
                raise SystemError("Non matching bracket in term " + attribute + " found!")
            self.attribute = attribute[macrocheck + 1:endmacro]

            # Obtain the individual pieces of the macro in a list.
            parencount = 0
            previdx = 0
            pieces = []
            for idx in range(len(self.attribute)):
                if self.attribute[idx] == ',' and parencount == 0:
                    pieces.append(self.attribute[previdx:idx])
                    previdx = idx + 1
                if self.attribute[idx] == '(' or self.attribute[idx] == '[':
                    parencount += 1
                if self.attribute[idx] == ')' or self.attribute[idx] == ']':
                    parencount -= 1
            pieces.append(self.attribute[previdx:])
            strrep = "("

            # Format macro based on TAG type.
            if self.tag == "AVG":
                for x in pieces:
                    strrep += x + "+"
                strrep = strrep[:len(strrep) - 1] + ')'
                strrep += "/"
                strrep += str(len(pieces))
            elif self.tag == "SQR":
                if len(pieces) > 1:
                    raise SystemError("Invalid input for SQR macro. Expected only 1 term, got " + str(len(pieces)))
                strrep = pieces[0] + "*" + pieces[0]
            elif self.tag == "RAND":
                if len(pieces) > 1:
                    raise  SystemError("Invalid input for RAND macro. Expected 1 term, got" + str(len(pieces)))
                strrep = str(random.randrange(int(pieces[0])))

            builder = main.ExpressionTreeBuilder()
            postorder = builder.create_expression_tree(strrep).get_postorder_result()

            self.postorder = postorder[:len(postorder)-1]
            self.attribute = postorder[len(postorder)-1]

    def is_sign(self, char):
        return char == '/' or char == '*' or char == '+' or char == '-'

    def __str__(self):
        # Generate string representation of term.
        strrep = ""
        addconnector = False

        if len(self.terms) > 0:
            if self.attribute == "+" or self.attribute == "-":
                strrep += "("
                addconnector = True
            for term in self.terms:
                if addconnector and term.sign == "+":
                    strrep += term.sign

                strrep += str(term)

                if not addconnector:
                    strrep += self.attribute

            if self.attribute == "+" or self.attribute == "-":
                strrep += ")"
            else:
                strrep = strrep[:len(strrep) - 1]

        else:
            # Printing an individual variable or number.
            sign = ""
            possibleattributes = ["+", "-", "*", "/"]
            if self.sign == "-":
                sign = "-"

            # if self.attribute not in possibleattributes:
            strrep = sign + str(self.attribute)

        return strrep


def compileequation(equation):
    builder = main.ExpressionTreeBuilder()
    exprtree = builder.create_expression_tree(equation)
    postorder = exprtree.get_postorder_result()
    while len(postorder) > 1:
        # Compile down postorder into terms. Establish relationships based on "Wells Master Algorithm"
        idx = 0
        while idx < len(postorder) - 1:
            # Collect 3 terms based on the window
            window = postorder[idx:idx+3]
            readytocombine = True

            # Can the window be combined into a subproblem?
            for entry in window[:2]:
                if is_sign(entry):
                    readytocombine = False
            readytocombine = readytocombine and is_sign(window[2])

            if readytocombine:
                # Creating relation with two children.
                t1 = window[0]
                if not isinstance(window[0], Term):
                    t1 = Term([], window[0])

                t2 = window[1]
                if not isinstance(window[1], Term):
                    t2 = Term([], window[1])

                # One special case: if window[0] a term, window[1] not a term, window[2] same attr as window[0]: Combine
                if isinstance(window[0], Term) and isinstance(window[1], str) and window[2] == window[0].attribute:
                    window[0].terms.append(Term([], window[1]))
                else:
                    parent = Term([t1, t2], window[2])
                postorder = postorder[:idx] + [parent] + postorder[idx + 3:]

            idx += 1

    return postorder[0]

easyequations = [
    "1 + 2",
    "1 + 3 + c + 5",
    "a * b",
    "a * b + c*d",
    "a * (b + c) * d",
    "1 + 2 + 3 + 4*5",
    # "a + b + c*b + d + e * g * h",
    # "a * b * c + 5 + c * b * a",
    # "-1-4",
    "(1+2)/(3)",
    "(1)/(2 + 3)",
    # "AVG[1,AVG[1,2,3],3]",
    # "AVG[1,9,90,40,50] + AVG[1,9,90,40,50]",
    # "SQR[10]",
    # "SQR[RAND[10]]",
    # "RAND[100] * RAND[50] + AVG[RAND[20], RAND[20], RAND[20]]",
    # "1 * (2/3)",
    # "1 * 2 / 3",
    # "1 * 2 * 3",
    # "1 * 2 * 3/4 * 5",
    # "1 * 2 * (3/4) * 5"
]

def run_tests():
    """
    Run a series of tests to confirm valid token parsing from input.
    """

    equations = [
        "5x+20",
        "ax - 5b + c + d + 2005 + 20b",
        "5 + (1+2+3)/3 - (4+5+6)/(1+2+3)"
    ]

    for equation in easyequations:
        formatequation = Equation(equation)
        print("------")
        print(equation)

        equation = ""

        for term in formatequation.terms:
            equation += str(term) + " "

        print(equation)

def postorder_tests():
    builder = main.ExpressionTreeBuilder()

    for equation in easyequations:
        exprtree = builder.create_expression_tree(equation)
        print(equation)
        postorder = str(exprtree.get_postorder_result())
        print(postorder)
        print(parenthesize_postorder_equation(postorder))
        print("===========")

def nextleveltests():
    builder = main.ExpressionTreeBuilder()

    for equation in easyequations:
        exprtree = builder.create_expression_tree(equation)
        postorder = exprtree.get_postorder_result()
        print(equation)
        print(str(postorder))
        formatequation = compileequation(postorder)
        print(formatequation)
        print("===========")



# postorder_tests(
# nextleveltests()
# print()
# print()
# run_tests()