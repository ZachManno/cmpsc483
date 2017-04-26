import random_lists_data
import random
import importlib
import logging
import sys

class Name(object):
    def __init__(self):
        pass


def str_to_class(module_name, class_name):
    try:
        module_ = importlib.import_module(module_name)
        class_ = ""
        try:
            class_ = getattr(module_, class_name)
            class_ = class_()
        except AttributeError:
            logging.error('ERROR: Class ' + class_name + ' does not exist!!!\n\n')
    except ImportError:
        logging.error('Module does not exist')
    return class_ or None

def local_str_to_class(class_name):
    try:
        return getattr(sys.modules[__name__], class_name)()
    except AttributeError:
        logging.error("Class does not exist")

def get_random_type():
    return random.choice(random_lists_data.ultimate_type_list)



class Parent_relation(object):
    def __init__(self, parentIn, childIn,downVerbIn,upVerbIn):
        """
        Class to wrap the Parent Relation data and send to other modules

        :param parentIn:
        :param childIn:
        :param downVerbIn:
        :param upVerbIn:
        """
        self.parent = parentIn
        self.child = childIn
        self.downVerb = downVerbIn
        self.upVerb = upVerbIn

"""
BUILDING
IN
CITIES
HAS
BUILDING
"""



#new relation types other than has



class Noun_object(object):
    def __init__(self, instanceList,adjList):
        try:
            chance = (random.randint(1, 100))
            if chance < 41:
                self.instanceTitle = random.choice(adjList) + ' ' + random.choice(instanceList)
            else:
                self.instanceTitle = random.choice(instanceList)
        except NotImplementedError:
            logging.error("Instance list not implemented for " + self.objectTitlePlural + "!")
        self.down_relations = {

        }
        self.up_relations = {

        }
    def getInstanceTitle(self):
        return self.instanceTitle
    def getParentRelation(self):
        upVerb = random.choice(list(self.up_relations.keys()))
        parentNoun = random.choice(self.up_relations[upVerb])
        #print("parent noun = " + parentNoun)
        downVerb = ""
        downVerbList = []
        foundFlag = False


        myclassobject = local_str_to_class(parentNoun)
        #print("dict = " + str(myclassobject.down_relations))
        #print("dict with key = " + str(myclassobject.down_relations['has']))

        #get key ('has' or 'carries' or etc)
        for key in myclassobject.down_relations:
            # print(key, 'corresponds to', str(myclassobject.down_relations[key]))
            #
            # The dictionary has a key of the type of down relation ('has' or etc)
            # And a value of a list of all Noun_objects corresponding to said type of down relation
            # Example. key = 'has', myclassobject.down_relations[key] = ['ROOMS','PLANTS','PEOPLE'].
            for item in myclassobject.down_relations[key]:
                #print('item = ' + item)
                if item == self.__class__.__name__:
                    # print("found self = "+ self.__class__.__name__)
                    # print("key = " + key)
                    # print("parent noun = "+parentNoun)
                    downVerbList.append(key)
                    foundFlag = True



        #print("parent relation test:")
        #print(p1.parent,p1.downVerb,p1.child)
        #print(p1.child,p1.upVerb,p1.parent)
        if foundFlag:
            downVerb = random.choice(downVerbList)
            p1 = Parent_relation(local_str_to_class(parentNoun), self, downVerb, upVerb)
            return p1
        else:
            raise SystemError("No down relation found!\n Parent = " + parentNoun + " \n Child = " + self.objectTitleSingular)




#Generic container class to be used when we run out of up relations
class CONTAINERS(Noun_object):
    def __init__(self):
        super(CONTAINERS, self).__init__(random_lists_data.CONTAINERS_list,random_lists_data.CONTAINERS_list_adj)
        # Noun_object.__init__(random_lists_data.CITIES_list)
        # self.instanceTitle = random.choice(random_lists_data.CITIES_list)
        self.objectTitleSingular = "CONTAINER"
        self.objectTitlePlural = "CONTAINERS"
        self.down_relations = {
            #Each top level noun object of a chain must be in CONTAINER'S down relations list
            'has':
                [
                    'CONTAINERS',
                    'CONTINENTS'
                ]
        }
        self.up_relations = {
            'is in':
                [
                    'CONTAINERS'
                ]

        }

#Chains are defined by: Top level -> as many nouns as you would like ... -> nouns,with,no,down,relations,separated,by,commas

#Weights:
#100 = Generic container
#95 = top level of chain
#0 = nouns with no down relations

#////////////////// Geography chain \\\\\\\\\\\\\\\\\\\\\\\\\\
#  Continents -> Countries -> States -> Cities -> Streets -> Buildings .... -> Fruits,Trash,Signs,Floor mats,Windows

# For down relations:
# They are reasonable items to contain ie A CITIES has buildings. A CITIES would not have atoms
class CONTINENTS(Noun_object):
    def __init__(self):
        super(CONTINENTS, self).__init__(random_lists_data.CONTINENTS_list,random_lists_data.CONTINENTS_list_adj)
        # Noun_object.__init__(random_lists_data.CITIES_list)
        # self.instanceTitle = random.choice(random_lists_data.CITIES_list)
        self.objectTitleSingular = "CONTINENT"
        self.objectTitlePlural = "CONTINENTS"
        self.down_relations = {
            'consists of':
                [
                    'COUNTRIES',
                    'STATES',
                    'CITIES',
                ]
            ,
            'governs':
                [
                    'PEOPLE'
                ]
        }
        self.up_relations = {
            'is in':
                [
                    'CONTAINERS'
                ]

        }

class COUNTRIES(Noun_object):
    def __init__(self):
        super(COUNTRIES, self).__init__(random_lists_data.COUNTRIES_list,random_lists_data.COUNTRIES_list_adj)
        # Noun_object.__init__(random_lists_data.CITIES_list)
        # self.instanceTitle = random.choice(random_lists_data.CITIES_list)
        self.objectTitleSingular = "COUNTRY"
        self.objectTitlePlural = "COUNTRIES"
        self.down_relations = {
            'has':
                [
                    'CITIES',
                    'STATES',
                    'STREETS',
                    'BUILDINGS',
                    'CARS',
                    'PEOPLE',
                    'ANIMALS',
                    'PARKS'
                ]
        }
        self.up_relations = {
            'is in':
                [
                    'CONTINENTS'

                ]

        }


class STATES(Noun_object):
    def __init__(self):
        super(STATES, self).__init__(random_lists_data.STATES_list,random_lists_data.STATES_list_adj)
        # Noun_object.__init__(random_lists_data.CITIES_list)
        # self.instanceTitle = random.choice(random_lists_data.CITIES_list)
        self.objectTitleSingular = "STATE"
        self.objectTitlePlural = "STATES"
        self.down_relations = {
            'has':
                [
                    'CITIES',
                    'STREETS',
                    'BUILDINGS',
                    'CARS',
                    'PEOPLE',
                    'ANIMALS',
                    'PLANTS',
                    'PARKS',
                    'LIGHTS'
                ]
        }
        self.up_relations = {
            'is in':
                [
                    'CONTINENTS',
                    'COUNTRIES'

                ]

        }



class CITIES(Noun_object):
    def __init__(self):
        super(CITIES, self).__init__(random_lists_data.CITIES_list,random_lists_data.CITIES_list_adj)
        # Noun_object.__init__(random_lists_data.CITIES_list)
        # self.instanceTitle = random.choice(random_lists_data.CITIES_list)
        self.objectTitleSingular = "CITIES"
        self.objectTitlePlural = "CITIES"
        self.down_relations = {
            'has':
                [
                    'STREETS',
                    'BUILDINGS',
                    'CARS',
                    'PEOPLE',
                    'PLANTS',
                    'PARKS',
                    'LIGHTS',
                    'ANIMALS',
                    'WINDOWS'
                ]
            ,
            'develops':
                [
                    'BUILDINGS',
                    'PARKS'
                ]
            ,
            'houses':
                [
                    'PEOPLE',
                    'ANIMALS'
                ]
            ,
            'is illuminated by':
                [
                    'LIGHTS'
                ]
            ,
            'is overrun by':
                [
                    'ANIMALS'
                ]


        }
        self.up_relations = {
            'is in':
                [
                    'STATES',
                    'COUNTRIES',
                    'CONTINENTS'

                ]

        }

        #


class STREETS(Noun_object):
    def __init__(self):
        super(STREETS, self).__init__(random_lists_data.STREETS_list,random_lists_data.STREETS_list_adj)
        self.objectTitleSingular = "STREET"
        self.objectTitlePlural = "STREETS"
        self.down_relations = {
            'has':
                [
                    'PEOPLE',
                    'SIGNS',
                    'CARS',
                    'BUILDINGS',
                    'ANIMALS',
                    'PARKS',
                    'TRASH',
                    'LIGHTS',
                    'SIDEWALKS',
                    'DOORS'
                ]
            ,
            'houses':
                [
                    'PEOPLE',
                    'ANIMALS',
                ]

        }
        self.up_relations = {
            'is in':
                [
                    'CITIES',
                    'STATES',
                    'COUNTRIES'
                ]

        }


class BUILDINGS(Noun_object):
    def __init__(self):
        super(BUILDINGS, self).__init__(random_lists_data.BUILDINGS_list,random_lists_data.BUILDINGS_list_adj)
        self.objectTitleSingular = "BUILDING"
        self.objectTitlePlural = "BUILDINGS"
        self.down_relations = {
            'contains':
                [
                    #'FLOORS',
                    #'ROOMS',
                    #'STAIRS',
                    'PEOPLE',
                    'ANIMALS',
                    'PLANTS',
                    'LIGHTS',
                    # 'COMPUTERS',
                    'DOORS',
                    'WINDOWS',
                    'SIGNS',
                    'FLOOR_MATS',
                    'SEATS',
                    'TRASH'
                ]
            ,
            'is constructed with':
                [
                    #'FLOORS',
                    #'ROOMS',
                    #'STAIRS',
                    # 'COMPUTERS',
                    'DOORS',
                    'WINDOWS'
                ]
            ,
            'houses':
                [
                    'PEOPLE',
                    'ANIMALS',
                    'PLANTS'
                ]
        }
        self.up_relations = {
            'on':
                [
                    'STREETS'
                ]
            ,
            'is in':
                [
                    'CITIES',
                    'STATES',
                    'COUNTRIES'
                ]
            ,
            'illuminated by':
            [
                'LIGHTS'
            ]

        }


class CARS(Noun_object):
    def __init__(self):
        super(CARS, self).__init__(random_lists_data.CARS_list,random_lists_data.CARS_list_adj)
        self.objectTitleSingular = "CAR"
        self.objectTitlePlural = "CARS"
        self.down_relations = {
            'has':
                [
                    'PEOPLE',
                    'ANIMALS',
                    'WINDOWS',
                    'SEATS',
                    'DOORS',
                    'LIGHTS',
                    'FLOOR_MATS',
                    'TRASH'
                ]
            ,
            'fits':
                [
                    'PEOPLE',
                    'ANIMALS',
                    'FLOOR_MATS',
                    'TRASH'
                ]
            ,
            'transports':
                [
                    'PEOPLE',
                    'ANIMALS',
                ]
        }
        self.up_relations = {
            'on':
                [
                    'STREETS'
                ]
            ,
            'is in':
                [
                    'CITIES',
                    'STATES',
                    'COUNTRIES'
                ]

        }


class PEOPLE(Noun_object):
    def __init__(self):
        super(PEOPLE, self).__init__(random_lists_data.PEOPLE_list,random_lists_data.PEOPLE_list_adj)
        self.objectTitleSingular = "PEOPLE"
        self.objectTitlePlural = "PEOPLE"
        self.down_relations = {
            'owns':
                [
                    'ANIMALS',
                    'BASKETS',
                    'FRUITS'
                    # 'ORGANS',
                    # 'EYES',
                    # 'LIMBS',
                    # 'FINGERS',
                    # 'TOES',
                    # 'BONES',
                    # 'TEETH'

                ]
            ,
            'holds':
                [
                    'BASKETS',
                    'FRUITS',
                ]
            ,
            'eats':
                [
                    'FRUITS',
                    'ANIMALS',
                ]
        }
        self.up_relations = {
            'is in':
                [
                    'BUILDINGS',
                    'STREETS',
                    'PARKS',
                    'CITIES',
                    'STATES',
                    'COUNTRIES',
                    'CONTINENTS'
                ]
            ,
            'drives':
                [
                    'CARS'
                ]
            ,
            'occupies':
                [
                    'SIDEWALKS'
                ]
            ,
            'held by':
                [
                    'SEATS'
                ]

        }




class PARKS(Noun_object):
    def __init__(self):
        super(PARKS, self).__init__(random_lists_data.PARKS_list,random_lists_data.PARKS_list_adj)
        self.objectTitleSingular = "PARK"
        self.objectTitlePlural = "PARKS"
        self.down_relations = {
            'has':
                [
                    'PEOPLE',
                    'ANIMALS',
                    'PLANTS',
                    'SIDEWALKS',
                    'LIGHTS',
                    'TRASH',
                    'SEATS',
                    'SIGNS'

                ]
        }
        self.up_relations = {
            'on':
                [
                    'STREETS'
                ]
            ,
            'is in':
                [
                    'CITIES',
                    'STATES',
                    'COUNTRIES'
                ]

        }

class PLANTS(Noun_object):
    def __init__(self):
        super(PLANTS, self).__init__(random_lists_data.PLANTS_list,random_lists_data.PLANTS_list_adj)
        self.objectTitleSingular = "PLANT"
        self.objectTitlePlural = "PLANTS"
        self.down_relations = {
            # 'has':
            #   [
            # 'LEAVES',
            # 'SEEDS',
            # 'BRANCHES'

            #   ]
        }
        self.up_relations = {
            'is in':
                [
                    'PARKS',
                    'BUILDINGS',
                    'CITIES',
                    'STATES'
                ]

        }


class LIGHTS(Noun_object):
    def __init__(self):
        super(LIGHTS, self).__init__(random_lists_data.LIGHTS_list,random_lists_data.LIGHTS_list_adj)
        self.objectTitleSingular = "LIGHT"
        self.objectTitlePlural = "LIGHTS"
        self.down_relations = {
            # 'has':
            #    [
            # 'BULBS'
            # 'BATTERIES',
            # 'WIRES'
            #   ]
            'illuminates':
                [
                    "BUILDINGS",
                    "SIDEWALKS"
                ]
        }
        self.up_relations = {
            'is in':
                [
                    'CARS',
                    'PARKS',
                    'BUILDINGS',
                    'CITIES',
                    'STATES'
                ]
            ,
            'on':
                [
                    'STREETS'
                ]

        }


class ANIMALS(Noun_object):
    def __init__(self):
        super(ANIMALS, self).__init__(random_lists_data.ANIMALS_list,random_lists_data.ANIMALS_list_adj)
        self.objectTitleSingular = "ANIMAL"
        self.objectTitlePlural = "ANIMALS"
        self.down_relations = {
            'eats':
                [
                    'FRUITS'
                ]
        }
        self.up_relations = {
            'is in':
                [
                    'PARKS',
                    'CARS',
                    'BUILDINGS',
                    'CITIES',
                    'STATES',
                    'COUNTRIES'
                ]
            ,
            'on':
                [
                    'STREETS',
                    'SIDEWALKS'
                ]
            ,
            'is owned by':
                [
                    'PEOPLE'
                ]
            ,
            'held by':
                [
                    'SEATS'
                ]

        }


class WINDOWS(Noun_object):
    def __init__(self):
        super(WINDOWS, self).__init__(random_lists_data.WINDOWS_list,random_lists_data.WINDOWS_list_adj)
        self.objectTitleSingular = "WINDOW"
        self.objectTitlePlural = "WINDOWS"
        self.down_relations = {
            # 'has':
            #   [
            # 'PARTICLES_OF_DUST'
            #
            #  ]
        }
        self.up_relations = {
            'is in':
                [
                    'CARS',
                    'BUILDINGS',
                    'CITIES'
                ]

        }


class SEATS(Noun_object):
    def __init__(self):
        super(SEATS, self).__init__(random_lists_data.SEATS_list,random_lists_data.SEATS_list_adj)
        self.objectTitleSingular = "SEAT"
        self.objectTitlePlural = "SEATS"
        self.down_relations = {
            'holds':
                [
                    "PEOPLE",
                    "ANIMALS"
                ]
        }
        self.up_relations = {
            'is in':
                [
                    'PARKS',
                    'CARS',
                    'BUILDINGS'
                ]

        }


class DOORS(Noun_object):
    def __init__(self):
        super(DOORS, self).__init__(random_lists_data.DOORS_list,random_lists_data.DOORS_list_adj)
        self.objectTitleSingular = "DOOR"
        self.objectTitlePlural = "DOORS"
        self.down_relations = {
            # 'has':
            #    [
            # 'HANDLES',
            # 'LOCKS',
            # 'SPEAKERS'

            #   ]
        }
        self.up_relations = {
            'is in':
                [
                    'BUILDINGS'
                ]
            ,
            'on':
                [
                    'CARS',
                    'STREETS'
                ]

        }


class FLOOR_MATS(Noun_object):
    def __init__(self):
        super(FLOOR_MATS, self).__init__(random_lists_data.FLOOR_MATS_list,random_lists_data.FLOOR_MATS_list_adj)
        self.objectTitleSingular = "FLOOR_MAT"
        self.objectTitlePlural = "FLOOR_MATS"
        self.down_relations = {
            # 'has':
            #   [
            #      #'RIDGES'
            #
            #  ]
        }
        self.up_relations = {
            'is in':
                [
                    'CARS',
                    'BUILDINGS'
                ]

        }


class SIGNS(Noun_object):
    def __init__(self):
        super(SIGNS, self).__init__(random_lists_data.SIGNS_list,random_lists_data.SIGNS_list_adj)
        self.objectTitleSingular = "SIGN"
        self.objectTitlePlural = "SIGNS"
        self.down_relations = {
            # 'has':
            #    [
            #
            #   ]
        }
        self.up_relations = {
            'is in':
                [
                    'PARKS',
                    'BUILDINGS'
                ]
            ,
            'on':
                [
                    'STREETS'
                ]

        }


class TRASH(Noun_object):
    def __init__(self):
        super(TRASH, self).__init__(random_lists_data.TRASH_list,random_lists_data.TRASH_list_adj)
        self.objectTitleSingular = "TRASH"
        self.objectTitlePlural = "TRASH"
        self.down_relations = {
            # 'has':
            #   [

            #   ]
        }
        self.up_relations = {
            'on':
                [
                    'STREETS',
                    'SIDEWALKS'
                ]
            ,
            'is in':
                [
                    'PARKS',
                    'CARS',
                    'BUILDINGS'
                ]

        }


class SIDEWALKS(Noun_object):
    def __init__(self):
        super(SIDEWALKS, self).__init__(random_lists_data.SIDEWALKS_list,random_lists_data.SIDEWALKS_list_adj)
        self.objectTitleSingular = "SIDEWALK"
        self.objectTitlePlural = "SIDEWALKS"
        self.down_relations = {
            'has':
                [
                    'PEOPLE',
                    'TRASH',
                    'ANIMALS'
                ]
        }
        self.up_relations = {
            'on':
                [
                    'PARKS',
                    'STREETS'
                ]
            ,
            'illuminated by':
                [
                    "LIGHTS",
                ]

        }

class BASKETS(Noun_object):
    def __init__(self):
        super(BASKETS, self).__init__(random_lists_data.BASKETS_list,random_lists_data.BASKETS_list_adj)
        self.objectTitleSingular = "BASKET"
        self.objectTitlePlural = "BASKETS"
        self.down_relations = {
            'has':
                [
                    'FRUITS'
                ]
        }
        self.up_relations = {
            'is owned by':
                [
                    'PEOPLE'
                ]

        }

class FRUITS(Noun_object):
    def __init__(self):
        super(FRUITS, self).__init__(random_lists_data.FRUITS_list,random_lists_data.FRUITS_list_adj)
        self.objectTitleSingular = "FRUIT"
        self.objectTitlePlural = "FRUITS"
        self.down_relations = {

        }
        self.up_relations = {
            'is in':
                [
                    'BASKETS'
                ]
            ,
            'eaten by':
                [
                    'ANIMALS',
                    'PEOPLE'
                ]

        }

#There are b streets. All streets have c cars. How many cars?



#There are c cages. Each cage has f animals. How many animals?

#STREET/ROAD/TYPE OF



#////////////////// End Geography chain \\\\\\\\\\\\\\\\\\\\\\\\\\