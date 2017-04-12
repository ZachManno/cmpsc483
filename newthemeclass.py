import random_lists_data
import random
import importlib
import logging


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


def get_random_type():
    return random.choice(random_lists_data.ultimate_type_list)


# Specify How many of a class you need.
# On each, specify



class MulVerb(object):
    def __init__(self):
        self.wrappedstatement = []


# For down relations:
# They are reasonable items to contain ie A city has buildings. A city would not have atoms
class CITY(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.CITY_list)
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

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]



class STREETS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.STREETS_list)
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
                    'CITY'
                ]

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class BUILDINGS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.BUILDINGS_list)
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
                    #'COMPUTERS',
                    'DOORS',
                    'WINDOWS'
                ]
        }
        self.up_relations = {

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class CARS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.CARS_list)
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

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class PEOPLE(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.PEOPLE_list)
        self.objectTitleSingular = "PEOPLE"
        self.objectTitlePlural = "PEOPLE"
        self.down_relations = {
            'has':
                [
                    'ANIMALS',
                    #'ORGANS',
                    #'EYES',
                    #'LIMBS',
                    #'FINGERS',
                    #'TOES',
                    #'BONES',
                    #'TEETH'

                ]
            #,
            #'holds':
             #   [
              #      'CANDY',
               #     'MONEY',
                #    'FRUIT'
                #]
        }
        self.up_relations = {

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class PLANTS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.PLANTS_list)
        self.objectTitleSingular = "PLANT"
        self.objectTitlePlural = "PLANTS"
        self.down_relations = {
            #'has':
             #   [
                    #'LEAVES',
                    #'SEEDS',
                    #'BRANCHES'

             #   ]
        }
        self.up_relations = {

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class PARKS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.PARKS_list)
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

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class LIGHTS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.LIGHTS_list)
        self.objectTitleSingular = "LIGHT"
        self.objectTitlePlural = "LIGHTS"
        self.down_relations = {
            #'has':
            #    [
                    #'BULBS'
                    #'BATTERIES',
                    #'WIRES'
             #   ]
        }
        self.up_relations = {

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class ANIMALS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.ANIMALS_list)
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
            #'has':
             #   [
                    #'CLAWS',
                    #'FUR',
                    #'TAILS',
                    #'PAWS'
              #  ]
        }
        self.up_relations = {

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            # Random chance for adjective.
            modifier = ""
            if (bool(random.getrandbits(1))):
                modifier = random.choice(self.adjectives) + " "

            if len(self.instanceTitle) > 1:
                return modifier + self.instanceTitle[plurality]
            elif plurality:
                return modifier + self.instanceTitle[0] + "s"
            else:
                return modifier + self.instanceTitle[0]


class WINDOWS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.WINDOWS_list)
        self.objectTitleSingular = "WINDOW"
        self.objectTitlePlural = "WINDOWS"
        self.down_relations = {
            #'has':
             #   [
                    #'PARTICLES_OF_DUST'
#
              #  ]
        }
        self.up_relations = {

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class SEATS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.SEATS_list)
        self.objectTitleSingular = "SEAT"
        self.objectTitlePlural = "SEATS"
        self.down_relations = {
        }
        self.up_relations = {

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class DOORS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.DOORS_list)
        self.objectTitleSingular = "DOOR"
        self.objectTitlePlural = "DOORS"
        self.down_relations = {
            #'has':
            #    [
                    #'HANDLES',
                    #'LOCKS',
                    #'SPEAKERS'

             #   ]
        }
        self.up_relations = {

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class FLOOR_MATS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.FLOOR_MATS_list)
        self.objectTitleSingular = "FLOOR_MAT"
        self.objectTitlePlural = "FLOOR_MATS"
        self.down_relations = {
            #'has':
             #   [
              #      #'RIDGES'
#
              #  ]
        }
        self.up_relations = {

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class SIGNS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.SIGNS_list)
        self.objectTitleSingular = "SIGN"
        self.objectTitlePlural = "SIGNS"
        self.down_relations = {
            #'has':
            #    [
            #
             #   ]
        }
        self.up_relations = {

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class TRASH(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.TRASH_list)
        self.objectTitleSingular = "TRASH"
        self.objectTitlePlural = "TRASH"
        self.down_relations = {
            #'has':
             #   [

             #   ]
        }
        self.up_relations = {

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


class SIDEWALKS(object):
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

        }

    def getInstanceTitle(self, plurality):
        if (plurality != 0 and plurality != 1):
            raise Exception("Invalid plurality!")
        else:
            if len(self.instanceTitle) > 1:
                return self.instanceTitle[plurality]
            elif plurality:
                return self.instanceTitle[0] + "s"
            else:
                return self.instanceTitle[0]


def run():
    print('yo')

run()
