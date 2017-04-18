import newthemeclass
import tagassigner
import introdata

class EnglishProblemGenerator(object):

    def __init__(self, equation):
        """
        Generate english problems based on a math equation.
        :param equation: Equation input as a string
        """

        # Save strrep of equation for later.
        self.strequation = equation
        if type(equation) != "str":
            raise TypeError("Expected string for equation, received " + type(equation))

        # Format equation
        self.formatequation = tagassigner.Equation(self.strequation)

        # Generate dict tree representation.
        self.equationdict = self.generate_dict_tree(self.formatequation, 0, None)
        self.initialproblemtype = newthemeclass.get_random_type()

    def debug_type_test(self):
        #TODO Remove
        myclass = "CITY"
        myclassobject = newthemeclass.str_to_class("newthemeclass", myclass)
        print(type(myclassobject))
        print(myclassobject.instanceTitle)

    def debug_display_contents(self, equationdict):
        #TODO Remove
        for entry in equationdict:
            print(str(entry) + ": " + str(equationdict[entry][0].attribute) + " " + str(equationdict[entry][1]) + " " +
                  str(equationdict[entry][2]))

    def generate_dict_tree(self, node, myid, parent=None):
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
            childtree = self.generate_dict_tree(child, childid, myid)
            mychildren.append(childid)
            childid = max(childtree) + 1
            # Update root dict tree.
            for entry in childtree:
                dict_tree[entry] = childtree[entry]

        dict_tree[myid].append(mychildren)

        # Pass up dict tree to parent.
        return dict_tree

    def get_term(self, nodeid, equationdict):
        return equationdict[nodeid][0]

    def get_parent_id(self, nodeid, equationdict):
        # Node id: Node, Parentid, child list
        return equationdict[nodeid][1]

    def get_children(self, nodeid, equationdict):
        return equationdict[nodeid][2]

    def combine_subprob(self, begin, node, entity, end):
        subproblem = begin
        subproblem += node.attribute

        # Get subproblem title based on plurality.
        subproblem += " " + entity.getInstanceTitle(int(node.attribute != "1"))
        subproblem += end

        if subproblem[len(subproblem) - 1] != ".":
            subproblem += "."

        return subproblem

    def issign(self, text):
        return text == "+" or text == "-" or text == "*" or text == "/"

    def generate_problem_for_equation(self):
        """Generate initial statements. Determine type."""
        self.ultimatefinalproblem = ""
        self.problemtype = newthemeclass.get_random_type()
        self.problemobject = newthemeclass.str_to_class("newthemeclass", self.initialproblemtype)


        # Find the leftmost node.
        nodeid = 0
        while len(self.equationdict[nodeid][2]) > 0:
            nodeid = self.equationdict[nodeid][2][0]

        # Generate a humble introduction.
        self.ultimatefinalproblem += introdata.generate_intro()
        print("The topic is " + self.initialproblemtype)

        self.ultimatefinalproblem += self.get_term(nodeid, self.equationdict).attribute
        self.ultimatefinalproblem += " "

        rootattribute = self.get_term(nodeid, self.equationdict).attribute
        if rootattribute == "1":
            self.ultimatefinalproblem += self.problemobject.getInstanceTitle(0)
        else:
            self.ultimatefinalproblem += self.problemobject.getInstanceTitle(1)
        self.ultimatefinalproblem += ". "

        # Initiate recursion to generate problem.
        self.gen_on_datatype(rootattribute, 0)

        # Conclude problem.
        self.ultimatefinalproblem += introdata.generate_conclusion(self.problemtype)

        return self.ultimatefinalproblem

    def gen_on_datatype(self, attribute, childid):
        """Fork in problem generation based on subproblem attribute type."""
        if attribute == "+":
            self.gen_addition_helper(childid)
        elif attribute == "*":
            self.gen_mul_helper(childid)
        elif attribute == "/":
            self.gen_div_helper(childid)

    def gen_addition_helper(self, parentid):
        """Generate addition type subproblem based on parentid"""
        for childid in self.equationdict[parentid][2]:

            # Check attribute for sign, to determine path.
            attribute = self.equationdict[childid][0].attribute
            if self.issign(attribute):
                self.gen_on_datatype(attribute, childid)
            else:
                # Attribute is a variable. Update problem text based on addition connectors.
                themeobject = newthemeclass.str_to_class("newthemeclass", self.problemtype)

                intro = introdata.get_and_connector() + introdata.generate_intro().lower()
                self.ultimatefinalproblem += self.combine_subprob(intro, self.get_term(childid, self.equationdict),
                                                                  themeobject, "")

                self.ultimatefinalproblem += " "

    def gen_mul_helper(self, parentid):
        """Generate multiplilcation type subproblem based on parentid"""

        # Generate encapsulating terms for each mul piece.
        containerlist = []
        mulproblemtype = self.problemtype
        mulsubproblemstring = ""
        for dummy_idx in self.equationdict[parentid][0][2]:
            # Generate new theme object based on mulproblemtype
            themeobject = newthemeclass.str_to_class("newthemeclass", mulproblemtype)

            # Fetch a containing theme type for next object
            # mulproblemtype = get_up_relation(themeobject) #TODO: ????

            containerlist.insert(0, mulproblemtype)


        # Using container list, generate problem definition.
        for idx in range(len(self.equationdict[parentid][0][2])):
            multermid = self.equationdict[parentid][0][2][idx]
            problemtypeobject = containerlist[idx]

        self.ultimatefinalproblem += mulsubproblemstring
        pass #TODO Continue working

    def gen_div_helper(self, parentid):
        """Generate division type subproblem based on parentid"""
        pass