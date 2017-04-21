import inflect
import newthemeclass



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

print("------------")
print("Parent relation demo:")
b1 = newthemeclass.BUILDINGS()
parentRelation1 = b1.getParentRelation()
#parentRelation1 has:
#       parentNoun object (parentRelation1.parent)
#       childNoun object  (parentRelation1.child)
#       downVerb string   (parentRelation1.downVerb)
#       upVerb string     (parentRelation1.upVerb)
print(parentRelation1.upVerb)
print(parentRelation1.parent.objectTitleSingular)