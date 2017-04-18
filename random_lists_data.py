import random
import inflect

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
    'utopia',
    'metropolis',
    'village',
    'town'
]

#A lot of these things loop in circles. when searching need to make sure we dont use something already used
#City has streets and buildings and people. Streets and buildings both have people. Streets have buildings.
STREETS_list = [
    'avenue',
    'boulevard',
    'alley',
    'cul-de-sac',
    'highway'

]

BUILDINGS_list = [
    'shop',
    'hotel',
    'mall',
    'skyscraper',
    'hospital',
    'apartment',
    'townhouse',
    'library'

]

CARS_list = [
    'sedan',
    'truck',
    'convertable',
    'minivan',
    'station wagon',
    'recreational vehicle'
]

#People can have clothes on them but that is different
PEOPLE_list = [
    'Professor',
    'Teacher',
    'Clergy',
    'Philosopher',
    'Anesthesiologist',
    'Audiologist',
    'Chiropractor',
    'Dentist',
    'Dietitian',
    'Nurse',
    'Occupational therapist',
    'Pharmacist',
    'Operating Department Practitioner',
    'Optometrist',
    'Pharmacist',
    'Physical therapist',
    'Physician',
    'Podiatrist',
    'Psychologist',
    'Radiographer',
    'Radiotherapist',
    'Speech-language pathologist',
    'Surgeon',
    'Veterinarian',
    'Accountant',
    'Actuarie',
    'Architect',
    'Engineer',
    'Linguistic',
    'Translator',
    'Interpreter',
    'Surveyor',
    'Urban Planner',
    'Air traffic controller',
    'Aircraft pilot',
    'Sea captain',
    'Lawyer',
    'Social Worker',
    'Health inspector',
    'Park ranger',
    'Police officer',
    'Military officer',
    'Scientist',
    'Astronomer',
    'Biologist',
    'Botanist',
    'Ecologist',
    'Geneticist',
    'Immunologist',
    'Paleontologist',
    'Pharmacologist',
    'Virologist',
    'Zoologist',
    'Chemist',
    'Geologist',
    'Meteorologist',
    'Neuroscientist',
    'Oceanographer',
    'Physicist',
    'Computer Scientist'
]

PLANTS_list = [
    'orchid',
    'daffodil',
    'geranium',
    'mum'
]


PARKS_list = [
    'national park',
    'playground',
    'amusement park',
    'skate park'
]



LIGHTS_list = [
    'LED light',
    'CFL light'
]

#people are animals but differnt. Can be a "has" relationship and an "are" relationship. Or maybe "are" relationship doesnt
#even help the problem at all
ANIMALS_list = [
    'cat',
    'dog',
    'bear',
    'rhino',
    'elephant',
    'Jack Russel',
    'Beetle',
    'Cavalier King Charles Spaniel',
    'Entlebucher Mountain Dog',
    'Bengal Tiger',
    'Black Bear',
    'Lemming',
    'African Bush Elephant',
    'Common Frog',
    'Coati',
    'Cesky Fousek',
    'Bolognese Dog',
    'Echidna',
    'Emperor Penguin',
    'Dugong',
    'Leopard',
    'Basenji Dog',
    'Australian Terrier',
    'Cuttlefish',
    'Asian Elephant',
    'Frilled Lizard',
    'Chihuahua',
    'Horseshoe Crab',
    'Howler Monkey',
    'Alpine Dachsbracke',
    'Guppy',
    'Chesapeake Bay Retriever',
    'Caiman',
    'Barracuda',
    'Fishing Cat',
    'Lion',
    'Birman',
    'Border Terrier',
    'Bottle Nosed Dolphin',
    'African Tree Toad',
    'English Cocker Spaniel',
    'Field Spaniel',
    'American Cocker Spaniel',
    'Giraffe',
    'Eskimo Dog',
    'Great Dane',
    'Bulldog',
    'Chinstrap Penguin',
    'Boston Terrier',
    'Greyhound',
    'Hyena',
    'Dusky Dolphin',
    'Guinea Fowl',
    'Arctic Wolf',
    'Dalmatian',
    'Goose', 'Geese',
    'Baboon',
    'Dunker',
    'Jackal',
    'Deer', 'Deer',
    'Bumble Bee',
    'Boxer Dog',
    'Great White Shark',
    'African Forest Elephant',
    'Donkey',
    'Asiatic Black Bear',
    'Blue Lacy Dog',
    'Appenzeller Dog',
    'Buffalo',
    'African Civet',
    'Bedlington Terrier',
    'Lynx',
    'Golden Retriever',
    'Barn Owl',
    'Airedale Terrier',
    'Highland Cattle',
    'Dolphin',
    'Cockroach', 'Cockroaches',
    'Antelope',
    'American Pit Bull Terrier',
    'Elephant Shrew',
    'American Staffordshire Terrier',
    'Leopard Seal',
    'Cross River Gorilla',
    'Fish'
]



############ TENTATIVE FIRST LEVEL DONE. NOW ONTO SECOND LEVEL ################


#Example for second level:
#CAR HAS:
WINDOWS_list = [
    #building window list
    'bay window',
    'awning window',
    'sliding window',
    'prison cell window'
    #car window list

]

EATS_list = [

]

DOORS_list = [
    'sliding door',
   'framed door'
]

##AREADY HAVE LIGHTS

##ALREADY HAVE PEOPLE
FLOOR_MATS_list = [
    'carpet floor mat',
    'plastic floor mat'
]

SIGNS_list = [
    'stop sign',
    'yield sign',
    'speed limit sign'
]

TRASH_list = [
    'wrapper',
    'soda can',
    'crumbled paper',
    'diaper',
    'Potato chip bag',
    'Ziplock bag',
    'Bubble wra',
    'Candy wrapper',
    'Food scrap',
    'Yard waste and leave',
    'Recyclable item',
    'Hazardous material',
]

ultimate_type_list = [
    "CITY",
    # "ZIP_CODES",
    "STREETS",
    "BUILDINGS",
    "CARS",
    "PEOPLE",
    "PLANTS",
    "PARKS",
    "LIGHTS",
    "ANIMALS",
    "WINDOWS",
    # "SEATS",
    "DOORS",
    "FLOOR_MATS",
    "SIGNS",
    "TRASH",
    # "SIDEWALKS"
]

#Examples
print("DEMO OF LIBRARY\n----------------------")
targets = ["cat", "woman", "exam", "sneaker", "thief", "tesla coil", "printer", "goose", "geese"]
p = inflect.engine()
for target in targets:
    print("The plural of ", target, " is ", p.plural(target))

###_____________ Articles ________________###
#Did you want a dog or a cat or an orange (p.a and p.an are the exact same function, used for readability)
print("Did you want ", p.a('dog'), " or ", p.an('cat'), "or", p.a('orange'))

#two cats
print(p.no("cat",2))

#two cats
print("2",p.plural("cat"))

#a cat
print(p.a("cat"))

#I saw 3 dogs
print("I saw ", p.no('dog',3))

#conditional plural (1=singular, greater than 1 = plural)
print("I saw", '2', p.plural("cat",2))
print("I saw", '1', p.plural("cat",1))

###_____________ Number to words ________________###
print(p.number_to_words(1234567))

#Full sentences
#NOTE: PLURALS BASED OFF THE PREVIOUS P.NUM CALL

#3 errors were detected. These errors were fatal
print(p.num(3), p.plural_noun(" error"), p.plural_verb(" was"), " detected.")
print(p.plural_adj("This"), p.plural_noun(" error"), p.plural_verb(" was"), "fatal.")


#1 error was detected. This error was fatal
print(p.num(1), p.plural_noun(" error"), p.plural_verb(" was"), " detected.")
print(p.plural_adj("This"), p.plural_noun(" error"), p.plural_verb(" was"), "fatal.")

#3 errors were detected. This error was fatal
print(p.num(3), p.plural_noun(" error"), p.plural_verb(" was"), " detected.")
p.num(1)
print(p.plural_adj("This"), p.plural_noun(" error"), p.plural_verb(" was"), "fatal.")