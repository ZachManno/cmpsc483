#https://abhirama.wordpress.com/2009/08/26/expression-tree/


operator_precedence = {
    '(': 0,
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

result = []

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.flags = []
        self.isans = False

class ExressionTree(object):

    def __init__(self, root=None):
        # Field values
        self.__root = root
        self.postorder_result = []
        self.preorder_result = []
        self.inorder_result = []
        self.node_list = []

    """
    Generate Order Trees
    """
    def generate_inorder(self):
        self.inorder_result = []
        self.__inorder_helper(self.__root)

    def generate_preorder(self):
        self.preorder_result = []
        self.__preorder_helper(self.__root)

    def generate_postorder(self):
        self.postorder_result = []
        self.__postorder_helper(self.__root)

    """
    Recursive Order helper functions
    """
    def __inorder_helper(self, node):
        self.node_list.append(node)
        if node:
            self.__inorder_helper(node.left)
            self.inorder_result.append(node.value)
            self.__inorder_helper(node.right)

    def __preorder_helper(self, node):
        self.node_list.append(node)
        if node:
            self.preorder_result.append(node.value)
            self.__preorder_helper(node.left)
            self.__preorder_helper(node.right)

    def __postorder_helper(self, node):
        if node:
            self.node_list.append(node)
            self.__postorder_helper(node.left)
            self.__postorder_helper(node.right)
            self.postorder_result.append(node.value)

    """
    Getters for Order Results
    """
    def get_postorder_result(self):
        if len(self.postorder_result) == 0:
            print("Gen!")
            self.generate_postorder()
        return self.postorder_result

    def get_preorder_result(self):
        if len(self.preorder_result) == 0:
            self.generate_preorder()
        return self.preorder_result

    def get_inorder_result(self):
        if len(self.inorder_result) == 0:
            self.generate_inorder()
        return self.inorder_result


class ExpressionTreeBuilder(object):
    def __init__(self):
        pass

    def create_expression_tree(self, infix):
        """
        Create an expression tree based on infix. Assign flags to potential areas of the tree.
        """


        infix = "".join(infix.split())
        postfix = self.postfix_convert(infix)

        stack = []

        for char in postfix:
            if char not in operator_precedence:
                node = Node(char)
                stack.append(node)
            else:
                node = Node(char)
                right = stack.pop()
                left = stack.pop()
                node.right = right
                node.left = left
                stack.append(node)

        # Declare root as answer
        root = stack.pop()
        root.isans = True
        exprtree = ExressionTree(root)

        # Base expression tree created. Identify potential answer structure.
        return exprtree

    def evaluate_AVG(self, exprtree):
        """
        Check for average strategy:
        - Iterate to each node and identify division.
            - If division, count number of nodes on left. If it it equals num on right, or num on right is letter,
            set flag and return.

        """
        if exprtree.__root.value == "/":
            # Possible AVG problem.
            expected = exprtree.__root.value.right.value
            if expected.isalpha():
                exprtree.__root.flags.append("AVG")
            elif expected.isdigit():
                # Confirm same count on left, otherwise it's not an average.
                valcount = self.avg_recurse(exprtree.__root)

                if valcount == expected:
                    # We have a match! This is an average.
                    exprtree.__root.flags.append("AVG")

    def avg_recurse(self, node):
        """
        Recursive helper for average. Traverses tree and counts nodes.
        """
        count = 0
        if node != None:
            if node.value.isdigit():
                count += 1

                count += self.avg_recurse(node.left)
                count += self.avg_recurse(node.right)

        return count

    def postfix_convert(self, infix):
        stack = []
        postfix = []

        # Append each char to stack / postfix in appropriate order.
        for char in infix:
            if char not in operator_precedence:
                postfix.append(char)
            else:
                if len(stack) == 0:
                    stack.append(char)
                else:
                    if char == "(":
                        stack.append(char)
                    elif char == ")":
                        while stack[len(stack) - 1] != "(":
                            postfix.append(stack.pop())
                        stack.pop()
                    elif operator_precedence[char] > operator_precedence[stack[len(stack) - 1]]:
                        stack.append(char)
                    else:
                        while len(stack) != 0:
                            if stack[len(stack) - 1] == '(':
                                break
                            postfix.append(stack.pop())
                        stack.append(char)

        # Transfer stack to postfix.
        while len(stack) != 0:
            val = stack.pop()
            print(val)
            postfix.append(val)
        print(postfix)
        return postfix


def run_tests():
    builder = ExpressionTreeBuilder()

    print("In Order:")
    builder.create_expression_tree("(A+B)*6").generate_inorder()

    print("Pre Order:")
    builder.create_expression_tree("(A+B)*6").generate_preorder()

    print("In Order:")
    builder.create_expression_tree("(A+B+C+D)/4").generate_inorder()

    print("Post Order:")
    exprtree = builder.create_expression_tree("(A+B+C+D)/(4)")
    exprtree.generate_postorder()

    print("Pre Order:")
    builder.create_expression_tree("(A+B+C+D)/4").generate_preorder()

    print("PostOrder Result:")
    print(exprtree.get_postorder_result())


def wells_tests():
    builder = ExpressionTreeBuilder()
    exprtree = builder.create_expression_tree("(5 + 4 + 3) / 3")
    print(exprtree.get_postorder_result())
    print(exprtree.get_preorder_result())
    print(exprtree.get_inorder_result())


class BTElement(object):
    def __init__(self, left, right, relation):
        self.left = left
        self.right = right
        self.relation = relation

class STGroup(object):
    def __init__(self, stelements):
        self.stelements = stelements

    def __str__(self):
        displaystr = ""
        for elem in self.stelements:
            displaystr += elem + " "

        return displaystr[:-1]

class STElement(object):
    def __init__(self, value, isnegative, isnumber):
        self.value = value
        self.isnegative = isnegative
        self.isnumber = isnumber

    def __str__(self):
        negmodifier = ""
        if self.isnegative:
            negmodifier = "-"

        return negmodifier + self.value


"""
Things to exploit:
FLAGS = ['AVG','SQUARE','SQRT', 'QUADRATIC','AREA', 'AREA_TRIANGLE']
Each piece needs to be identified.

AVG
(x + y) / 2

Square
Not average, two terms mul together?

Sort
??????

Area
Multiple terms multiplied together

Area triangle
Multiple terms multiplied together / 2


"""

wells_tests()