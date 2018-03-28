# this file is for function using input

import csvExceptionFile as ce       # importing csvExceptionFile as ce
import csvReuse as cr               # importing csvReuse as cr
import csv                            # importing csv module
import os                             # importing os module
import time                           # importing time module
import sys                            # importing sys module
import logging                        # importing logging module


def reuseInput():
    # will reuse the function whenever we ask for option input

    while True:
        # try-except clause

        try:
            print()
            time.sleep(0.5)      # stopping the time for 0.5 seconds

            x = int(input('Enter The Option Number :- ').strip())  # to input the choice

            break               # breaking when the input is valid

        except ValueError:
            # when vaue error is caught
            print()
            time.sleep(0.5)     # stopping the time for 0.5 seconds

            print('Invalid Input')

    return(x)


def enterName(num):
    # this function is for entering name of the file
    # if num = 0 then the name will be entered for the new file which is being created
    # if num = 1 then then name will be entered for renaming of the file

    invalid_names = ['~', '#', '%', '*', '{', '}', '\\', ':', '<', '>', '?', '/', '+', '|', '"']
    # this is the list of the character that cannot be used while creating a folder or file

    filePresent = os.listdir()
    # appending all the file names to filePresent list

    while True:
        # try-except clause
        try:
            if(num == 0):
                x = input('Enter The Name of CSV File :- ').strip()          # to be entered by the user, CSV file name

            if(num == 1):
                x = input('Enter New Name for CSV File :- ').strip()          # to be entered by the user, CSV file name

            x += '.csv'         # adding .csv to the name of the file

            logging.info(f'File name entered as :- {x}')
            # using logging.info

            for i in invalid_names:
                if i in x:
                    raise(ce.filenameException)
            # raising fileException as the name of the file entered is not valid

            for i in filePresent:
                if(i == x):
                    raise(ce.morethanoneException)
            # raising morethanoneException as file is already there in the directory

            break         # breaking the clause if the name is valid and meet the criteria

        except ce.filenameException:
            # if fileException is caught
            logging.info(f'File Name Not Valid')       # using loging.info
            print('File Name Not Valid')
            cr.lineTime(sec=0.5)       # calling lineTime function

        except ce.morethanoneException:
            # if morethanoneException is caught
            logging.info(f'File With {x} Already Present')         # using logging.info
            print(f'File With {x} Already Present')
            cr.lineTime(sec=0.5)      # calling lineTime function

        except ValueError:
            # if value error is caught
            logging.info('Invalid Input')            # using logging.info
            print('Invalid Input')
            cr.lineTime(sec=0.5)

    return(x)


def openSys():
    # printing down 'Opening Your File' in interactive way

    for i in range(6):
        sys.stdout.write("\r")
        sys.stdout.write('Opening Your File' + '.' * i)    # using stdout to print the message in an interactive way
        sys.stdout.flush()                                  # using the flush function
        time.sleep(0.5)                # stopping the time for 0.5 seconds
    sys.stdout.write("\r")
    sys.stdout.write('                                              \n')


def totalColumn():
    # entering down total number of columns

    while True:
        # try-except clause
        try:
            x = int(input('Enter Total Number of Column :- '))    # user will enter total number of column required

            logging.info(f'Total Number of Column Entered :- {x}')       # using logging.info

            break                 # breaking when input is valid

        except ValueError:
            # if value error is caught
            cr.lineTime(sec=0.5)    # calling lineTime function
            logging.info('Invalid Input')    # using logging.info
            print('Invalid Input')
            cr.lineTime(sec=0.5)        # calling lineTime funtion

    return(x)


def totalLines():
    # entering dowm total number of lines

    while True:
        # try-except clause
        try:
            x = int(input('Enter Total Lines To Be Added :- ').strip())

            logging.info(f'Number of lines to be added :- {x}')       # using logging.info

            break       # breaking when the input is valid

        except ValueError:
            # if value error is caught
            logging.info('Invalid Input')                  # using logging.info
            cr.lineTime(sec=0.5)      # calling lineTime function
            print('Invalid Input')
            cr.lineTime(sec=0.5)      # calling lineTime function

    return(x)


def indexFileNumber(num, l):
    # for chossing the file name using their indexes
    # if num = 0 then it is for opening
    # if num = 1 then it is for removing
    # if num = 2 then it is for renaming

    while True:
        # try-except clause
        try:
            if(num == 0):
                x = int(input('Enter The Index Number of The File To Be Opened :- ').strip())
                # inputtting the file index to be opened

            elif(num == 1):
                x = int(input('Enter The Index Number of The File To Be Removed :- ').strip())
                # inputtting the file index to be opened

            elif(num == 2):
                x = int(input('Enter The Index Number of The File To Be Renamed :- ').strip())
                # inputtting the file index to be opened

            if(x > len(l) or x <= 0):
                raise(ce.nosuchfileException)
            # raising nosuchfileException if the conditions are not met

            l = []

            for files in os.listdir():
                f_name, f_ext = os.path.splitext(files)  # splitting the files and their extension
                if(f_name != 'csvReaderLogFile'):
                    l.append(files)
            for files in l:
                file_ext = os.path.splitext(files)
                if(file_ext[1] != '.csv'):
                    raise(ce.notcsvException)
            # raising when other than csv files are opened
            break       # breaking the clause when the input is valid

        except ce.nosuchfileException:
            cr.lineTime(sec=0.5)        # calling lineTime function
            print('No Such Index Present')
            logging.info('No Such Index Present')                       # using logging.info

        except ce.notcsvException:
            cr.lineTime(sec=0.5)          # calling lineTime function
            print('This Is Not A CSV File')
            logging.info('This is not a csv file')                      # using logging.info

        except ValueError:
            cr.lineTime(sec=0.5)       # calling lineTime function
            print('Invalid Input')
            logging.info('Invaild Input')                               # using logging.info

    return(x)


def csvWriteFile(fileName, col, info):
    for i in range(len(col)):
        if(i == len(col) - 1):
            fileName.write(col[i])
        else:
            fileName.write(col[i] + ',')
    # appending the column name in the file
    fileName.write('\n')
    k = 1
    for i in range(1, len(info) + 1):
        if(k == len(col)):
            k = 0
            fileName.write(info[i-1])
            fileName.write('\n')
        else:
            fileName.write(info[i-1] + ',')
        k += 1
    # writing down information in the file

# the end of the program
# Programmed By :- Slothfulwave@612
