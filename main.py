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

def postfix_convert(infix):
    stack = []
    postfix = []

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

    while len(stack) != 0:
        postfix.append(stack.pop())

    return postfix


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class ExressionTree(object):

    def __init__(self, root=None):
        self.__root = root
        self.postorder_result = []
        self.preorder_result = []
        self.inorder_result = []

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
        if node:
            self.__inorder_helper(node.left)
            self.inorder_result.append(node.value)
            self.__inorder_helper(node.right)

    def __preorder_helper(self, node):
        if node:
            self.preorder_result.append(node.value)
            self.__preorder_helper(node.left)
            self.__preorder_helper(node.right)

    def __postorder_helper(self, node):
        if node:
            self.__postorder_helper(node.left)
            self.__postorder_helper(node.right)
            self.postorder_result.append(node.value)

    """
    Getters for Order Results
    """

    def get_postorder_result(self):
        if self.postorder_result == []:
            self.generate_postorder()

        return self.postorder_result

    def get_preorder_result(self):
        if self.preorder_result == []:
            self.generate_preorder()

        return self.preorder_result

    def get_inorder_result(self):
        if self.inorder_result == []:
            self.generate_inorder()

        return self.inorder_result



def create_expression_tree(infix):
    infix = "".join(infix.split())
    postfix = postfix_convert(infix)

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

    return ExressionTree(stack.pop())

def run_tests():
    print "In Order:"
    create_expression_tree("(A+B)*6").generate_inorder()
    #print "Post Order:"
    #create_expression_tree("(A+B)*6").postorder()
    print "Pre Order:"
    create_expression_tree("(A+B)*6").generate_preorder()

    print "In Order:"
    create_expression_tree("(A+B+C+D)/4").generate_inorder()
    print "Post Order:"
    exprtree = create_expression_tree("(A+B+C+D)/(4)")
    exprtree.generate_postorder()


    print "Pre Order:"
    create_expression_tree("(A+B+C+D)/4").generate_preorder()


    print "Result:"
    #print ExressionTree.get_postorder_result()

    print exprtree.get_postorder_result()

def wells_tests():
