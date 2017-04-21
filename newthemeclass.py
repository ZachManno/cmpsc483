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
        try:
            class_ = getattr(module_, class_name)()
        except AttributeError:
            logging.error('Class does not exist')
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


# Specify How many of a class you need.
# On each, specify
class Parent_relation(object):
    def __init__(self, parentIn, childIn,downVerbIn,upVerbIn):
        self.parent = parentIn
        self.child = childIn
        self.downVerb = downVerbIn
        self.upVerb = upVerbIn

"""
BUILDING
IN
CITY
HAS
BUILDING
"""






class Noun_object(object):
    def __init__(self, instanceList):
        self.instanceTitle = random.choice(instanceList)
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


        myclassobject = local_str_to_class(parentNoun)
        #print("bruh = " + str(myclassobject.down_relations))
        #print("yo = " + str(myclassobject.down_relations['has']))

        #get key ('has' or 'carries' or etc)
        for key in myclassobject.down_relations:
            #print(key, 'corresponds to', str(myclassobject.down_relations[key]))
            #The dictionary has a key of the type of down relation ('has' or etc)
            #And a value of a list of all Noun_objects corresponding to said type of down relation
            #Example. key = 'has', myclassobject.down_relations[key] = ['ROOMS','PLANTS','PEOPLE'].
            for item in myclassobject.down_relations[key]:
                #print('item = ' + item)
                if item == self.__class__.__name__:
                    # print("found self = "+ self.__class__.__name__)
                    # print("key = " + key)
                    # print("parent noun = "+parentNoun)
                    downVerb = key


        p1 =  Parent_relation(local_str_to_class(parentNoun),self,downVerb,upVerb)
        #print("parent relation test:")
        #print(p1.parent,p1.downVerb,p1.child)
        #print(p1.child,p1.upVerb,p1.parent)
        return p1




# For down relations:
# They are reasonable items to contain ie A city has buildings. A city would not have atoms
class CONTINENTS(Noun_object):
    def __init__(self):
        super(CONTINENTS, self).__init__(random_lists_data.CONTINENTS_list)
        # Noun_object.__init__(random_lists_data.CITY_list)
        # self.instanceTitle = random.choice(random_lists_data.CITY_list)
        self.adjectives = [
            'Cold',
            'Warm',
        ]
        self.objectTitleSingular = "CONTINENT"
        self.objectTitlePlural = "CONTINENTS"
        self.down_relations = {
            'has':
                [
                    'COUNTRIES',
                    'PEOPLE'
                ]
        }
        self.up_relations = {

        }

class COUNTRIES(Noun_object):
    def __init__(self):
        super(COUNTRIES, self).__init__(random_lists_data.COUNTRIES_list)
        # Noun_object.__init__(random_lists_data.CITY_list)
        # self.instanceTitle = random.choice(random_lists_data.CITY_list)
        self.adjectives = [
            'Crowded',
            'Developed',
        ]
        self.objectTitleSingular = "COUNTRY"
        self.objectTitlePlural = "COUNTRIES"
        self.down_relations = {
            'has':
                [
                    'STATES',
                    'STREETS',
                    'BUILDINGS',
                    'CARS',
                    'PEOPLE'
                ]
        }
        self.up_relations = {
            'in':
                [
                    'CONTINENTS'

                ]

        }


class STATES(Noun_object):
    def __init__(self):
        super(STATES, self).__init__(random_lists_data.STATES_list)
        # Noun_object.__init__(random_lists_data.CITY_list)
        # self.instanceTitle = random.choice(random_lists_data.CITY_list)
        self.adjectives = [
            'Crowded',
            'Developed',
        ]
        self.objectTitleSingular = "STATE"
        self.objectTitlePlural = "STATES"
        self.down_relations = {
            'has':
                [
                    'CITY',
                    'STREETS',
                    'BUILDINGS',
                    'CARS',
                    'PEOPLE'
                ]
        }
        self.up_relations = {
            'in':
                [
                    'COUNTRIES',
                    'CONTINENTS'

                ]

        }



class CITY(Noun_object):
    def __init__(self):
        super(CITY, self).__init__(random_lists_data.CITY_list)
        # Noun_object.__init__(random_lists_data.CITY_list)
        # self.instanceTitle = random.choice(random_lists_data.CITY_list)
        self.adjectives = [
            'Gleaming',
            'Dirty',
            'Clean',
            'Crowded',
            'Developed',
        ]
        self.objectTitleSingular = "CITY"
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
                    'ANIMALS'
                ]
        }
        self.up_relations = {
            'in':
                [
                    'STATES',
                    'COUNTRIES',
                    'CONTINENTS'

                ]

        }

        #


class STREETS(Noun_object):
    def __init__(self):
        super(STREETS, self).__init__(random_lists_data.STREETS_list)
        self.adjectives = [
            'Dirty',
            'Clean',
            'Crowded',
            'Packed',
        ]
        self.objectTitleSingular = "STREET"
        self.objectTitlePlural = "STREETS"
        self.down_relations = {
            'has':
                [
                    'PEOPLE',
                    'SIGNS',
                    'CARS',
                    'BUILDINGS',
                    'TRASH',
                    'LIGHTS',
                    'SIDEWALK'
                ]

        }
        self.up_relations = {
            'in':
                [
                    'CITY',
                    'STATES',
                    'COUNTRIES'
                ]

        }


class BUILDINGS(Noun_object):
    def __init__(self):
        super(BUILDINGS, self).__init__(random_lists_data.BUILDINGS_list)
        self.objectTitleSingular = "BUILDING"
        self.objectTitlePlural = "BUILDINGS"
        self.down_relations = {
            'has':
                [
                    'FLOORS',
                    'ROOMS',
                    'STAIRS',
                    'PEOPLE',
                    'LIGHTS',
                    # 'COMPUTERS',
                    'DOORS',
                    'WINDOWS'
                ]
        }
        self.up_relations = {
            'on':
                [
                    'STREETS'
                ]
            ,
            'in':
                [
                    'CITY',
                    'STATES',
                    'COUNTRIES'
                ]

        }


class CARS(Noun_object):
    def __init__(self):
        super(CARS, self).__init__(random_lists_data.CARS_list)
        self.objectTitleSingular = "CAR"
        self.objectTitlePlural = "CARS"
        self.down_relations = {
            'has':
                [
                    'PEOPLE',
                    'WINDOWS',
                    'SEATS',
                    'DOORS',
                    'LIGHTS',
                    'FLOOR MATS'
                ]
        }
        self.up_relations = {
            'on':
                [
                    'STREETS'
                ]
            ,
            'in':
                [
                    'CITY',
                    'STATES',
                    'COUNTRIES'
                ]

        }


class PEOPLE(Noun_object):
    def __init__(self):
        super(PEOPLE, self).__init__(random_lists_data.PEOPLE_list)
        self.objectTitleSingular = "PEOPLE"
        self.objectTitlePlural = "PEOPLE"
        self.down_relations = {
            'has':
                [
                    'ANIMALS',
                    # 'ORGANS',
                    # 'EYES',
                    # 'LIMBS',
                    # 'FINGERS',
                    # 'TOES',
                    # 'BONES',
                    # 'TEETH'

                ]
            # ,
            # 'holds':
            #   [
            #      'CANDY',
            #     'MONEY',
            #    'FRUIT'
            # ]
        }
        self.up_relations = {
            'in':
                [
                    'BUILDINGS',
                    'STREETS',
                    'CITY',
                    'STATES',
                    'COUNTRIES'
                ]

        }




class PARKS(Noun_object):
    def __init__(self):
        super(PARKS, self).__init__(random_lists_data.PARKS_list)
        self.objectTitleSingular = "PARK"
        self.objectTitlePlural = "PARKS"
        self.down_relations = {
            'has':
                [
                    'PEOPLE',
                    'ANIMALS',
                    'PLANTS',
                    'LIGHTS'

                ]
        }
        self.up_relations = {
            'on':
                [
                    'STREETS'
                ]
            ,
            'in':
                [
                    'CITY',
                    'STATES',
                    'COUNTRIES'
                ]

        }

class PLANTS(Noun_object):
    def __init__(self):
        super(PLANTS, self).__init__(random_lists_data.PLANTS_list)
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
            'in':
                [
                    'PARKS',
                    'CARS',
                    'BUILDINGS',
                    'CITY',
                    'STATES',
                    'COUNTRIES'
                ]

        }


class LIGHTS(Noun_object):
    def __init__(self):
        super(LIGHTS, self).__init__(random_lists_data.LIGHTS_list)
        self.objectTitleSingular = "LIGHT"
        self.objectTitlePlural = "LIGHTS"
        self.down_relations = {
            # 'has':
            #    [
            # 'BULBS'
            # 'BATTERIES',
            # 'WIRES'
            #   ]
        }
        self.up_relations = {
            'in':
                [
                    'PARKS',
                    'BUILDINGS',
                    'CITY',
                    'STATES',
                    'COUNTRIES'
                ]
            ,
            'on':
                [
                    'STREETS'
                ]

        }


class ANIMALS(Noun_object):
    def __init__(self):
        super(ANIMALS, self).__init__(random_lists_data.ANIMALS_list)
        self.adjectives = [
            "fluffy",
            "furry",
            "silky",
            "loud",
            "lumbering",
            "hibernating",
            "shaggy",
            "tired",
        ]

        self.objectTitleSingular = "ANIMAL"
        self.objectTitlePlural = "ANIMALS"
        self.down_relations = {
            # 'has':
            #   [
            # 'CLAWS',
            # 'FUR',
            # 'TAILS',
            # 'PAWS'
            #  ]
        }
        self.up_relations = {
            'in':
                [
                    'PARKS',
                    'CARS',
                    'BUILDINGS',
                    'CITY',
                    'STATES',
                    'COUNTRIES'
                ]
            ,
            'on':
                [
                    'STREETS'
                ]

        }


class WINDOWS(Noun_object):
    def __init__(self):
        super(WINDOWS, self).__init__(random_lists_data.WINDOWS_list)
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
            'in':
                [
                    'CARS',
                    'BUILDINGS',
                    'CITY',
                    'STATES'
                ]

        }


class SEATS(Noun_object):
    def __init__(self):
        super(SEATS, self).__init__(random_lists_data.SEATS_list)
        self.objectTitleSingular = "SEAT"
        self.objectTitlePlural = "SEATS"
        self.down_relations = {
        }
        self.up_relations = {
            'in':
                [
                    'PARKS',
                    'CARS',
                    'BUILDINGS'
                ]

        }


class DOORS(Noun_object):
    def __init__(self):
        super(DOORS, self).__init__(random_lists_data.DOORS_list)
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
            'in':
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
        super(FLOOR_MATS, self).__init__(random_lists_data.FLOOR_MATS_list)
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
            'in':
                [
                    'CARS',
                    'BUILDINGS'
                ]

        }


class SIGNS(Noun_object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.SIGNS_list)
        self.objectTitleSingular = "SIGN"
        self.objectTitlePlural = "SIGNS"
        self.down_relations = {
            # 'has':
            #    [
            #
            #   ]
        }
        self.up_relations = {
            'in':
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
        self.instanceTitle = random.choice(random_lists_data.TRASH_list)
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
                    'STREETS'
                ]
            ,
            'in':
                [
                    'PARKS',
                    'CARS',
                    'BUILDINGS'
                ]

        }


class SIDEWALKS(Noun_object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.SIDEWALKS_list)
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

        }



#There are b streets. All streets have c cars. How many cars?



#There are c cages. Each cage has f animals. How many animals?

#STREET/ROAD/TYPE OF