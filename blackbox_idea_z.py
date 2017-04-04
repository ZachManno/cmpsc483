#Black box idea by Zach
#We have Templates that represent base equations such as a/b
#Each Template has a list of Options
#The Options contain the actual templates such as "A noun has b nouns. How many nouns does noun have?"
#The "actual templates" just mentioned are stored as a list of strings and "Variable Classes" such as NounVar, NameVar, UnitVar
#[A, NounVar('a'), has , NumberVar('b'), NounVar('b') , ". How many" , NounVar('b'), does, NounVar('a'), have? ]
#Each NumberVar or NounVar or etc goes through the RandItem class to get the number or noun
#As of now I'm just pulling random numbers, nouns, names from a list. But later on it will pull from the Theme Class
#Each Option also contains a Property class, which has properties about the Option such as how many nouns, does it use units, etc
#The idea is that when a user enters "(a+b)/c" we can use the parse tree info with the Property class to piece these templates together
#Many different combinations of Options and Templates can be used for the example above, we can print out say the best 5 or 10
#Some might make sense and some might not
#Extra logic can go into how to substitute certain types of Templates


import math
import random
import random_lists_data

#helper function to remove duplicates from list
def removeDuplicates(input):
  output = []
  for x in input:
    if x not in output:
      output.append(x)
  return output


class Template(object):
    def __init__(self, idInput):
        """
        Template that will store one base equation such as "a*b"
        Right now id = "a*b" but I should make this a Term

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

    def generateTemplate(self):
        names = []
        nums = []
        nouns = []
        units = []
        outputstr = ""
        outputList
        for item in self.templateList:
            if isinstance(item, str):
                pass
            elif isinstance(item, NameVar):
                names.append(item.value)
            elif isinstance(item, NumberVar):
                nums.append(item.value)
            elif isinstance(item, NounVar):
                nouns.append(item.value)
            elif isinstance(item, UnitVar):
                units.append(item.value)

        names = removeDuplicates(names)
        nums = removeDuplicates(nums)
        nouns = removeDuplicates(nouns)
        units = removeDuplicates(units)


        for item in self.templateList:
            if isinstance(item, str):
                outputstr += item + " "
            elif isinstance(item, NameVar):
                for name in names:
                    if name == item.value:
                        outputstr += name + " "
            elif isinstance(item, NumberVar):
                for num in nums:
                    if num == item.value:
                        outputstr += str(num) + " "
            elif isinstance(item, NounVar):
                for noun in nouns:
                    if noun == item.value:
                        outputstr += noun
            elif isinstance(item, UnitVar):
                for unit in units:
                    if unit == item.value:
                        outputstr += unit
        outputstr += "?"
        return outputstr

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
            self.nouns = 0
        else:
            self.nouns = numNouns
        if numNumbers is None:
            self.numbers = 0
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
        return "Properties:\nnouns = " + str(self.nouns) + "\nnumbers =" + str(self.numbers) + "\nunits =" + str(self.units)

class RandItem(object):

    numsUsed = [] #keeping tabs on random numbers used so they are not used again

    #IDEA: Get random theme class right here, store as static variables, whenever random number or noun is needed pull from that

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
                noun = random.choice(random_lists_data.NOUNS)
                random_lists_data.NOUNS.remove(noun)
                return noun
            elif self.id == 'name':
                name = random.choice(random_lists_data.NAMES)
                random_lists_data.NAMES.remove(name)
                return name
            elif self.id == 'unit':
                unit = random.choice(random_lists_data.UNITS)
                random_lists_data.UNITS.remove(unit)
                return unit
        else: #this means there was a range input, so return a random number
            num = random.randint(1, rangeInput)
            if num not in RandItem.numsUsed:
                RandItem.numsUsed.append(num)
                return num
            else:
                print("ERROR RANDOM NUM THE SAME. FIX THIS ISSUE LATER(put while loop in)")


    def getId(self):
        return self.id

    def __str__(self):
        return "Class: RandItem\nID = " + self.id

#////////// VARIABLE CLASSES \\\\\\\\\\\\\\\\
#Each type of variable class takes in an id such as 'a' or 'b'
#For example, a template could be "NameVar('a') has NumberVar('a') items. How many items does NameVar('a') have? "
#                                   "Rodney has 5 items. How many items does Rodney have?
class NumberVar(object):
    nums = []
    def __init__(self,idInput):
        """
        Class that represents a random number variable

        :param idInput: The id of the variable ( 'a' or 'b' or 'c' or etc)

        """
        self.id = idInput
        flag = True
        for num in NumberVar.nums:
            if num.id == self.id:
                self.value = num.value
                flag = False

        if flag:
            self.value = RandItem('num').getRand(20)
            NumberVar.nums.append(self)

    def __str__(self):
        return "Num Var: id = " + self.id + " value = " + str(self.value)

class NameVar(object):
    names = []
    def __init__(self,idInput):
        """
        Class that represents a random name variable

        :param idInput: The id of the variable ( 'a' or 'b' or 'c' or etc)

        """
        self.id = idInput
        flag = True
        for name in NameVar.names:
            if name.id == self.id:
                self.value = name.value
                flag = False

        if flag:
            self.value = RandItem('name').getRand()
            NameVar.names.append(self)

    def __str__(self):
        return "Name Var: id = " + self.id + " value = " + self.value


class UnitVar(object):
    units = []
    def __init__(self, idInput):
        """
        Class that represents a random unit variable

        :param idInput: The id of the variable ( 'a' or 'b' or 'c' or etc)

        """
        self.id = idInput
        flag = True
        for unit in UnitVar.units:
            if unit.id == self.id:
                self.value = unit.value
                flag = False

        if flag:
            self.value = RandItem('unit').getRand()
            UnitVar.units.append(self)

    def __str__(self):
        return "Unit Var: id = " + self.id + " value = " + self.value

class NounVar(object):
    nouns = []

    def __init__(self, idInput):
        """
        Class that represents a random noun variable

        :param idInput: The id of the variable ( 'a' or 'b' or 'c' or etc)

        """
        self.id = idInput
        flag = True
        for noun in NounVar.nouns:
            if noun.id == self.id:
                self.value = noun.value
                flag = False

        if flag:
            self.value = RandItem('noun').getRand()
            NounVar.nouns.append(self)

    def __str__(self):
        return "Noun Var: id = " + self.id + " value = " + self.value

class HandleInput(object):
    """
    Class that will handle taking in the term and calling the appropriate classes and methods
    :param termInput: the term
    """

    def __init__(self,termInput):
        self.term = termInput
        print("Term input: " + str(self.term))


def test():

    #create property
    p1 = Property(numNouns=2,numNumbers=2)
    print("Property class example =")
    print(p1)
    print('-------------')

    #create option with property (option takes in property and option list)
    o1 = Option(p1, [NameVar('a'), 'spent', NumberVar('a'), 'dollars','for',NounVar('a'),'.','This','was',NumberVar('b'),'dollars','less','than','what',NameVar('b')
                     ,'spent','for',NounVar('b'),'.','How','much','did',NameVar('b'),'spend','on',NounVar('b')])

    #create another option with property
    p2 = Property(numNumbers=2,numNouns=1)
    o2 = Option(p2,[NameVar('a'),'has',NumberVar('a'),NounVar('a'),'s.',NameVar('b'),'has',NumberVar('b'),NounVar('a'), 's. '
                    'How','many','more',NounVar('a'), 's does', NameVar('b'),'have','than',NameVar('a')])
    #create template
    t1 = Template("a-b")
    #add two options to template
    t1.options.append(o1)
    t1.options.append(o2)
    print(t1)

    #repeat for template t2
    p3 = Property(numNumbers=2,numNouns=1,numUnits=1)
    o3 = Option(p3,['One',UnitVar('a'),' is' , NumberVar('a'), UnitVar('b'),'s. How much', UnitVar('b'), 's is', NumberVar('b'), UnitVar('a'),'s'])

    t2 = Template("a*b")
    t2.options.append(o3)

    print("--------------------------------")
    print("Template \"a-b\"")
    print("Option 1:")
    print(o1.generateTemplate())
    print("Option 2:")
    print(o2.generateTemplate())

    print("--------------------------------")
    print("Template \"a*b\"")
    print("Option 1:")
    print(o3.generateTemplate())


test()

#IDEA: maybe do all random item getting inside the Option class init

