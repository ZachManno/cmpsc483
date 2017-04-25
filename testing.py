import newthemeclass
import tagassigner2
import introdata
import inflect

p = inflect.engine()

class EnglishProblemGenerator(object):

    def __init__(self, equation):
        """
        Generate english problems based on a math equation.
        :param equation: Equation input as a string
        """

        # Save strrep of equation for later.
        self.strequation = equation
        # print(type(equation))
        # if type(equation) != type(str):
        #     raise TypeError("Expected string for equation, received " + type(equation))

        # Format equation
        self.formatequation = tagassigner2.compileequation(self.strequation)

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
        if (int(node.attribute != 1)):
            subproblem += " " + p.plural(entity.getInstanceTitle())
        else:
            subproblem += " " + entity.getInstanceTitle()
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
        print(self.initialproblemtype)
        self.problemobject = newthemeclass.str_to_class("newthemeclass", self.initialproblemtype)
        nodeid = 0

        # Generate a humble introduction.
        self.ultimatefinalproblem += introdata.generate_intro()
        print("The topic is " + self.problemtype)

        # Initiate recursion to generate problem.
        self.gen_on_datatype(self.get_term(nodeid, self.equationdict).attribute, 0)

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

    def gen_addition_helper(self, parentid, problemtype = "", quick=False):
        """Generate addition type subproblem based on parentid"""
        first = True


        for childid in self.equationdict[parentid][2]:
            # Check attribute for sign, to determine path.
            attribute = self.equationdict[childid][0].attribute
            if self.issign(attribute):
                self.gen_on_datatype(attribute, childid)
            else:
                # Attribute is a variable. Update problem text based on addition connectors.
                themeobject = newthemeclass.str_to_class("newthemeclass", self.problemtype)

                message = introdata.generate_intro().lower()
                if not first:
                    message = introdata.get_and_connector() + message
                else:
                    first = False

                self.ultimatefinalproblem += self.combine_subprob(message, self.get_term(childid, self.equationdict),
                                                                  themeobject, "")

                self.ultimatefinalproblem += " "

    def gen_mul_helper(self, parentid):
        """Generate multiplilcation type subproblem based on parentid"""

        # Generate encapsulating terms for each mul piece.
        containerlist = []
        tempobjectlist = []
        mulproblemtype = self.problemtype
        mulsubproblemstring = ""
        print("Ruhroh: " + self.problemtype)
        tempobjectlist.append(newthemeclass.str_to_class("newthemeclass", mulproblemtype))
        for idx in range(len(self.equationdict[parentid][2])):
            # Generate new theme object based on mulproblemtype
            prevobject = tempobjectlist[idx]
            print("Here: " + prevobject.objectTitleSingular)
            parentRelation = prevobject.getParentRelation()

            # Fetch a containing theme type for next object
            #parentRelation1 has:
            #       parentNoun object (parentRelation1.parent)
            #       childNoun object  (parentRelation1.child)
            #       downVerb string   (parentRelation1.downVerb)
            #       upVerb string     (parentRelation1.upVerb)

            containerlist.insert(0, parentRelation)
            tempobjectlist.append(parentRelation.parent)

        # Using container list, generate problem definition.
        prevproblem = None
        subproblem = False

        quickchain = False

        for idx in range(len(self.equationdict[parentid][2])):
            multermid = self.equationdict[parentid][2][idx]
            parentrelation = containerlist[idx]

            message = ""
            if prevproblem == None:
                test = True
                # message = introdata.get_and_connector() + message
            elif not subproblem:
                downverb = parentrelation.downVerb
                if parentrelation.downVerb == "":
                    downverb = "(MISSING)"

                # p.num(1)
                message = "Each " + prevproblem.getInstanceTitle() + " " + downverb + " "
            else:
                # We want the container type, not the instance type.
                # message = "For each " + prevproblem.get
                # p.num(1)
                message = "For each " + p.singular_noun(prevproblem.objectTitleSingular) + ", there are"

            # Todo THIS SHOULD SPLIT ON ATTR
            if self.equationdict[multermid][0].attribute == "+":
                self.ultimatefinalproblem += message
                subproblem = True
                self.gen_addition_helper(multermid)
                prevproblem = parentrelation.parent

            else:
                subproblem = False
                prevproblem = parentrelation.child
                # p.num(2)

                message += self.equationdict[multermid][0].attribute + " " + p.plural_noun(prevproblem.getInstanceTitle()) + ". "
                self.ultimatefinalproblem += message

            # self.ultimatefinalproblem += message


    def gen_div_helper(self, parentid):
        """Generate division type subproblem based on parentid"""
        pass