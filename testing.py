import newthemeclass
import tagassigner
import introdata


def debug_type_test():
    myclass = "CITY"
    myclassobject = newthemeclass.str_to_class("newthemeclass", myclass)
    print(type(myclassobject))
    print(myclassobject.instanceTitle)


def debug_display_contents(equationdict):
    for entry in equationdict:
        print(str(entry) + ": " + str(equationdict[entry][0].attribute) + " " + str(equationdict[entry][1]) + " " +
              str(equationdict[entry][2]))


# PROBLEM GENERATOR METHODS
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


def get_term(nodeid, equationdict):
    return equationdict[nodeid][0]


def get_parent_id(nodeid, equationdict):
    # Node id: Node, Parentid, child list
    return equationdict[nodeid][1]


def get_children(nodeid, equationdict):
    return equationdict[nodeid][2]


def combine_subprob(begin, node, entity, end):
    subproblem = begin
    subproblem += node.attribute

    # Get subproblem title based on plurality.
    subproblem += " " + entity.getInstanceTitle(int(node.attribute != "1"))

    subproblem += end

    if subproblem[len(subproblem) - 1] != ".":
        subproblem += "."

    return subproblem


def generate_problem_for_equation(equation):
    ultimatefinalproblem = ""

    # Format equation
    formatequation = tagassigner.Equation(equation)

    # Generate dict tree representation.
    equationdict = generate_dict_tree(formatequation, 0, None)

    # Find the leftmost node.
    nodeid = 0
    while len(equationdict[nodeid][2]) > 0:
        nodeid = equationdict[nodeid][2][0]

    # Generate a humble introduction.
    ultimatefinalproblem += introdata.generate_intro()
    initialproblemtype = newthemeclass.get_random_type()

    # initialproblemtype = "ANIMALS"
    print("The topic is " + initialproblemtype)

    # Chose "big type" for problem.

    initialobject = newthemeclass.str_to_class("newthemeclass", initialproblemtype)

    # ultimatefinalproblem += " "
    ultimatefinalproblem += get_term(nodeid, equationdict).attribute
    ultimatefinalproblem += " "

    if get_term(nodeid, equationdict).attribute == "1":
        ultimatefinalproblem += initialobject.getInstanceTitle(0)
    else:
        ultimatefinalproblem += initialobject.getInstanceTitle(1)

    ultimatefinalproblem += ". "

    # Keep building the problem based on what we see.
    previousobjecttype = initialproblemtype
    previousobject = initialobject
    mulchain = False

    nodeid += 1
    while nodeid < max(equationdict) + 1:
        if equationdict[get_parent_id(nodeid, equationdict)][0].attribute == "+":
            # Plus chain.
            newobject = newthemeclass.str_to_class("newthemeclass", initialproblemtype)
            attribute = get_term(nodeid, equationdict).attribute

            intro = introdata.get_and_connector() + introdata.generate_intro().lower()
            ultimatefinalproblem += combine_subprob(intro, get_term(nodeid, equationdict), newobject, "")

        if equationdict[get_parent_id(nodeid,equationdict)][0].attribute == "*":
            # Mulchain
            mulchain = True
            previousobjecttype = initialproblemtype

        ultimatefinalproblem += " "

        nodeid += 1

    # TODO Assuming counting for now.

    ultimatefinalproblem += introdata.generate_conclusion(initialproblemtype)

    return ultimatefinalproblem


def run_tests():
    """
    Run a series of tests to display equation output
    """

    equations = [
        # "a + b",
        "a + b + c",
        # "1 + 1 + b",
        # "a * b * c",
        # "a + b * c",
        # "a / b + c",
        # "c * g"
    ]

    for equation in equations:
        print("Original equation:")
        print(equation)

        print()
        print("Generated Problem:")
        print(generate_problem_for_equation(equation))

        print("=============")
        print()
        print()

for dummy_idx in range(3):
    run_tests()