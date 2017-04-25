# This is the introductory black box file for the project


import themeclass

"""
It becomes necessary to understand how a base ratio becomes connected to a clause.
For the purposes of this explanation, we define a clause as follows:
    A clause is a a list of terms that do not include addition or subtraction operators.




"""

class Clause(object):
    # assumption: name is a string, terms is a list of terms ... e.g. ['a', '*', 'b', '/', 'c']
    def __init__(self, name, terms, base_ratio):
        self.name = name
        self.terms = terms



# sample parse input






# # sample parse input
# input = "a*b+c*d+e"
# tree = []
#
# last_op = ""
# last_term = ""
#
# # basic parser found below, takes input and puts it into the 'tree'
# for i in range(0, len(input)):
#     term = input[i]
#
#     # if we receieve a term
#     if term >= 'a' and term <= 'z':
#         if last_term == '' and last_op == '':
#             last_term = term
#         elif last_term != '' and last_op != '':
#             tree.append((last_term, term, last_op))
#             last_term = ''
#             last_op = ''
#         else:
#             print("ERROR LINE 170?")
#     # if we receive an op
#     else:
#         if last_term == '' and last_op == '':
#             tree.append(term)
#         elif last_term != '' and last_op == '':
#             last_op = term
#         else:
#             print("ERROR LINE 178?")
# if last_term != "":
#     tree.append((last_term)