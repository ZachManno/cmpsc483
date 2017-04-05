import newthemeclass
import tagassigner


myclass = "CITY"
myclassobject = newthemeclass.str_to_class("newthemeclass", myclass)
print(type(myclassobject))
print(myclassobject.instanceTitle)


def generate_dict_tree(node, myid, parent=None):
    """
    Recursively generate the tree reference structure.
    :param node: The currently viewed node.
    :param myid: The id of the node
    :param parent: The id of the parent node.
    :return: The dict_tree of this node and its children.
    """

    childid = myid + 1

    # Storing a node as {nodeid: nodeobject, parentid}
    dict_tree = {myid: [node, parent]}
    mychildren = []

    for child in node.terms:
        childtree = generate_dict_tree(child, childid, myid)
        mychildren.append(childid)
        childid = max(childtree) + 1
        # Update root dict tree.
        for entry in childtree:
            dict_tree[entry] = childtree[entry]

    dict_tree[myid].append(mychildren)

    # Pass up dict tree to parent.
    return dict_tree

def run_tests():
    """
    Run a series of tests to display equation output
    """

    equations = [
        "a + b",
        "a * b",
        "a * b * c",
        "a + b * c",
        "a / b + c"
    ]

    for equation in equations:
        print("Original equation:")
        print(equation)

        # Formate equation
        formatequation = tagassigner.Equation(equation)

        # Generate dict tree representation.
        equationdict = generate_dict_tree(formatequation, 0, None)

        for entry in equationdict:
            print(str(entry) + ": " + str(equationdict[entry][0].attribute) + " " + str(equationdict[entry][1]) + " " + str(equationdict[entry][2]))

        # Iterate through formated equation.


        # equation = ""
        #
        # for term in formatequation.terms:
        #     equation += str(term) + " "

        print("=============")
        print()
        print()

run_tests()