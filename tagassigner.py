import sys
import main


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

            # Remove math from front of term temporarily (necessary workaround for postorder).
            tempterm = strterm
            oldsign = ""
            if tempterm[0] == '+' or tempterm[0] == '-':
                oldsign = tempterm[0]
                tempterm = tempterm[1:]
            postorder = builder.create_expression_tree(tempterm).get_postorder_result()

            # Add back old sign.
            if oldsign != "":
                postorder[0] = oldsign + postorder[0]

            # Save term to list.
            terms.append(Term(strterm, postorder[:len(postorder)-1], postorder[len(postorder)-1]))

        # Save terms list as official term object split by addition.
        self.terms = [Term(terms, "+")]

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
                if curridx != idx:
                    terms.append("".join(input[curridx:idx].split()))
                    curridx = idx

        # Append ending term
        terms.append(input[curridx:])
        return terms


class Term(object):
    def __init__giventerms(self, terms, attribute):
        self.terms = terms
        self.attribute = attribute

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
            self.determine_macro(attribute)

            """
            A term consists of several sub terms, as well as an 'attribute' which describes
            the relationship of all subterms.

            EX: "*" attribute means all values are multiplied together.

            An attribute will be a number or a char, if the term is simply a variable/number.

            Terms may also have a "tag" which further describes the relationship, such as "AVG", "SQ",
            etc.

            To construct the term object

            """
            # Attempt to determine if value is digit
            is_dig = True
            try:
                int (self.attribute)
            except:
                is_dig = False

            # Determine if an "attribute" is a char or a num.
            if self.attribute[len(self.attribute) - 1].isalpha() or is_dig:
                # The term is not a relation. It is a variable or digit, the simplest form of a term.

                # Determine Sign
                stripvalue = "".join(self.attribute.split())
                if stripvalue[0] == "-" or stripvalue[0] == "+":
                    self.sign = stripvalue[0]
                    self.attribute = stripvalue[1:]
                else:
                    self.sign = "+"
                    self.attribute = stripvalue

                # Assert valid input
                if not is_dig and len(self.attribute) != 1:
                    raise SystemError("Error! " + valueinput + " not valid input!")

            elif self.attribute == '*' or self.attribute == '/':
                # Multiplication / Division relation. Break apart using postorder result.

                # Determine cancelling opposite attribute.
                oppositeattribute = "/"
                if self.attribute == "/":
                    oppositeattribute = "*"

                # Iterate through result, createing subterms.
                postorderidx = len(postorder) - 1
                for postorderval in reversed(self.postorder):
                    if postorderval == self.attribute:
                        postorderidx -= 1
                        continue

                    # Create subterm.
                    self.terms.insert(0, Term("", self.postorder[:postorderidx], self.postorder[postorderidx]))

                    # Check if new relation type is detected.
                    if postorderval != self.attribute and self.is_sign(postorderval):
                        break

                    postorderidx -= 1

                self.sign = "+"

            elif self.attribute == '+':
                postorderidx = len(postorder) - 1

                for postorderval in reversed(self.postorder):
                    if self.attribute == postorderval:
                        postorderidx -= 1
                        continue

                    self.terms.insert(0, (Term("", "", self.postorder[postorderidx])))

                    if postorderval == '*' or postorderval == '/':
                        break
                    else:
                        postorderidx -= 1
                self.sign = "+"

            else:
                raise SystemError("Invalid attribute '" + attribute + "' provided!")

    def determine_macro(self, attribute):
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
                strrep= strrep[:len(strrep) - 1] + ')'
                strrep += "/"
                strrep += str(len(pieces))

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
        "1 + 3 - c - 1* 5",
        "a * b",
        "a * b + a*c",
        "a + b + c*b + d + e * g * h",
        "a * b * c + 5 + c * b * a",
        "-1-4",
        "(1+2)/(3)",
        "(1)/(2 + 3)",
        "AVG[1,AVG[1,2,3],3]",
        "AVG[1,9,90,40,50] + AVG[1,9,90,40,50]"
    ]

    for equation in easyequations:
        formatequation = Equation(equation)
        print("------")
        print(equation)

        equation = ""

        for term in formatequation.terms:
            equation += str(term) + " "

        print(equation)

run_tests()
