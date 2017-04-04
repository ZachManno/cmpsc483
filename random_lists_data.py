NAMES = [
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

VERBS = [
    'has',
    'have',
    'goes',
    'performs',
    'does',
    'are'
]

NOUNS = [
    'dog',
    'cat',
    'ball',
    'dress',
    'pencil',
    'apple',
    'football',
    'shoe',
    'computer'
]

UNITS = [
    'dollar',
    'cent',
    'gallon',
    'cup',
    'meter'
]

CONVERSIONS = [
    ['mile','yards',1760],
    ['mile','feet',5280],
    ['mile','inches',63360],
    ['yard','feet',3],
    ['foot','inches',12],
    ['year','days',365],
    ['year','months',12],
    ['day','hours',24],
    ['hour','minutes',60],
    ['gallon','quarts',4]
]


#################################################################

#City has all of these things in it
#Topic to discuss: Cities can have animals, but also dogs and cats. But animals cant have dogs and cats, they are dogs and cats
#Just like a shop is a kind of building
CITY = [
    'zip codes'
    'streets',
    'buildings',
    'cars',
    'people',
    'plants',
    'parks',
    'air',
    'lights',
    'animals',
]

ZIP_CODES = [
    'burrows'
    'buildings'
]

#A lot of these things loop in circles. when searching need to make sure we dont use something already used
#City has streets and buildings and people. Streets and buildings both have people. Streets have buildings.
STREETS = [
    'people',
    'signs',
    'cars',
    'buildings',
    'trash',
    'lights',
    'sidewalk'
]

BUILDINGS = [
    'floors',
    'rooms',
    'stairs',
    'people',
    'lights',
    'computers',
    'doors',
    'windows'
]

CARS = [
    'people',
    'windows',
    'seats',
    'doors',
    'lights',
    'floor mats'
]

#People can have clothes on them but that is different
PEOPLE = [
    'organs'
    'eyes'
    'skin'
    'limbs'
    'fingers'
    'toes'
    'bones'
    'teeth'
]

PLANTS = [
    'leaves',
    'petals',
    'seeds',
    'roots',
    'branches'
]


PARKS = [
    'plants'
    'animals'
    'people'
    'lights'
    'jungle gyms'
]

#might want to just eliminate air (kind of weird)
#wouldnt make sense to say air has animals, but air does have birds. Maybe use alternative name for animal here
AIR = [
    'birds'
    'oxygen'
    'nitrogen'
    'dust'
]


LIGHTS = [
    'batteries'
    'wires'
]

#people are animals but differnt. Can be a "has" relationship and an "are" relationship. Or maybe "are" relationship doesnt
#even help the problem at all
ANIMALS = [
    'claws'
    'fur'
    'tails'
    'paws'
]


############ TENTATIVE FIRST LEVEL DONE. NOW ONTO SECOND LEVEL ################


#Example for second level:
#CAR HAS:
WINDOWS = [
    'glass',
    'dust'

]

SEATS = [
    'dust'
]

DOORS = [
    'handles',
    'speakers',
    'windows',
    'locks',
]

##ALREADY HAVE LIGHTS

##ALREADY HAVE PEOPLE

FLOOR_MATS = [
    'ridges'
]


