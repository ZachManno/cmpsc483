import newthemeclass
import tagassigner2
import introdata
import inflect
import random

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

    def has_replacer(self):
        return random.choice(['has', 'is beside', 'is around', 'is surrounded by',
                              'is flanked by', 'is situated beside'])

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

    def combine_subprob(self, begin, node, objecttitle, end):
        subproblem = begin
        subproblem += node.attribute

        # Get subproblem title based on plurality.

        if (int(node.attribute != 1)):
            subproblem += " " + p.plural(objecttitle)
        else:
            subproblem += " " + objecttitle
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
        self.denominatortype = ""
        print(self.initialproblemtype)
        self.problemobject = newthemeclass.str_to_class("newthemeclass", self.initialproblemtype)
        nodeid = 0

        # Generate a humble introduction.
        # self.ultimatefinalproblem += introdata.generate_intro()
        print("The topic is " + self.problemtype)

        # Initiate recursion to generate problem.
        self.gen_on_datatype(self.get_term(nodeid, self.equationdict).attribute, 0)

        # Conclude problem.
        self.ultimatefinalproblem += introdata.generate_conclusion(self.problemtype)

        return self.ultimatefinalproblem

    def gen_on_datatype(self, attribute, childid, problemType = None, quick = False):
        """Fork in problem generation based on subproblem attribute type."""
        if attribute == "+" or attribute == "-":
            self.gen_addition_helper(childid, problemType, quick)
        elif attribute == "*":
            self.gen_mul_helper(childid, problemType, quick)
        elif attribute == "/":
            self.gen_div_helper(childid, problemType, quick)

    def gen_addition_helper(self, parentid, problemtype = None, quick=False):
        """Generate addition type subproblem based on parentid"""
        first = True

        if problemtype == None:
            problemtype = self.problemtype

        # if quick:
        #     self.ultimatefinalproblem += " there are "

        for idx in range(len(self.equationdict[parentid][2])):
            childid = self.equationdict[parentid][2][idx]

            # Check attribute for sign, to determine path.
            attribute = self.equationdict[childid][0].attribute
            if self.issign(attribute):
                self.ultimatefinalproblem += introdata.generate_intro()
                self.gen_on_datatype(attribute, childid)
            else:
                # Attribute is a variable. Update problem text based on addition connectors.
                themeobject = newthemeclass.str_to_class("newthemeclass", problemtype)

                message = introdata.generate_intro().lower()
                if not first:
                    if self.equationdict[childid][0].sign == "+":
                        message = introdata.get_and_connector() + message
                    else:
                        message = introdata.get_sub_connector()
                else:
                    first = False

                # Special output for "Quick addition" (basically a list)
                if not quick:
                    title = themeobject.getInstanceTitle()
                    if self.equationdict[childid][0].sign == "-":
                        title = p.singular_noun(themeobject.objectTitlePlural.lower())

                    self.ultimatefinalproblem += self.combine_subprob(message, self.get_term(childid, self.equationdict),
                                                                  title, "")
                else:
                    coremessage = ""
                    term = self.get_term(childid, self.equationdict)

                    if self.equationdict[childid][0].sign == "+":
                        coremessage = term.attribute + " " + p.plural_noun(themeobject.getInstanceTitle())
                    else:
                        coremessage = introdata.get_sub_connector() + term.attribute + " " + p.plural_noun(themeobject.objectTitleSingular.lower())

                    if idx < len(self.equationdict[parentid][2]) - 1 and len(self.equationdict[parentid][2]) > 2:
                        # Comma separate
                        coremessage += ","

                    elif idx != 0:
                        # Final term of list (no comma!)
                        coremessage = "and " + coremessage + "."

                    self.ultimatefinalproblem += coremessage

                self.ultimatefinalproblem += " "

    def gen_mul_helper(self, parentid, problemType = None, quick = False):
        """Generate multiplilcation type subproblem based on parentid"""

        # Generate encapsulating terms for each mul piece.
        containerlist = []
        tempobjectlist = []
        mulproblemtype = self.problemtype
        if problemType != None:
            mulproblemtype = self.problemtype

        # Generate problem type based on mulproblemtype for each var in mul chain.
        print("Current Problem Type : " + self.problemtype)
        tempobjectlist.append(newthemeclass.str_to_class("newthemeclass", mulproblemtype))
        for idx in range(len(self.equationdict[parentid][2])):
            prevobject = tempobjectlist[idx]
            print("Here: " + prevobject.objectTitleSingular)
            parentRelation = prevobject.getParentRelation()

            # Save these for later.
            containerlist.insert(0, parentRelation)
            tempobjectlist.append(parentRelation.parent)

        # Using container list, generate problem definition.
        prevproblem = None
        subproblem = False


        for idx in range(len(self.equationdict[parentid][2])):
            # Get multermid and parent relation
            multermid = self.equationdict[parentid][2][idx]
            parentrelation = containerlist[idx]


            # Begin next multerm based on prev problem content
            message = ""
            if prevproblem != None:
                if not subproblem:
                    downverb = parentrelation.downVerb
                    if downverb == "has":
                        downverb = self.has_replacer()
                    if parentrelation.downVerb == "":
                        downverb = "(MISSING)"

                    message = "Each " + prevproblem.getInstanceTitle() + " " + downverb + " "
                else:
                    # We want the container type, not the instance type.
                    # message = "For each " + prevproblem.get
                    if not p.singular_noun(prevproblem.objectTitleSingular):
                        message = "For each " + prevproblem.objectTitleSingular + ", there are "
                    else:
                        message = "For each " + p.singular_noun(prevproblem.objectTitleSingular.lower()) + ", there are "


            # Finish displaying multerm. Recurse if necessary.
            if self.equationdict[multermid][0].attribute == "+":
                self.ultimatefinalproblem += message
                subproblem = True

                # Good chance of quick add. 80%.
                quick = random.randrange(100) < 80
                self.gen_addition_helper(multermid, parentrelation.child.objectTitlePlural, quick)
                prevproblem = parentrelation.child
            else:
                subproblem = False
                prevproblem = parentrelation.child

                message += self.equationdict[multermid][0].attribute + " " + p.plural_noun(prevproblem.getInstanceTitle()) + ". "
                self.ultimatefinalproblem += message

            # self.ultimatefinalproblem += message

    def gen_div_helper(self, parentid, problemType = None, quick = False):
        """Generate division type subproblem based on parentid"""
        childrenids = self.equationdict[parentid][2]

        # Get Denominator Type
        parentrelation = ""
        if self.denominatortype == "":
            parentrelation = self.problemobject.getParentRelation()
            self.denominator = parentrelation.parent


        # Display denominator
        denominator = self.equationdict[childrenids[1]]
        if self.issign(denominator[0].attribute):
            self.gen_on_datatype(denominator[0].attribute, childrenids[1], self.denominator.objectTitlePlural)
        else:
            self.ultimatefinalproblem += denominator[0].attribute + " " + p.plural_noun(self.denominator.getInstanceTitle()) + "."

        # Connect denominator into numerator
        self.ultimatefinalproblem += " Split evenly among these " + parentrelation.parent.objectTitlePlural.lower() + ", "

        # Display numerator
        numerator = self.equationdict[childrenids[0]]
        if self.issign(numerator[0].attribute):
            self.gen_on_datatype(numerator[0].attribute, childrenids[0])
        else:
            self.ultimatefinalproblem += numerator[0].attribute + " " + numerator.getInstanceTitle() + "."

        # Statement to eliminate denominator type.
        self.ultimatefinalproblem += " Consider only one " + p.singular_noun(parentrelation.parent.objectTitlePlural.lower()) + ". "

print(p.plural_verb("eat"))

#Each highway has b libraries.
"""
[has, is beside, is around, is surrounded by, is flanked, is situated beside]
"""