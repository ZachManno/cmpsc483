import sys

class Term(object):
    def __init__(self, valueinput):
        """
        Construct a term, with a stored sign, accepts chars and ints
        """

        try:
            # Attempt to parse integer from value
            value = int(valueinput)
            self.value = abs(value)

            # Determine Sign
            if value < 0:
                self.sign = "-"
            else:
                self.sign = "+"

        except ValueError:
            # Parse variable chars from value
            stripvalue = "".join(valueinput.split())

            # Determine Sign
            if stripvalue[0] == "-" or stripvalue[0] == "+":
                self.sign = stripvalue[0]
                self.value = stripvalue[1:]
            else:
                self.sign = "+"
                self.value = stripvalue

    def __str__(self):
        return self.sign + str(self.value)

class Division (object):
    def __init__(self, terms):
        self.terms = terms
        self.sign = "/"

    def addTerms(self, terms):
        [self.terms.append(term) for term in terms]

class Multiplication(object):
    def __init__(self, terms):
        self.terms=terms
        self.sign = "*"

    def addTerms(self, terms):
        [self.terms.append(term) for term in terms]


tests = ["-5", "15", "270", "-b", "-57c"]

for test in tests:
    print(str(Term(test)) + " " + test)


equations = ["5x+20"]
for equation in equations:
    equation = "".join(equation.split())



