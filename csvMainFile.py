# csv reader's main menu
# will contain all the main menu options
# those options are executed by linking the main file with the function file

import time                         # importing time module
from csvFunctionFile import *       # importing csvFunctionFile
import csvReuseInputOutput as ci    # importing csvReuseInputOutput as ci

choice = 0            # choice is the choice, which will be specified by the user
# the program will exit when the option 3 is selected i.e. when choice becomes 3 the program will exit

while(choice != 3):
    cr.lineTime(sec=0.5)
    # calling lineTime fucntion                     # stopping the time for 0.5 seconds

    print('The CSV Reader'.center(150, ' '))       # printing the title on the center using the centre method

    cr.lineTime(sec=0.5)
    # calling lineTime fucntion                     # stopping the time for 0.5 seconds

    print('1. Create a new CSV')        # the first option which will create a new csv file

    print('2. More Options')            # the second option for more options

    print('3. Exit')                    # the third option for exiting the program

    cr.lineTime(sec=0.5)
    # calling lineTime fucntion                    # stopping the time for 0.5 seconds

    choice = ci.reuseInput()       # calling ci.reuseInput()

    cr.lineTime(sec=0.5)
    # calling lineTime fucntion                    # stopping the time for 0.5 seconds

    if(choice == 1):
        # if the user selected first option
        obj.createCSV()         # calling createCSV function

    elif(choice == 2):
        # if the user selected second option - More Option

        choice_moreOption = 0                 # choice_moreOption is the choice for option 2
        # more option will run until option 6 is not chosen

        while(choice_moreOption != 6):

            cr.lineTime(sec=0.5)

            print('More Option'.center(30, ' '))        # printing More option and aligining it

            cr.lineTime(sec=0.5)
            # calling lineTime fucntion              # stopping the time for 0.5 seconds

            print('1. Open CSV File')           # our first option

            print('2. Show All Saved Files')    # our second option

            print('3. Remove Saved Files')      # our third option

            print('4. Rename Saved Files')     # our fourth option

            print('5. Perform More Action')    # our fifth option

            print('6. Exit')                  # our sixth option

            choice_moreOption = ci.reuseInput()  # calling the ci.reuseInput function

            cr.lineTime(sec=0.5)
            # calling lineTime fucntion          # stopping the time for 0.5 seconds

            if(choice_moreOption == 1):
                # when option one is selected
                # this sub-option will include two options
                # 1. Display every content in the file and  2. Display the specific contents

                choice_openCSV = 0  # user will have to choose the option, it's for the Open CSV File
                # the option will exit when 3 option is chosen

                while(choice_openCSV != 3):

                    cr.lineTime(sec=0.5)

                    print('Open CSV File'.center(30, ' '))     # printing and aligning the title

                    cr.lineTime(sec=0.5)
                    # calling lineTime fucntion    # stopping the time for 0.5 seconds

                    print('1. Display Every Content of The File')  # our first option

                    print('2. Display Only The Specific Contents')  # our second option

                    print('3. Back')                              # our third option

                    choice_openCSV = ci.reuseInput()     # calling the funtion ci.reuseInput

                    cr.lineTime(sec=0.5)
                    # calling lineTime fucntion    # stopping the time for 0.5 seconds

                    if(choice_openCSV == 1):
                        # when option one is selected
                        obj.displayCSV(num=0)     # calling displayCSV(0) function

                    elif(choice_openCSV == 2):
                        # when option two is selected
                        obj.displayCSV(num=1)     # calling displayCSV(1) function

                    elif(choice_openCSV == 3):
                        # calling lineTime fucntion   # stopping the time for 0.5 seconds

                        break             # breaking the loop when option 3 is chosen, i.e. we get back to the more oprion

                    else:
                        cr.lineTime(sec=0.5)
                        # calling lineTime fucntion   # stopping the time for 0.5 seconds

                        print('Option Does Not Exist')

                        continue         # continue to input the value

            elif(choice_moreOption == 2):
                # when option two is selected
                obj.dispSavedFiles()    # calling dispSavedFiles

            elif(choice_moreOption == 3):
                # when the third option is selected
                # option for removing your csv files present in csvDocument directory
                # will include two Options
                # 1. remove specific files and 2. remove all files

                choice_removeFile = 0
                # the option will quit when option 3 is chosen

                while(choice_removeFile != 3):

                    cr.lineTime(sec=0.5)

                    print('Remove Saved Files'.center(30, ' '))   # printing and aligining the title

                    cr.lineTime(sec=0.5)
                    # calling lineTime fucntion          # stopping the time for 0.5 seconds

                    print('1. Remove Specific Files')  # our first option

                    print('2. Remove All Files')      # our second option

                    print('3. Back')                 # our third option

                    choice_removeFile = ci.reuseInput()   # calling ci.reuseInput option

                    if(choice_removeFile == 1):
                        # when option one is selected
                        obj.removeSpecificFiles()       # calling removeSpecificFiles function

                    elif(choice_removeFile == 2):
                        # when option two is selected
                        obj.removeAllFiles()            # calling removeAllFiles function

                    elif(choice_removeFile == 3):
                        # for exiting the loop
                        cr.lineTime(sec=0.5)
                        # calling lineTime fucntion       # stopping the time for 0.5 second
                        break

                    else:
                        cr.lineTime(sec=0.5)
                        # calling lineTime fucntion         # stopping the time for 0.5 seconds

                        print('Option Does Not Exist')

                        continue                # continue to ask for the input

            elif(choice_moreOption == 4):
                # when option 4 is selected
                obj.renameFiles()               # calling renameFiles function

            elif(choice_moreOption == 5):
                # when option 5 is selected

                choice_moreAction = 0        # option variable for more action
                # the option will exit when option 4 is chosen

                while(choice_moreAction != 4):

                    cr.lineTime(sec=0.5)

                    print('Perform More Action'.center(30, ' '))      # printing and aligning the title

                    cr.lineTime(sec=0.5)
                    # calling lineTime fucntion         # stopping the time for 0.5 seconds

                    print('1. Copy Content')                # our first option

                    print('2. Edit Content')                # our second option

                    print('3. Search Content')              # our third option

                    print('4. Properties')                 # our fourth option

                    print('5. Back')                       # our fifth option

                    choice_moreAction = ci.reuseInput()       # calling ci.reuseInput

                    cr.lineTime(sec=0.5)
                    # calling lineTime fucntion         # stopping the time for 0.5 seconds

                    if(choice_moreAction == 1):
                        # when option 1 is selected

                        choice_copyContent = 0      # option varaible for copy content
                        # the option will exit when option 3 is chosen

                        while(choice_copyContent != 3):

                            cr.lineTime(sec=0.5)

                            print('Copy Content'.center(30, ' '))    # printing and aligning the content

                            cr.lineTime(sec=0.5)
                            # calling lineTime fucntion               # stopping the time for 0.5 seconds

                            print('1. Copy All Content To Another File')       # option one

                            print('2. Copy Specific Content To Another File')  # option two

                            print('3. Back')                                   # option three

                            choice_copyContent = ci.reuseInput()           # calling ci.reuseInput()

                            if(choice_copyContent == 1):
                                # when option one is selected
                                obj.copyContent(0)          # calling copyContent function

                            elif(choice_copyContent == 2):
                                # when option two is selected
                                obj.copyContent(1)          # calling copyContent function

                            elif(choice_copyContent == 3):
                                break           # breaking when option 3 is chosen

                            else:
                                print('Option Does Not Exist')
                                continue        # continue for asking the input

                    elif(choice_moreAction == 2):
                        # when option 2 is selected

                        choice_editContent = 0         # option varaible for edit content
                        # the option will exit when option 4 is chosen

                        while(choice_editContent != 4):

                            cr.lineTime(sec=0.5)

                            print('Edit Content'.center(30, ' '))           # printing and aligning the content

                            cr.lineTime(sec=0.5)
                            # calling lineTime fucntion                 # stopping the time for 0.5 seconds

                            print('1. Add A New Line')              # option one

                            print('2. Update The Information')    # option two

                            print('3. Delete The Existing Line')              # option three

                            print('4. Back')                                 # option four

                            choice_editContent = ci.reuseInput()     # calling ci.reuseInput()

                            cr.lineTime(sec=0.5)
                            # calling lineTime fucntion                 # stopping the time for 0.5 seconds

                            if(choice_editContent == 1):
                                # when option 1 is selected

                                choice_addInfo = 0              # option variable
                                # the option will exit when the choice_addInfo becomes 4

                                while(choice_addInfo != 4):

                                    cr.lineTime(sec=0.5)

                                    print('Add A New Line'.center(30, ' '))         # printing and aligning the content

                                    cr.lineTime(sec=0.5)
                                    # calling lineTime fucntion                        # stopping the time for 0.5 seconds

                                    print('1. Add Line At Front Position')          # option one

                                    print('2. Add Line In Between')                 # option two

                                    print('3. Add Line At Rare Position')           # option three

                                    print('4. Back')                                # option four

                                    cr.lineTime(sec=0.5)
                                    # calling lineTime fucntion                     # stopping the time for 0.5 seconds

                                    choice_addInfo = ci.reuseInput()       # calling ci.reuseInput()

                                    cr.lineTime(sec=0.5)
                                    # calling lineTime fucntion                     # stopping the time for 0.5 seconds

                                    if(choice_addInfo == 1):
                                        # when option one is selected
                                        obj.addAtFront()                # calling addAtFront function

                                    elif(choice_addInfo == 2):
                                        # when option two is selected
                                        obj.addInBtw()                  # calling addInBtw function

                                    elif(choice_addInfo == 3):
                                        # when option three is selected
                                        obj.addAtRare()                 # calling addAtRare function

                                    elif(choice_addInfo == 4):
                                        # when option four is selected
                                        break               # breaking the loop when option 4 is selected

                                    else:
                                        print('Option Does Not Exits')
                                        continue            # continue to ask for the input

                            elif(choice_editContent == 2):
                                # when option 2 is selected

                                choice_updateInfo = 0       # option varaible for update information
                                # the option will exit when the option 3 is chosen

                                while(choice_updateInfo != 3):

                                    cr.lineTime(sec=0.5)

                                    print('Update The Information'.center(30, ' '))  # printing and aligning the title

                                    cr.lineTime(sec=0.5)
                                    # calling lineTime fucntion        # stopping the time for 0.5 seconds

                                    print('1. Update The Whole Line')     # option 1

                                    print('2. Update The Specific Column')  # option 2

                                    print('3. Back')                      # option 3

                                    choice_updateInfo = ci.reuseInput()      # calling ci.reuseInput()

                                    cr.lineTime(sec=0.5)
                                    # calling lineTime fucntion      # stopping the time for 0.5 seconds

                                    if(choice_updateInfo == 1):
                                        # when option one is selected
                                        obj.updateLine()             # calling updateLine function

                                    elif(choice_updateInfo == 2):
                                        # when option two is selected
                                        obj.UpdateSpecific()         # calling UpdateSpecific function

                                    elif(choice_updateInfo == 3):
                                        # when option three is selected
                                        break          # exiting the loop, comming back from the option

                                    else:
                                        print('Option Does Not Exist')
                                        continue      # continue to ask the input

                            elif(choice_editContent == 3):
                                # when option 3 is selected
                                obj.delCsvLine()      # calling delCsvLine function

                            elif(choice_editContent == 4):
                                break               # breaking the loop when option 4 is selected

                            else:
                                print('Option Does Not Exist')
                                continue            # continue to ask the input

                    elif(choice_moreAction == 3):
                        # when option 3 is selected
                        obj.searchCsvFile()         # calling searchCsvFile function

                    elif(choice_moreAction == 4):
                        # when option 4 is selected
                        obj.propertyCsvFile()       # calling propertyCsvFile function

                    elif(choice_moreAction == 5):
                        break               # breaking the loop when option 5 is chosen

                    else:
                        print('Option Does Not Exist')
                        continue            # continue to ask for the input

            elif(choice_moreOption == 6):
                cr.lineTime(sec=0.5)
                # calling lineTime fucntion              # stopping the time for 0.5 seconds

                break             # breaking the loop when sixth option is chosen

            else:
                cr.lineTime(sec=0.5)
                # calling lineTime fucntion             # stopping the time for 0.5 seconds

                print('Option Does Not Exist')

                continue        # continue to ask for the input

    elif(choice == 3):
        cr.lineTime(sec=0.5)
        # calling lineTime fucntion                    # stopping the time for 0.5 seconds

        break                  # breaking the loop, the whole program, when third option is chosen

    else:
        cr.lineTime(sec=0.5)
        # calling lineTime fucntion                    # stopping the time for 0.5 seconds

        print('Option Does Not Exist')

        continue              # continue to ask for the input

# the end of the program
# Programmed By :- Slothfulwave@612
