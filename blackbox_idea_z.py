#Black box idea by Zach
#We have Templates that represent base equations such as a/b
#Each Template has a list of Options
#The Options contain the actual templates such as "A noun has b nouns. How many nouns does noun have?"
#Each Option also contains a Property class, which has properties about the Option such as how many nouns, does it use units, etc
#The idea is that when a user enters "(a+b)/c" we can use the parse tree to piece these templates together
#Many different combinations of Options and Templates can be used for the example above, we can print out say the best 5 or 10
#Some might make sense and some might not
#Extra logic can go into how to substitute certain types of Templates





class Template(object):
    def __init__(self, idInput):
        """
        Template that will store one base equation such as "a*b"
        Right now id = "a*b" but possbily later on the id can be a Term

        :param idInput: String representation of an equation
        """
        self.id = idInput
        self.options = [] #list of Options

    def __str__(self):
        str1 = "Template:\nid = " + self.id + "\noptions =\n[\n"
        if self.options:
            for option in self.options:
                str1 += '{'
                str1 += str(option) + "\n"
                str1 += '}\n'
        str1 += "]"
        return str1

class Option(object):
    def __init__(self, propertiesInput,templateListInput):
        """
        An Option is one option to a Template
        Each Option has Property(ies) and the actual template question

        :param propertiesInput: Input of class Property that describes the properties of this option (number of nouns verbs units etc)
        :param templateListInput: Input of a list containing the question for this option.
                                  This list can consist of strings, objects, or functions
                                  Ex: ["The", rand_noun, "has", rand_num, "apples]
        """
        self.properties = propertiesInput
        self.templateList = templateListInput

    def __str__(self):
        str1 = "\ntemplateList:"
        str1 += "["
        if self.templateList:
            for item in self.templateList:
                str1 += str(item) + ","
        str1 = str1[:-1] #deletes extra comma off end of list
        str1 += "]\n"
        str1 += str(self.properties)
        return str1




class Property(object):
    def __init__(self, numNouns,numNumbers):
        """
        Class that the property data of each option is wrapped in

        :param propertiesInput: Input of class Property that describes the properties of this option (number of nouns verbs units etc)
        :param templateListInput: Input of a list containing the question for this option.
                                  This list can consist of strings, objects, or functions
                                  Ex: ["The", rand_noun, "has", rand_num, "apples]
        """
        self.nouns = numNouns
        self.numbers = numNumbers

    def __str__(self):
        return "Properties:\nnouns = " + str(self.nouns) + "\nnumbers =" + str(self.numbers)

def test():
    p1 = Property(2,3)
    print("P1 =")
    print(p1)
    print('-------------')
    o1 = Option(p1, ["The", "Dog"])
    o2 = Option(p1, ["A", "Boy"])
    o3 = Option(p1, [4, "Cats"])
    t1 = Template("a*b")
    t1.options.append(o1)
    t1.options.append(o2)
    t1.options.append(o3)
    print(t1)

test()

#NOTE: ADD FUNCTIONALITY TO PUT AS MANY PROPERTIES IN THE PROPERTIES CLASS AS YOU WANT, BY NAME