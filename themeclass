import math

# This class provides the detail of a "unit"
# For example, it could describe a unit of length
# class Unit:

# This class provides the details and functionality of the shape of a theme class
# It is then subclassed into the specific shape that it is
# For example, a car would be a rectangular prism
# Required functions:
#   volume:         returns the volume of the shape
#   surfaca_area:   returns the surface area of the shape
class Shape(object):
    RECTANGULAR_PRISM = 0
    SPHERE = 1
    CYLINDER = 2

    SHAPE_NAMES = { RECTANGULAR_PRISM: "Rectangular Prism", SPHERE: "Sphere", CYLINDER: "Cylinder" }

    def __init__(self, shape):
        self.shape = shape
        self.name = self.SHAPE_NAMES[shape]

# These are all extensions of the shape class
class Rectnagular_prism(Shape):
    def __init__(self, length, width, height):
        super(Rectnagular_prism,self).__init__(self.RECTANGULAR_PRISM)
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def surface_area(self):
        return 2 * (self.width * self.height + self.width * self.length + self.length * self.height)
class Sphere(Shape):
    def __init__(self, radius):
        super(Sphere, self).__init__(self.SPHERE)
        self.radius = radius

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

    def surface_area(self):
        return 4 * math.pi * self.radius ** 2
class Cylinder(Shape):
    def __index__(self, radius, height):
        super(Cylinder,self).__init__(self.CYLINDER)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * self.height


# This is the UNIT class, it specifies the details and functionality of a unit of measurement
# Some examples include, money, length, time ... these are all UNITs
class Unit(object):
    MONEY = 0
    LENGTH = 1
    TIME = 2

    UNIT_NAMES = { MONEY: "Money", LENGTH: "Length", TIME: "Time" }

    def __init__(self, unit):
        self.CONVERSION = {}
        self.unit = unit


# This is the LENGTH class, it extends the UNIT class
# base unit: meter
class Length(Unit):
    CONVERSION = { "meter": 1, "decimeter": 10, "centimeter": 100, "millimeter": 1000, "kilometer": 0.001 }

    def __init__(self):
        super(Length,self).__init__(self.LENGTH)

# This is the TIME class, it extends the UNIT class
# base unit: second
class Time(Unit):
    CONVERSION = { "second": 1 , "minute": 1/60, "hour": 1/3600, "day": 1/86400, "week": 1/604800 }

    def __init__(self):
        super(Time,self).__init__(self.Time)

# This is the MONEY class, it extends the UNIT class
# base unit: dollar
class Money(Unit):
    CONVERSION = { "dollar": 1, "cent": 1/100 }

    def __init__(self):
        super(Money,self).__init__(self.Money)

# This is the AREA class, it extends the UNIT class
# Base unit: meters squared
# TODO








class Theme(object):
    # initialization function for the theme class
    # argument:     names are all possible names for the theme class, names[0] is considered the official name of the class; example: [car, sedan, truck]
    # argument:     the shape is the shape of the theme class in quesiton, for example a car is a rectangular prism
    # argument:     the ratios argument is a list of ratios that are relevant to the theme class, for example a car might have: money:distance, distance:time
    #               these ratios are passed as a LIST of TUPLES, where (money, time) would indicate money : time
    #               the tuple contains two UNIT objects; unit objects are defined above
    #               thus, the ratios list should appear formatted as follows: [ (UNIT, UNIT), (UNIT, UNIT), (UNIT, UNIT) ... (UNIT, UNIT) ]





    def __init__(self, names, shape, ratios):
        self.names = names
        self.shape = shape
        self.ratios = ratios





















