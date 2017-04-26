import random_lists_data
import newthemeclass


def check(verbose):
    foundFlag = False
    if verbose:
        print()
    for noun in random_lists_data.ultimate_type_list:
        if verbose:
            print()
            print('======================================================================================================================================')
            print('Testing noun = ' + noun + ' for the existance of all down relations by iterating through downverbs:')
        myclassobject = newthemeclass.str_to_class("newthemeclass", noun)
        #for each down relation the class object has:
        #check to make sure the corresponding up relation is found
        for key in myclassobject.down_relations:
            if verbose:
                print(' ______________________________________________________________________________________________________')
                print(' downverb = \"' + key +'\", list = ', str(myclassobject.down_relations[key]))
            #
            # The dictionary has a key of the type of down relation ('has' or etc)
            # And a value of a list of all Noun_objects corresponding to said type of down relation
            # Example. key = 'has', myclassobject.down_relations[key] = ['ROOMS','PLANTS','PEOPLE'].
            if hasattr(myclassobject, 'down_relations'):
                for item in myclassobject.down_relations[key]:
                    if verbose:
                        print('     ************************************************************************************')
                        print('     item in list: ' + item)

                    class_testing = newthemeclass.str_to_class("newthemeclass", item)
                    if class_testing is None:
                        raise SystemError("CLASS + ",item + "DOES NOT EXIST")
                    if hasattr(class_testing, 'up_relations'):
                        for key2 in class_testing.up_relations:
                            if verbose:
                                print("         ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print('         upverb= \"' + key2 + '\" list = ', str(class_testing.up_relations[key2]))
                            for noun2 in class_testing.up_relations[key2]:
                                if verbose:
                                    print("             noun comparing = " + noun2)
                                if noun2 == myclassobject.objectTitlePlural:
                                    if verbose:
                                        print('                 ~~~~~~~~~~~~~~~~~~~~~~~~~')
                                        print("                 ~SUCCESS!")
                                        print("                 ~" + noun, key, item)
                                        print("                 ~" + item, key2, noun)
                                        print('                 ~~~~~~~~~~~~~~~~~~~~~~~~~')
                                    foundFlag = True
                            if verbose:
                                print("         ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        if not foundFlag:
                            raise SystemError("NO MATCH FOR NOUN " + item +',Parent = ' + noun)
                        else:
                            foundFlag = False
                if verbose:
                    print('     *************************************************************************************')
            if verbose:
                print(' ______________________________________________________________________________________________________')
        if verbose:
            print('\nFinished testing noun: '+noun)
            print('======================================================================================================================================\n')

                            #dsfmdslfmsklfnlwenflewflnewlf

    if verbose:
        print('\n\n/////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('/////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('/////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')
        print('////////  FINISHED DOWN RELATION TO UP RELATION CHECK. STARTING UP RELATION TO DOWN RELATION CHECK  /////////\n')
        print('/////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('/////////////////////////////////////////////////////////////////////////////////////////////////////////////')
        print('/////////////////////////////////////////////////////////////////////////////////////////////////////////////\n\n\n')


    foundFlag = False
    for noun in random_lists_data.ultimate_type_list:
        if verbose:
            print()
            print('======================================================================================================================================')
            print('Testing noun = ' + noun + ' for the existance of all up relations by iterating through upverbs:')
        myclassobject = newthemeclass.str_to_class("newthemeclass", noun)
        # for each down relation the class object has:
        # check to make sure the corresponding up relation is found
        for key in myclassobject.up_relations:
            if verbose:
                print(' ______________________________________________________________________________________________________')
                print(' upverb = \"' + key +'\", list = ', str(myclassobject.up_relations[key]))
            #
            # The dictionary has a key of the type of down relation ('has' or etc)
            # And a value of a list of all Noun_objects corresponding to said type of down relation
            # Example. key = 'has', myclassobject.down_relations[key] = ['ROOMS','PLANTS','PEOPLE'].
            if hasattr(myclassobject, 'up_relations'):
                for item in myclassobject.up_relations[key]:
                    if verbose:
                        print('     ************************************************************************************')
                        print('     item in list: ' + item)
                    class_testing = newthemeclass.str_to_class("newthemeclass", item)
                    if class_testing is None:
                        raise SystemError("CLASS + ", item + "DOES NOT EXIST")
                    if hasattr(class_testing, 'down_relations'):
                        for key2 in class_testing.down_relations:
                            if verbose:
                                print("         ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                                print('         downverb= \"' + key2 + '\" list = ', str(class_testing.down_relations[key2]))
                            for noun2 in class_testing.down_relations[key2]:
                                if verbose:
                                    print("             noun comparing = " + noun2)
                                if noun2 == myclassobject.objectTitlePlural:
                                    if verbose:
                                        print('                 ~~~~~~~~~~~~~~~~~~~~~~~~~')
                                        print("                 ~SUCCESS!")
                                        print("                 ~" + noun, key, item)
                                        print("                 ~" + item, key2, noun)
                                        print('                 ~~~~~~~~~~~~~~~~~~~~~~~~~')
                                    foundFlag = True
                            if verbose:
                                print("         ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
                        if not foundFlag:
                            raise SystemError("NO MATCH FOR PARENT NOUN " + item + ',CHILD = ' + noun)
                        else:
                            foundFlag = False
                if verbose:
                    print('     *************************************************************************************')
            if verbose:
                print(' ______________________________________________________________________________________________________')
        if verbose:
            print('\nFinished testing noun: ' + noun)
            print('======================================================================================================================================\n')




check(False)