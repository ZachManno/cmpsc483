#Black box idea by Zach
#We have Templates that represent base equations such as a/b
#Each Template has a list of Options
#The Options contain the actual templates such as "A noun has b nouns. How many nouns does noun have?"
#Each Option also contains a Property class, which has properties about the Option such as how many nouns, does it use units, etc
#The idea is that when a user enters "(a+b)/c" we can use the parse tree to piece these templates together
#Many different combinations of Options and Templates can be used for the example above, we can print out say the best 5 or 10
#Some might make sense and some might not
#Extra logic can go into how to substitute certain types of Templates

import math
import random
import random_lists_data



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
    def __init__(self, numNouns=None,numNumbers=None,numUnits=None, lessMoreInput = None):
        """
        Class that the property data of each option is wrapped in

        :param propertiesInput: Input of class Property that describes the properties of this option (number of nouns verbs units etc)
        :param templateListInput: Input of a list containing the question for this option.
                                  This list can consist of strings, objects, or functions
                                  Ex: ["The", rand_noun, "has", rand_num, "apples]
        """
        if numNouns is None:
            self.nouns=0
        else:
            self.nouns = numNouns
        if numNumbers is None:
            self.numbers=0
        else:
            self.numbers = numNumbers
        if numUnits is None:
            self.units = 0
        else:
            self.units = numUnits
        if lessMoreInput is None:
            self.lessMore = 0
        else:
            self.lessMore = lessMoreInput


    def __str__(self):
        return "Properties:\nnouns = " + str(self.nouns) + "\nnumbers =" + str(self.numbers) + "\nunits =" + str(self.units) \
               + "\nlessMore =" + str(self.lessMore)

class RandItem(object):
    def __init__(self,idInput):
        """
        Class that has methods for getting random words/numbers

        :param idInput: The id determines which type of random item to return when the getRand() method is called

        """
        self.id = idInput

    def getRand(self,rangeInput=None):
        if rangeInput is None: #no range input, get random item based on id
            #could use a dispatcher here to call rand funct based on id but for now will use if else
            if self.id == 'noun':
                return 'dog' #just return any noun for now. later on could be theme class now or rand noun
            elif self.id == 'name':
                return random.choice(random_lists_data.NAMES)

        else: #this means there was a range input, so return a random number
            return random.randint(1,rangeInput)

    def getId(self):
        return self.id

    def __str__(self):
        return "Class: RandItem\nID = " + self.id



def test():
    p1 = Property(numUnits=3, numNouns=1)
    print("P1 =")
    print(p1)
    print('-------------')
    o1 = Option(p1, [RandItem('name'),"gets",RandItem('num'),"cars"])
    o2 = Option(p1, ["A", "Boy"])
    o3 = Option(p1, [4, "Cats"])
    t1 = Template("a*b")
    t1.options.append(o1)
    t1.options.append(o2)
    t1.options.append(o3)
    print(t1)

    print("--------------------------------")
    print("Option 1 template list printout:")
    for item in o1.templateList:
        # if the item in the list is a string print it
        if isinstance(item,str):
            print(item + " ", end='')
        # item is a RandItem object, need to get the random value (later on will use theme class)
        else:
            if item.getId() == 'num':
                print(str(item.getRand(7)) + " ", end='')
            else:
                print(item.getRand() + " ", end='')

    print('.')

test()



