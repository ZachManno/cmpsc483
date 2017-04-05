import random

NAMES_list = [
'Rodrigo',
'Miles',
'Marisa',
'Zach',
'Rodney',
'Steve',
'Josh',
'Kathy',
'Daren',
'Rubye',
'Sean',
'Delcie',
'Carley',
'Lenard',
'Jules',
'Penney',
'Leandra',
'Jama',
'Melda',
'Cassandra',
'Jettie',
'Angla',
'Jeanne',
'Garnet',
'Rachelle',
'Palma',
'Cinthia',
'Dina',
'Devorah',
'Samual',
'Ike',
'Jeremiah',
'June',
'Belva',
'Yuonne',
'Mauricio',
'Chae',
'Serafina' ,
'Alane',
'Lizabeth',
'Delena',
'Beaulah',
'Lucille',
'Agustina',
'Charley',
'Isabella',
'Deanne',
'Joaquina',
'Sherry',
'Jeanmarie',
'Ronny',
'Azzie',
'Erlene',
'Candy',
'Tashia'
]


VERBS_list = [
    'has',
    'have',
    'goes',
    'performs',
    'does',
    'are'
]



###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################
###############################################################################################

#City has all of these things in it
#Topic to discuss: Cities can have animals, but also dogs and cats. But animals cant have dogs and cats, they are dogs and cats
#Just like a shop is a kind of building




CITY_list = [
    ['utopia'],
    ['metropolis','metropoli'],
    ['village'],
    ['town']
]

#A lot of these things loop in circles. when searching need to make sure we dont use something already used
#City has streets and buildings and people. Streets and buildings both have people. Streets have buildings.
STREETS_list = [
    ['avenue'],
    ['boulevard'],
    ['alley'],
    ['cul-de-sac'],
    ['highway']

]

BUILDINGS_list = [
    ['shop'],
    ['hotel'],
    ['mall'],
    ['skyscraper'],
    ['hospital'],
    ['apartment'],
    ['townhouse'],
    ['library','libraries']

]

CARS_list = [
    ['sedan'],
    ['truck'],
    ['convertable'],
    ['minivan'],
    ['station wagon'],
    ['recreational vehicle']
]

#People can have clothes on them but that is different
PEOPLE_list = [
    ['computer scientist'],
    ['body builder'],
    ['homewrecker'],
    ['plumber'],
    ['janitor']
]

PLANTS_list = [
    ['orchid'],
    ['daffodil'],
    ['geranium'],
    ['mum']
]


PARKS_list = [
    ['national park'],
    ['playground'],
    ['amusement park'],
    ['skate park']
]



LIGHTS_list = [
    ['LED light'],
    ['CFL light']
]

#people are animals but differnt. Can be a "has" relationship and an "are" relationship. Or maybe "are" relationship doesnt
#even help the problem at all
ANIMALS_list = [
    ['monkey'],
    ['cat'],
    ['dog'],
    ['bear'],
    ['rhino'],
    ['snake']

]


############ TENTATIVE FIRST LEVEL DONE. NOW ONTO SECOND LEVEL ################


#Example for second level:
#CAR HAS:
WINDOWS_list = [
    #building window list
    ['bay window'],
    ['awning window'],
    ['sliding window']
    #car window list

]

SEATS_list = [

]

DOORS_list = [
    ['sliding door'],
    ['framed door']
]

##ALREADY HAVE LIGHTS

##ALREADY HAVE PEOPLE

FLOOR_MATS_list = [
    ['carpet floor mat'],
    ['plastic floor mat']
]

SIGNS_list = [
    ['stop sign'],
    ['yield sign'],
    ['speed limit sign']
]

TRASH_list = [
    ['wrapper'],
    ['soda can'],
    ['crumbled paper']
]

ultimate_type_list = [
    "CITY",
    "ZIP_CODES",
    "STREETS",
    "BUILDINGS",
    "CARS",
    "PEOPLE",
    "PLANTS",
    "PARKS",
    "LIGHTS",
    "ANIMALS",
    "WINDOWS",
    "SEATS",
    "DOORS",
    "FLOOR_MATS",
    "SIGNS",
    "TRASH",
    "SIDEWALKS"
]


