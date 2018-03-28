# this is a file for reusing various function


import csvExceptionFile as ce               # importing csvExceptionFile as ce
import csv                            # importing csv module
import os                             # importing os module
import time                           # importing time module
import sys                            # importing sys module
import logging                        # importing logging module


def enter_Exception():
    # this function is for enter exception
    # for pressing enter key
    # and checking whether enter key is pressed or not

    while True:
        # try-except clause
        try:
            lineTime(sec=0.5)
            # calling lineTime funciton
            x = input('Press Enter Key To Continue').strip()

            if(len(x) > 0):
                raise(ce.enterException)

            break            # breaking the clause when enter key is pressed

        except ce.enterException:
            lineTime(sec=0.5)           # calling lineTime fucntion
            print('Press Only Enter Key')


def dispFileName():
    # this function will display all the files present in csvDocument
    i, l = 1, []      # assigning i value 1 and l an empty list

    if(len(os.listdir()) > 1):
        lineTime(sec=0.5)            # calling lineTime function
        print('All CSV Files Saved in csvDocument are :- ')
        lineTime(sec=0.5)            # calling lineTime function

    for files in os.listdir():
        if(len(os.listdir()) > 1):
            f_name, f_ext = os.path.splitext(files)  # splitting the files and their extension
            if(f_name != 'csvReaderLogFile'):
                print(f'{i}. {f_name}')       # displaying all the files present
                i += 1
                l.append(f_name)       # appending all the file name in fileList
        else:
            lineTime(sec=0.5)           # calling lineTime function
            print('No File Has Been Saved')
    return(l)


def delAllFile():
    # this function will remove all the files present in csvDocument
    l = []      # assigning i value 1 and l an empty list

    for files in os.listdir():
        f_name, f_ext = os.path.splitext(files)  # splitting the files and their extension
        if(f_name != 'csvReaderLogFile'):
            l.append(files)       # appending all the file name in fileList
    return(l)


def appendFileCol(file_name):
    # this function will append the file's column
    j, l = 0, []           # assiging j a value 0

    with open(file_name, 'r') as csv_file:
        # opening the file to append the column name
        csv_reader = csv.reader(csv_file)

        for i in csv_reader:
            if(j == 0):
                l = i
                j += 1
            else:
                break
    return(l)


def appendFileInfo(file_name):
    # this function will append the file's information
    l = []           # assiging j a value 0
    j = 0
    with open(file_name, 'r') as csv_file:
        # opening the file to append the information
        csv_reader = csv.reader(csv_file)

        for i in csv_reader:
            if(j != 0):
                l += i
            j += 1

    return(l)


def lineTime(sec):
    # this function is for printing line and stopping time for sec seconds
    print()
    time.sleep(sec)       # stopping the time for 0.5 seconds


def saveFile(name):
    g = 19
    # initialising variable g to value 19

    sys.stdout.write(f'Saving Your File {name}')
    sys.stdout.flush()
    time.sleep(1)
    sys.stdout.write('\r')
    sys.stdout.write('                                 \n')
    # using sys.stdout function displaying interactive message

    for i in range(20):
        sys.stdout.write('\r')
        sys.stdout.write('[' + '=' * i + ' ' * (g - i) + ']')
        sys.stdout.flush()
        time.sleep(0.05)

    sys.stdout.write('\r')
    sys.stdout.write('                                            \n')


# def noFileCSV()

def columnNames(l):
    # printing out the column names
    j = 1
    # assigning the value 1 to vriable j
    for i in l:
        print(f'{j}. {i}')
        j += 1
    # printing out column names
    logging.info(l)                     # using logging.info


def exceptionX(xnum, l):
    while True:
        # try-except clause
        try:
            lineTime(sec=0.5)            # calling the lineTime funtion

            if(xnum == 0):
                # user will enter the number of column he wants to display
                x = int(input('Enter Number of Column To Be Displayed :- ').strip())
            if(xnum == 1):
                # user will enter the index number of the column
                x = int(input('Enter Index Number of Column  :- ').strip())

            if(xnum == 2):
                # user will enter the index number of the column
                x = int(input('Enter Total Number of Columns To Be Updated :- ').strip())

            if(xnum == 3):
                # user will enter the number of column he wants to display
                x = int(input('Enter Number of Column To Be Updated :- ').strip())

            if(x > len(l) or x <= 0):
                raise(ce.nosuchcolumnException)
                # raising nosuchcolumnException when the condition is not met

            break   # breaking the clause when the input is valid

        except ce.nosuchcolumnException:
            # when nosuchcolumnException error is caugth
            lineTime(sec=0.5)        # calling lineTime fucntion
            print('Column Does Not Exist')

        except ValueError:
            # when the value error is caugth
            lineTime(sec=0.5)        # calling lineTime function
            print('Invalid Input')
    return(x)


def displayTable(Listcol, Listinfo):
    maxLength = []        # characters having max length

    g = len(Listinfo) // len(Listcol)
    # g is a variable which will store number of lines in the file

    length = len(Listcol)

    # length in the number of columns we have in the file

    colLength = []
    infoLength = []

    for i in range(length):
        colLength.append(len(Listcol[i]))
    for i in range(len(Listinfo)):
        infoLength.append(len(Listinfo[i]))
    # appending all the length of character in the list colLength and infoLength

    for i in range(length):
        if(g > 1):
            # if lines are more than one
            temp = colLength[i]
            z = 0
            x = i
            while(z < len(infoLength) - 1):
                if(temp > infoLength[x]):
                    temp = temp
                else:
                    temp = infoLength[x]
                z += length
                x += length
            maxLength.append(temp)
        elif(g == 1):
            if(colLength[i] > infoLength[i]):
                maxLength.append(colLength[i])
            else:
                maxLength.append(infoLength[i])
    # appending the maximum length of all the character in their respective column

    dashes = 0
    # assigning dashes a value 0

    for i in range(length):

        temp = maxLength[i]
        dashes += len('| ' + Listcol[i] + ' ' * (temp - len(Listcol[i])) + ' |')
        print('| ' + Listcol[i] + ' ' * (temp - len(Listcol[i])) + ' |', end='')
    print(end='\n')
    # calculating the number of dahses that will fill up the line and printing the column names

    print('=' * dashes)   # printing = 'dashes' number of times

    i = j = 0    # assigning i and j a value zero

    tempLength = length    # assigning tempLength the length of 'length'

    while(i < len(Listinfo)):
        temp = maxLength[j]
        print('| ' + Listinfo[i] + ' ' * (temp - len(Listinfo[i])) + ' |', end='')
        # printing down the information
        i += 1
        j += 1
        if(i == tempLength):
            time.sleep(0.5)       # stopping the time for 0.5 seconds
            print(end='\n')
            tempLength += length
        if(j == length):

            j = 0
# the end of the program
# Programmed By :- Slothfulwave@612
