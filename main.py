#https://abhirama.wordpress.com/2009/08/26/expression-tree/

operator_precedence = {
    '(': 0,
    ')': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

# Term for each num and sign
result = []

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.flags = []
        self.isans = False


class ExpressionTree(object):

    def __init__(self, root=None):
        # Field values
        self.root = root
        self.postorder_result = []
        self.preorder_result = []
        self.inorder_result = []

        self.node_list = []

    """
    Generate Order Trees
    """
    def generate_inorder(self):
        self.inorder_result = []
        self.__inorder_helper(self.root)

    def generate_preorder(self):
        self.preorder_result = []
        self.__preorder_helper(self.root)

    def generate_postorder(self):
        self.postorder_result = []
        self.__postorder_helper(self.root)

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
        stack = []

        postfix = self.postfix_convert(infix)

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
        exprtree = ExpressionTree(root)

        # Return evaluated expression tree.
        return exprtree

    def postfix_convert(self, infix):
        stack = []
        postfix = []
        previdx = 0
        idx = 0

        # Append each char to stack / postfix in appropriate order.
        for char in infix:
            if char in operator_precedence:
                prevcontent = infix[previdx: idx]
                if len(prevcontent) > 0:
                    postfix.append(prevcontent)
                previdx = idx + 1

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
            idx += 1

        prevcontent = infix[previdx: idx]
        if len(prevcontent) > 0:
            postfix.append(prevcontent)

        # Transfer stack to postfix.
        while len(stack) != 0:
            val = stack.pop()
            postfix.append(val)
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
    equations = [
                "5*x+2", "a * x - 5 * b + c + d + 2 * b",
                 "5 + (1+2+3)/3 - (4+5+6)/(1+2+3)"]
    equations = ["(600*5)/(SWAG[5,3,4]*2)", "(6*5)/4*2", "(6*5*4)/4*2"]
    # equations = ["-2"]
    # equations = ["1 + 2*3","2*3 + 1", "5 + 4", "6/3 + 2"]

    builder = ExpressionTreeBuilder()

    for equation in equations:
        print("====================")
        print(equation)
        exprtree = builder.create_expression_tree(equation)
        print(exprtree.get_postorder_result())
        print(exprtree.get_preorder_result())
        print(exprtree.get_inorder_result())
        print("====================")


def equalitycheck(val1, val2):
    print("---")
    print(val1)
    print(val2)
    if val1 == val2:
        print("Correct")
    else:
        print("==========FAIL==========")
    print("---")


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

# wells_tests()