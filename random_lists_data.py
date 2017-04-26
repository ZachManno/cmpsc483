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
CONTAINERS_list = [
    'group',
    'collection',
    'assortment'
]

CONTAINERS_list_adj = [
            'colorful',
            'groovy',
            'boring'
        ]

#City has all of these things in it
#Topic to discuss: Cities can have animals, but also dogs and cats. But animals cant have dogs and cats, they are dogs and cats
#Just like a shop is a kind of building
CONTINENTS_list = [
    'Eastern Hemisphere',
    'Western Hemisphere'
]
CONTINENTS_list_adj = [
    'cold',
    'warm'
]

COUNTRIES_list = [
    'First-world country',
    'Third-world country'
]
COUNTRIES_list_adj = [
            'crowded',
            'developed'
]

STATES_list = [
    'Breadbasket state',
    'Northeastern state',
    'coastal state'
]
STATES_list_adj = [
        'industrial',
        'farming'
        ]

CITIES_list = [
    'utopia',
    'metropolis',
    'village',
    'town'
]
CITIES_list_adj = [
    'gleaming',
    'dirty',
    'clean',
    'crowded',
    'developed'
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
STREETS_list_adj = [
    'dirty',
    'clean',
    'crowded',
    'packed'
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
BUILDINGS_list_adj = [
    'modern',
    'rustic',
    'expensive',
    'grandoise'
]

CARS_list = [
    'sedan',
    'truck',
    'convertable',
    'minivan',
    'station wagon',
    'recreational vehicle'
]
CARS_list_adj = [
    'fast',
    'slow',
    'luxury',
    'powerful'
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
PEOPLE_list_adj = [
    'annoying',
    'smart',
    'arrogent',
    'kind',
    'pessimistic',
    'broke',
    'rich'
]

PLANTS_list = [
    'orchid',
    'daffodil',
    'geranium',
    'mum',
    'rose',
    'daisy',
    'violet'
]
PLANTS_list_adj = [
    'aquatic',
    'infected',
    'tall',
    'hardy',
    'rare',
    'potted',
    'pretty'
]

PARKS_list = [
    'national park',
    'playground',
    'amusement park',
    'skate park'
]
PARKS_list_adj = [
    'beautiful',
    'green',
    'popular',
    'spacious',
    'wooded'
]



LIGHTS_list = [
    'LED light',
    'CFL light'
]
LIGHTS_list_adj = [
    'bright',
    'shiny',
    'luminous',
    'dull'
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
    'Bolognese Dog',
    'Emperor Penguin',
    'Leopard',
    'Basenji Dog',
    'Australian Terrier',
    'Cuttlefish',
    'Asian Elephant',
    'Frilled Lizard',
    'Chihuahua',
    'Horseshoe Crab',
    'Howler Monkey',
    'Guppy',
    'Chesapeake Bay Retriever',
    'Barracuda',
    'Lion',
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
    'Jackal',
    'Deer',
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
    'Cockroach',
    'Antelope',
    'American Pit Bull Terrier',
    'Elephant Shrew',
    'American Staffordshire Terrier',
    'Leopard Seal',
    'Cross River Gorilla',
    'Fish'
]
ANIMALS_list_adj = [
    "fluffy",
    "furry",
    "silky",
    "loud",
    "lumbering",
    "hibernating",
    "shaggy",
    "tired"
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
WINDOWS_list_adj = [
    'small',
    'large',
    'stained',
    'dirty',
    'shattered',
    'latticed'
]

EATS_list = [

]

DOORS_list = [
    'sliding door',
    'framed door',
    'garage door',
    'bay door',
    'falcon wing door'
]
DOORS_list_adj = [
    'closed',
    'open',
    'heavy',
    'revolving',
    'golden',
    'hidden',
    'panelled'
]

##AREADY HAVE LIGHTS

##ALREADY HAVE PEOPLE
FLOOR_MATS_list = [
    'carpet floor mat',
    'plastic floor mat',
    'Anti-Fatigue Floor Mat',
    'Entrance Floor Mat',
    'Grease Resistant Mat',
]
FLOOR_MATS_list_adj = [
    'dirty',
    'clean',
    'sparkly',
    'pristine'
]

SIGNS_list = [
    'stop sign',
    'yield sign',
    'speed limit sign',
    'ped walking sign',
    'school zone sign',
]
SIGNS_list_adj = [
    'clean',
    'obnoxious',
    'informative',
    'boring',
    'funny',
    'whimsical',
    'enlightening'
]

TRASH_list = [
    'wrapper',
    'soda can',
    'crumbled paper',
    'diaper',
    'Potato chip bag',
    'Ziplock bag',
    'Bubble wrap',
    'Candy wrapper',
    'Food scrap',
    'Yard waste and leave',
    'Recyclable item',
    'Hazardous material',
]
TRASH_list_adj = [
    'dirty',
    'disgusting',
    'horrid',
    'wretched'
]

BASKETS_list = [
    'shopping basket',
    'all purpose basket',
    'wooden basket',
    'handwoven basket',
]
BASKETS_list_adj = [
    'woven',
    'fancy',
    'expensive',
    'cheap',
    'clean',
    'dirty'
]

FRUITS_list = [
    'Apple',
    'Apricot',
    'Avocado',
    'Banana',
    'Bilberry',
    'Blackberry',
    'Blueberry',
    'Boysenberry',
    'Cherry',
    'Cloudberry',
    'Coconut',
    'Cranberry',
    'Cucumber',
    'Dragonfruit',
    'Elderberry',
    'Feijoa',
    'Fig',
    'Goji berry',
    'Gooseberry',
    'Grape',
    'Raisin',
    'Grapefruit',
    'Guava',
    'Honeyberry',
    'Huckleberry',
    'Jackfruit',
    'Juniper berry',
    'Kiwifruit',
    'Kumquat',
    'Lemon',
    'Lime',
    'Mango',
    'Marionberry',
    'Melon',
    'Cantaloupe',
    'Honeydew',
    'Watermelon',
    'Miracle fruit',
    'Mulberry',
    'Nectarine',
    'Orange',
    'Blood orange',
    'Clementine',
    'Mandarine',
    'Tangerine',
    'Papaya',
    'Passionfruit',
    'Peach',
    'Pear',
    'Plum',
    'Prune',
    'Pineapple',
    'Pomegranate',
    'Purple mangosteen',
    'Quince',
    'Raspberry',
    'Salmonberry',
    'Salal berry',
    'Star fruit',
    'Strawberry',

]
FRUITS_list_adj = [
    'rotten',
    'succulent',
    'juicy',
    'ripe',
    'delicious'
]

SIDEWALKS_list = [
    'concrete sidewalk',
    'boardwalk',
]
SIDEWALKS_list_adj = [
    'concrete',
    'icey',
    'dirty',
    'snowy',
    'littered',
    'grassy',
    'muddy',
    'wide',
    'narrow',
    'busy',
    'slippery',
    'unpaved'
]

SEATS_list = [
    'chair',
    'cushion',
    'seat',
    'studio chair',
    'desk seat',
    'egg chair',
]
SEATS_list_adj = [
    'comfortable',
    'vacant',
    'cheap',
    'uncomfortable',
    'cushioned',
    'reserved'
]

ultimate_type_list = [
    "CONTINENTS",
    "COUNTRIES",
    "STATES",
    "CITIES",
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
    "BASKETS",
    "FRUITS",
    "SIDEWALKS"
]