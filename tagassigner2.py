import sys
import main
import random

"""
New and improved!!!
"""

def is_sign(char):

        return char == '/' or char == '*' or char == '+' or char == '-'

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

def attributeequivalence(attr1, attr2):
    if attr1 == attr2:
        return True
    if attr1 == "+" and attr2 == "-" or attr1 == "-" and attr2 == "+":
        return True

    return False

def convertsign(attr):
    if attr == "-":
        return "+"

    return attr

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
                if isinstance(window[0], Term) and isinstance(window[1], str) and attributeequivalence(window[2], window[0].attribute):
                    term = Term([], window[1])
                    if window[2] == "-":
                        term.sign = "-"
                    window[0].terms.append(term)
                else:
                    parent = Term([t1, t2], convertsign(window[2]))
                    if window[2] == "-":
                        t2.sign = "-"


                postorder = postorder[:idx] + [parent] + postorder[idx + 3:]
            else:
                idx += 1

    return postorder[0]

easyequations = [
    # "1 + 2",
    # "a * b",
    # "a * b + c*d",
    # "a * (b + c) * d",
    # "1 + 2 + 3 + 4*5",
    # "a + b + c*b + d + e * g * h",
    # "a * b * c + 5 + c * b * a",
    # "-1-4",
    # "(1+2)/(3)",
    # "(1)/(2 + 3)",
    # "b * c + d * e * f",
    "RAND[150] * (b - f + g) * d"
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

def nextleveltests():
    builder = main.ExpressionTreeBuilder()

    for equation in easyequations:
        exprtree = builder.create_expression_tree(equation)
        postorder = exprtree.get_postorder_result()
        print(equation)
        print(str(postorder))
        formatequation = compileequation(equation)
        print(formatequation)
        print("===========")



# postorder_tests(
nextleveltests()
# print()
# print()
# run_tests()