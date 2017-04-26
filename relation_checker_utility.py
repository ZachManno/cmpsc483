import random_lists_data
import newthemeclass


def check():
    foundFlag = False
    for noun in random_lists_data.ultimate_type_list:
        print('noun = ' + noun)
        myclassobject = newthemeclass.str_to_class("newthemeclass", noun)
        print('--------------------------------------------------------------------------')
        #for each down relation the class object has:
        #check to make sure the corresponding up relation is found
        for key in myclassobject.down_relations:
            print('key = \"' + key +'\", list = ', str(myclassobject.down_relations[key]))
            print('===========================================================')
            #
            # The dictionary has a key of the type of down relation ('has' or etc)
            # And a value of a list of all Noun_objects corresponding to said type of down relation
            # Example. key = 'has', myclassobject.down_relations[key] = ['ROOMS','PLANTS','PEOPLE'].
            if hasattr(myclassobject, 'down_relations'):
                for item in myclassobject.down_relations[key]:
                    print("checking \"" + key + "\" key of " + "noun " +noun)
                    print('item = ' + item)
                    print('*************************')

                    class_testing = newthemeclass.str_to_class("newthemeclass", item)
                    if class_testing is None:
                        raise SystemError("CLASS + ",item + "DOES NOT EXIST")
                    if hasattr(class_testing, 'up_relations'):
                        for key2 in class_testing.up_relations:
                            print('key2 = \"' + key2 + '\" list = ', str(class_testing.up_relations[key2]))
                            print("++++++++++++++++++++++")
                            for noun2 in class_testing.up_relations[key2]:
                                print("key2 = " + key2 + ", noun2 = " + noun2)
                                if noun2 == myclassobject.objectTitlePlural:
                                    print("SUCCESS!\n   " + noun, key, item + "\n",item,key2,noun )
                                    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                    foundFlag = True
                        if not foundFlag:
                            raise SystemError("NO MATCH FOR NOUN " + item +',Parent = ' + noun)
                        else:
                            foundFlag = False

                            #dsfmdslfmsklfnlwenflewflnewlf


    print('/////////////////////////////////////////////////////////////////////////////////////////////////////////')
    foundFlag = False
    for noun in random_lists_data.ultimate_type_list:
        print('noun = ' + noun)
        myclassobject = newthemeclass.str_to_class("newthemeclass", noun)
        print('--------------------------------------------------------------------------')
        # for each down relation the class object has:
        # check to make sure the corresponding up relation is found
        for key in myclassobject.up_relations:
            print('key = \"' + key + '\", list = ', str(myclassobject.up_relations[key]))
            print('===========================================================')
            #
            # The dictionary has a key of the type of down relation ('has' or etc)
            # And a value of a list of all Noun_objects corresponding to said type of down relation
            # Example. key = 'has', myclassobject.down_relations[key] = ['ROOMS','PLANTS','PEOPLE'].
            if hasattr(myclassobject, 'up_relations'):
                for item in myclassobject.up_relations[key]:
                    print("checking \"" + key + "\" key of " + "noun " + noun)
                    print('item = ' + item)
                    print('*************************')

                    class_testing = newthemeclass.str_to_class("newthemeclass", item)
                    if class_testing is None:
                        raise SystemError("CLASS + ", item + "DOES NOT EXIST")
                    if hasattr(class_testing, 'down_relations'):
                        for key2 in class_testing.down_relations:
                            print('key2 = \"' + key2 + '\" list = ',
                                  str(class_testing.down_relations[key2]))
                            print("++++++++++++++++++++++")
                            for noun2 in class_testing.down_relations[key2]:
                                print("key2 = " + key2 + ", noun2 = " + noun2,"objectTitlePlural = " + myclassobject.objectTitlePlural)
                                if noun2 == myclassobject.objectTitlePlural:
                                    print("SUCCESS!\n   " + noun, key, item + "\n", item, key2,
                                          noun)
                                    print('~~~~~~~~~~~~~~~~~~~~~~~~~')
                                    foundFlag = True
                        if not foundFlag:
                            raise SystemError("NO MATCH FOR PARENT NOUN " + item + ',CHILD = ' + noun)
                        else:
                            foundFlag = False




check()