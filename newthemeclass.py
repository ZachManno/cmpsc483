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

# Specify How many of a class you need.
# On each, specify



class MulVerb(object):
    def __init__(self):
        self.wrappedstatement = []



#For down relations:
#They are reasonable items to contain ie A city has buildings. A city would not have atoms
class CITY(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.CITY_list)
        self.objectTitleSingular = "CITY"
        self.objectTitlePlural = "CITIES"
        self.down_relations = {
            'has': [    'ZIP_CODES', 'STREETS', 'BUILDINGS', 'CARS','PEOPLE', 'PLANTS', 'PARKS', 'AIR', 'LIGHTS', 'ANIMALS']
        }
        self.up_relations = {

        }








class ZIP_CODES(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.ZIP_CODES_list)
        self.objectTitleSingular = "ZIP_CODE"
        self.objectTitlePlural = "ZIP_CODES"
        self.down_relations = {
            'has': ['burrows']
        }
        self.up_relations = {

        }



class STREETS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.STREETS_list)
        self.objectTitleSingular = "STREET"
        self.objectTitlePlural = "STREETS"
        self.down_relations = {
            'has': ['people', 'signs', 'cars', 'buildings', 'trash', 'lights', 'sidewalk']
        }
        self.up_relations = {

        }



class BUILDINGS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.BUILDINGS_list)
        self.objectTitleSingular = "BUILDING"
        self.objectTitlePlural = "BUILDINGS"
        self.down_relations = {
        }
        self.up_relations = {

        }



class CARS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.CARS_list)
        self.objectTitleSingular = "CAR"
        self.objectTitlePlural = "CARS"
        self.down_relations = {
        }
        self.up_relations = {

        }



class PEOPLE(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.PEOPLE_list)
        self.objectTitleSingular = "PEOPLE"
        self.objectTitlePlural = "PEOPLE"
        self.down_relations = {
        }
        self.up_relations = {

        }



class PLANTS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.PLANTS_list)
        self.objectTitleSingular = "PLANT"
        self.objectTitlePlural = "PLANTS"
        self.down_relations = {
        }
        self.up_relations = {

        }



class PARKS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.PARKS_list)
        self.objectTitleSingular = "PARK"
        self.objectTitlePlural = "PARKS"
        self.down_relations = {
        }
        self.up_relations = {

        }



class AIR(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.AIR_list)
        self.objectTitleSingular = "AIR"
        self.objectTitlePlural = "AIR"
        self.down_relations = {
        }
        self.up_relations = {

        }



class LIGHTS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.LIGHTS_list)
        self.objectTitleSingular = "LIGHT"
        self.objectTitlePlural = "LIGHTS"
        self.down_relations = {
        }
        self.up_relations = {

        }



class ANIMALS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.ANIMALS_list)
        self.objectTitleSingular = "ANIMAL"
        self.objectTitlePlural = "ANIMALS"
        self.down_relations = {
        }
        self.up_relations = {

        }



class WINDOWS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.WINDOWS_list)
        self.objectTitleSingular = "WINDOW"
        self.objectTitlePlural = "WINDOWS"
        self.down_relations = {
        }
        self.up_relations = {

        }



class SEATS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.SEATS_list)
        self.objectTitleSingular = "SEAT"
        self.objectTitlePlural = "SEATS"
        self.down_relations = {
        }
        self.up_relations = {

        }



class DOORS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.DOORS_list)
        self.objectTitleSingular = "DOOR"
        self.objectTitlePlural = "DOORS"
        self.down_relations = {
        }
        self.up_relations = {

        }



class FLOOR_MATS(object):
    def __init__(self):
        self.instanceTitle = random.choice(random_lists_data.FLOOR_MATS_list)
        self.objectTitleSingular = "FLOOR_MAT"
        self.objectTitlePlural = "FLOOR_MATS"
        self.down_relations = {
        }
        self.up_relations = {

        }










