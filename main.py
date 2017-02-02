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

    def inorder(self):
        self.__inorder_helper(self.__root)

    def __inorder_helper(self, node):
        if node:
            self.__inorder_helper(node.left)
            print node.value
            self.__inorder_helper(node.right)

    def preorder(self):
        self.__preorder_helper(self.__root)

    def __preorder_helper(self, node):
        if node:
            print node.value
            self.__preorder_helper(node.left)
            self.__preorder_helper(node.right)

    def postorder(self):
        self.__postorder_helper(self.__root)

    def __postorder_helper(self, node):
        if node:
            self.__postorder_helper(node.left)
            self.__postorder_helper(node.right)
            print node.value
            self.postorder_result.append(node.value)
            print "postorder", self.postorder_result

    def get_postorder_result(self):
        # print self.postorder_result
        return self.postorder_result


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


print "In Order:"
create_expression_tree("(A+B)*6").inorder()
#print "Post Order:"
#create_expression_tree("(A+B)*6").postorder()
print "Pre Order:"
create_expression_tree("(A+B)*6").preorder()

print "In Order:"
create_expression_tree("(A+B+C+D)/4").inorder()
print "Post Order:"
exprtree = create_expression_tree("(A+B+C+D)/(4)")
exprtree.postorder()


print "Pre Order:"
create_expression_tree("(A+B+C+D)/4").preorder()


print "Result:"
#print ExressionTree.get_postorder_result()

print exprtree.get_postorder_result();
