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


class Noun_object(object):
    def __init__(self, instanceList):
        self.instanceTitle = random.choice(instanceList)


# For down relations:
# They are reasonable items to contain ie A city has buildings. A city would not have atoms
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

        }

        #


class STREETS(object):
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
                    'CITY'
                ]

        }


class BUILDINGS(object):
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

        }


class CARS(object):
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

        }


class PEOPLE(object):
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

        }


class PLANTS(object):
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

        }


class PARKS(object):
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

        }


class LIGHTS(object):
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

        }


class ANIMALS(object):
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

        }


class WINDOWS(object):
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

        }


class SEATS(object):
    def __init__(self):
        super(SEATS, self).__init__(random_lists_data.SEATS_list)
        self.objectTitleSingular = "SEAT"
        self.objectTitlePlural = "SEATS"
        self.down_relations = {
        }
        self.up_relations = {

        }


class DOORS(object):
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

        }


class FLOOR_MATS(object):
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

        }


class SIGNS(object):
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

        }


class TRASH(object):
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

        }


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


def run():
    c1 = CITY()
    print(c1.instanceTitle)