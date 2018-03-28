# this is csv's most function file
# the most important file, as it will contain all the option function's code
# we will link this file to our main file and execute the required operation

import csv                            # importing csv module
import os                             # importing os module
import time                           # importing time module
import sys                            # importing sys module
import logging                        # importing logging module
import datetime                       # importing datetime module
import csvExceptionFile as ce         # importing csvFunctionFile as ce
import csvReuse as cr                 # importing csvReuse as cr
import csvReuseInputOutput as ci      # importing csvReuseInputOutput as ci


class csvExecution:
    # class named csvExcution for executing all the operation

    def createCSV(self):
        # this function will create a new csv file

        try:
            os.makedirs('csvDocument')
            # making the directory where all csv files

        except Exception:
            pass

        os.chdir('csvDocument')
        # changing the directory to csvDocument, as all files will be saved there

        logging.basicConfig(filename='csvReaderLogFile.log', level=logging.INFO, format='%(asctime)s : %(message)s')
        # using basicConfig function to keep a track what is happening in the program

        file_name = ci.enterName(num=0)     # calling enterName function with parameter num=0

        cr.lineTime(sec=0.5)      # calling lineTime function

        ci.openSys()              # calling openSys function

        cr.lineTime(sec=0.5)      # calling lineTime function

        with open(file_name, 'w') as my_file:
            # opening the specified file name in write mode
            logging.info(f'{file_name} has been opened for writing the content')       # using logging.info

            cr.lineTime(sec=0.5)        # calling lineTime function

            totColumn = ci.totalColumn()  # calling totalColumn function and assigning totColumn the value of x

            cr.lineTime(sec=0.5)      # calling lineTime function

            colList = []
            # list that will store column names

            for i in range(totColumn):
                # inputting the column names in specified csv file
                col_name = input(f'Enter The Column Name {i+1} :- ').strip()
                colList.append(col_name)
                # appending the column name to colList

                logging.info(f'Column Name {i+1} :- {col_name}')            # using logging.info

                if(i+1 == totColumn):
                    my_file.write(col_name)
                else:
                    my_file.write(col_name + ',')
                # writing down the column name in the csv file

            my_file.write('\n')             # writing a new line in the file

            cr.lineTime(sec=0.5)            # calling lineTime function

            numLines = ci.totalLines()      # calling totalLines function and assiging numLines the value of x

            cr.lineTime(sec=0.5)            # calling lineTime function

            for i in range(1, numLines + 1):
                for j in range(1, totColumn + 1):

                    while True:
                        # try-except clause
                        try:
                            col_info = input(f'Enter {colList[j-1]} For Line {i} :- ').strip()

                            logging.info(f'{colList[j-1]} For Line {i} :- {col_info}')     # using logging.info

                            for i in col_info:
                                if(i == ','):
                                    col_info = col_info.replace(',', '-')

                            # inputting the information in respective column
                            break           # breaking when input is valid

                        except ValueError:
                            # if value error is caught
                            cr.lineTime(sec=0.5)        # calling lineTime function
                            logging.info('Invalid Input')  # using logging.info
                            print('Invalid Input')
                            cr.lineTime(sec=0.5)        # calling lineTime function

                    if(j != totColumn):
                        my_file.write(col_info + ',')
                    else:
                        my_file.write(col_info)
                    # appending the information in the csv file
                cr.lineTime(sec=0.5)        # calling lineTime function
                my_file.write('\n')

            logging.info('Saving Your File')      # using logging.info
            cr.saveFile(name=file_name)         # calling saveFile function

            os.chdir('..')                        # comming back from the directory csvDocument
            logging.info(os.getcwd())             # using logging.info

    def displayCSV(self, num):
        # this function will display all the column names and thier information in a tabular format
        # if num = 0 then display all the information in a tabular format
        # if num = 1 then display specific information in a tabular format

        # try-exception clause
        try:
            os.chdir('csvDocument')
            # changing the directory to csvDocument
            logging.info(f'{os.getcwd()} is our current working directory')           # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)         # stopping the time for 0.5 seconds
            print('csvDocument Does Not Exist')
            logging.info('csvDocument Does Not Exist')      # using logging.info

        else:
            # if no error is caught

            fileList = cr.dispFileName()
            # calling dispFileName and assigning fileList with list l

            cr.lineTime(sec=0.5)    # calling lineTime function

            logging.info('Displaying Files Present In csvDocument')
            logging.info(fileList)
            # using logging.info

            indexFile = ci.indexFileNumber(num=0, l=fileList)    # calling indexFileNumber function and assigning the value of x to indexFile

            cr.lineTime(sec=0.5)                # calling lineTime function

            file_name = fileList[indexFile - 1] + '.csv'

            logging.info(f'{file_name} is the file selected')

            # try-except clause
            try:
                with open(file_name, 'r') as my_file:
                    logging.info(f'Opening {file_name}')                        # using loggging.info

                    colList = cr.appendFileCol(file_name)
                    # appending column name in colList
                    infoList = cr.appendFileInfo(file_name)
                    # appending information in infoList

                    if(num == 0):
                        # for displaying all the information
                        logging.info('Displaying all the information in a tabular format')

                        cr.displayTable(Listcol=colList, Listinfo=infoList)   # calling displayTable function
                        # to print the whole data in a tabular format

                    elif(num == 1):
                        # to display specific information
                        print(f'{file_name} has following {len(colList)} columns :-')
                        cr.lineTime(sec=0.5)          # calling lineTime function

                        cr.columnNames(l=colList)     # calling columnNames function

                        numCol = cr.exceptionX(xnum=0, l=colList)  # calling exceptionX function

                        indexl = []
                        colSpecific = []
                        # colSpecific is an empty list

                        cr.lineTime(sec=0.5)           # calling lineTime function

                        cr.columnNames(l=colList)     # calling columnNames function

                        for i in range(numCol):
                            a = cr.exceptionX(xnum=1, l=colList)  # calling exceptionX funtion
                            colSpecific.append(colList[a-1])
                            # appending the column names to colSpecific list
                            indexl.append(a-1)
                            # appending index in another list indexl

                        logging.info(f'{colSpecific} are the column names')

                        infoSpecific = []                   # infoSpecific is an empty list
                        temp = 0

                        for i in range(len(infoList) // len(colList)):
                            for j in indexl:
                                infoSpecific.append(infoList[temp + j])
                            temp += len(colList)
                        # appending specific information in infoSpecific list

                        logging.info('Displaying specific information in a tabular format')         # using logging.info

                        cr.lineTime(sec=0.5)        # calling lineTime function

                        # for displaying all the information
                        cr.displayTable(Listcol=colSpecific, Listinfo=infoSpecific)   # calling displayTable function
                        # to print the whole data in a tabular format

            except Exception as e:
                cr.lineTime(sec=0.5)            # calling lineTime function
                print('Error In Opening The File')
                print(e)
                logging.info('Error In Opening The File')       # using logging.info

            os.chdir('..')                          # comming back from csvDocument
            logging.info(f'{os.getcwd()} is our current directory')           # using logging.info

            cr.lineTime(sec=0.5)                # calling lineTime funtion

            cr.enter_Exception()                    # calling enter_Exception funciton

    def dispSavedFiles(self):
        # this function will display all the files that are saved inside csvDocument directory
        # try-except clause

        try:
            os.chdir('csvDocument')             # chaning the directory to csvDocument
            logging.info(f'{os.getcwd()} is our current directory')      # using logging.info

        except Exception:
            # if any exception is found
            cr.lineTime(sec=0.5)                # calling lineTime function
            print('csvDocument Not Found')
            logging.info('csvDocument Not Found')       # using logging.info

        else:
            # if no exception is found

            cr.dispFileName()               # calling dispFileName

            os.chdir('..')                  # comming back from csvDocument
            logging.info(f'{os.getcwd()} is our current directory')

        cr.enter_Exception()                # calling enter_Exception

    def removeSpecificFiles(self):
        # this function will remove the files

        # try-except clause
        try:
            os.chdir('csvDocument')             # chaning the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)               # calling lineTime fucntion
            print('No Such File Present')

        else:
            # is no error is caught

            # try-except clause
            try:
                fileList = cr.dispFileName()    # calling dispFileName function

                if(len(fileList) == 0):
                    raise(ce.nosuchfileException)

                cr.lineTime(sec=0.5)            # calling lineTime function

                indexFile = ci.indexFileNumber(num=1, l=fileList)   # calling indexFileNumber function and assiging the value of x in indexFile

                cr.lineTime(sec=0.5)                # calling lineTime function

                file_name = fileList[indexFile - 1] + '.csv'

                logging.info(f'{file_name} is the file selected')                   # using logging.info

                os.remove(file_name)        # removing the file specified
                logging.info(f'{file_name} Removed')
                print(f'{file_name} Is Removed Successfully')

            except ce.nosuchfileException:
                cr.lineTime(sec=0.5)        # calling lineTime function

            os.chdir('..')                     # coming back from the directory
            logging.info(f'{os.getcwd()} is our current directory')     # using logging.info

        cr.enter_Exception()               # calling enter_Exception function

    def removeAllFiles(self):
        # this function will remove all the files present in the csvDocument

        # try-except clause
        try:
            os.chdir('csvDocument')        # changing the directory
            logging.info(f'{os.getcwd()} is our current working directory')  # using logging.info

        except Exception:
            cr.lineTime(sec=0.5)           # calling lineTime function
            print('File Not Found')
            logging.info('File Not Found')

        else:

            try:
                deleteFile = cr.delAllFile()

                if(len(deleteFile) == 0):
                    raise(ce.nosuchfileException)

                for files in deleteFile:
                    os.remove(files)
                # removing files

            except ce.nosuchfileException:
                cr.lineTime(sec=0.5)        # calling lineTime function
                print('No File Is Saved')

            else:
                cr.lineTime(sec=0.5)        # calling lineTime function
                print('All Files Have Been Successfully Removed')
                logging.info('All Files Have Been Successfully Removed')       # using logging.info

            os.chdir('..')                   # coming back from the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        cr.enter_Exception()            # calling enter_Exception function

    def renameFiles(self):
        # this function will rename files

        # try-except clause
        try:
            os.chdir('csvDocument')             # chaning the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)               # calling lineTime fucntion
            print('So Such File Present')

        else:
            # is no error is caught

            try:
                fileList = cr.dispFileName()    # calling dispFileName function

                if(len(fileList) == 0):
                    raise(ce.nosuchfileException)

                cr.lineTime(sec=0.5)           # calling lineTime function

                indexFile = ci.indexFileNumber(num=2, l=fileList)   # calling indexFileNumber function and assigning the value of x to indexFile

                cr.lineTime(sec=0.5)                # calling lineTime function

                file_name = fileList[indexFile - 1] + '.csv'

                logging.info(f'{file_name} is the file selected')                   # using logging.info

                newName = ci.enterName(num=1)   # calling enterName function

                cr.lineTime(sec=0.5)            # calling lineTime function

                os.rename(file_name, newName)   # renaming the file

                print(f'{file_name} has been renamed to {newName}')
                logging.info(f'{file_name} has been renamed to {newName}')      # using logging.info

            except ce.nosuchfileException:
                cr.lineTime(sec=0.5)

            os.chdir('..')          # coming back from the directory
            logging.info(f'{os.getcwd()} is our current directory')         # using logging.info

        cr.enter_Exception()           # using enter_Exception function

    def copyContent(self, call):
        # this function is for copying the content from one file to another file
        # if call = 0 then copy all the content to another file
        # if call = 1 then copy only specific content to another file

        # try-exception clause
        try:
            os.chdir('csvDocument')
            # changing the directory to csvDocument
            logging.info(f'{os.getcwd()} is our current working directory')           # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)         # stopping the time for 0.5 seconds
            print('csvDocument Does Not Exist')
            logging.info('csvDocument Does Not Exist')      # using logging.info

        else:
            # if no error is caught

            fileList = cr.dispFileName()
            # calling dispFileName and assigning fileList with list l

            cr.lineTime(sec=0.5)    # calling lineTime function

            logging.info('Displaying Files Present In csvDocument')
            logging.info(fileList)
            # using logging.info

            indexFile = ci.indexFileNumber(num=0, l=fileList)    # calling indexFileNumber function and assigning the value of x to indexFile

            cr.lineTime(sec=0.5)                # calling lineTime function

            file_name = fileList[indexFile - 1] + '.csv'

            logging.info(f'{file_name} is the file selected')

            # try-except clause
            try:
                with open(file_name, 'r') as my_file:
                    logging.info(f'Opening {file_name}')               # using loggging.info

                    csv_reader = csv.DictReader(my_file)       # using DictReader to read the content of the csv file

                    file_name2 = ci.enterName(num=0)     # calling enterName function with parameter num=0

                    logging.info(f'{file_name2} is our new file')       # using logging.info

                    cr.lineTime(sec=0.5)      # calling lineTime function

                    with open(file_name2, 'w') as new_file:
                        if(call == 0):
                            # for writing down all the information

                            logging.info('Writing Down All Information')    # using logging.info

                            fieldnames = cr.appendFileCol(file_name)       # calling appendFileCol function

                            logging.info(f'{fieldnames} are the specific columns')      # calling logging.info

                            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames)     # using DictWriter for writing down the information
                            csv_writer.writeheader()           # using writeheader() to write the column names

                            for lines in csv_reader:
                                csv_writer.writerow(lines)     # writing down the lines

                        elif(call == 1):
                            # for writing down specific information

                            logging.info('Writing down specific information')

                            colList = cr.appendFileCol(file_name)         # using appendFileCol function
                            logging.info(f'{colList} are the columns')  # using logging.info

                            # to display specific information
                            print(f'{file_name} has following {len(colList)} columns :-')
                            cr.lineTime(sec=0.5)          # calling lineTime function

                            cr.columnNames(l=colList)     # calling columnNames function

                            numCol = cr.exceptionX(xnum=0, l=colList)  # calling exceptionX function

                            colSpecific = []           # colSpecific is an empty list
                            delCol = []                # delCol is an empty list

                            cr.lineTime(sec=0.5)       # calling lineTime function

                            cr.columnNames(l=colList)     # calling columnNames function

                            for i in range(numCol):
                                a = cr.exceptionX(xnum=1, l=colList)  # calling exceptionX funtion
                                colSpecific.append(colList[a-1])
                                # appending the column names to colSpecific list

                            for i in colList:
                                if i not in colSpecific:
                                    delCol.append(i)
                            # appending columns that are to be deleted from the file

                            logging.info(f'{colSpecific} are the column names')     # using logging.info

                            csv_writer = csv.DictWriter(new_file, fieldnames=colSpecific)    # using DictWriter method
                            csv_writer.writeheader()        # using writeheader method

                            for lines in csv_reader:
                                for item in delCol:
                                    del lines[item]
                                csv_writer.writerow(lines)

                cr.lineTime(sec=0.5)                        # calling lineTime function
                print('Copying Successfully Done')

            except Exception as e:
                # if exception is caught
                cr.lineTime(sec=0.5)            # calling lineTime function
                print(e)
                print('Error')
                logging.info('Error')

            os.chdir('..')          # coming back from the directory
            logging.info(f'{os.getcwd()} is our current working directory')
        cr.enter_Exception()    # calling enter_Exception function

    def addAtFront(self):
        # this function will add a line at the top of the file

        # try-except clause
        try:
            os.chdir('csvDocument')             # chaning the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)               # calling lineTime fucntion
            print('No Such File Present')

        else:
            # is no error is caught

            fileList = cr.dispFileName()
            # calling dispFileName and assigning fileList with list l

            cr.lineTime(sec=0.5)    # calling lineTime function

            logging.info('Displaying Files Present In csvDocument')
            logging.info(fileList)
            # using logging.info

            indexFile = ci.indexFileNumber(num=0, l=fileList)    # calling indexFileNumber function and assigning the value of x to indexFile

            cr.lineTime(sec=0.5)                # calling lineTime function

            file_name = fileList[indexFile - 1] + '.csv'

            logging.info(f'{file_name} is the file selected')

            # try-except clause
            try:
                with open(file_name, 'r') as my_file:
                    # opening the file

                    logging.info(f'Opening {file_name}')              # using loggging.info

                    colList = cr.appendFileCol(file_name)
                    # appending column name in colList
                    infoList = cr.appendFileInfo(file_name)
                    # appending information in infoList

                    infoUpdate = []     # infoUpdate is an empty list

                    with open('new_file.csv', 'w') as new_file:
                        # opening new file to store the updated information
                        for i in colList:
                            while True:
                                # try-except clause
                                try:
                                    x = input(f'Enter Description in {i} :- ').strip()     # enter the information

                                    for i in x:
                                        if(i == ','):
                                            x = x.replace(',', '-')

                                    break   # breaking when valid input is entered
                                except ValueError:
                                    # if value error is caught
                                    cr.lineTime(sec=0.5)        # calling lineTime function
                                    print('Invalid Input')

                            infoUpdate.append(x)
                        # appending information at font of the list

                        for i in infoList:
                            infoUpdate.append(i)
                        # appending all other information in the list

                        ci.csvWriteFile(fileName=new_file, col=colList, info=infoUpdate)    # calling csvWriteFile function

                cr.lineTime(sec=0.5)            # calling lineTime fucntion
                print('Information Added Successfully')
                logging.info('Information Added Successfully')  # using logging.info
                cr.lineTime(sec=0.5)       # calling lineTime function

                os.remove(file_name)                # removing file_name
                os.rename('new_file.csv', file_name)      # renaming the file

            except Exception as e:
                # if any exception is caught
                cr.lineTime(sec=0.5)       # calling lineTime function
                print(e)
                print('Program Confronted Some Error')

            os.chdir('..')          # comming back from the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info
            cr.lineTime(sec=0.5)    # calling lineTime function
            cr.enter_Exception()    # calling enter_Exception function

    def addInBtw(self):
        # this function will add information in between the line

        # try-except clause
        try:
            os.chdir('csvDocument')             # chaning the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)               # calling lineTime fucntion
            print('No Such File Present')

        else:
            # is no error is caught
            fileList = cr.dispFileName()
            # calling dispFileName and assigning fileList with list l

            cr.lineTime(sec=0.5)    # calling lineTime function

            logging.info('Displaying Files Present In csvDocument')
            logging.info(fileList)
            # using logging.info

            indexFile = ci.indexFileNumber(num=0, l=fileList)    # calling indexFileNumber function and assigning the value of x to indexFile

            cr.lineTime(sec=0.5)                # calling lineTime function

            file_name = fileList[indexFile - 1] + '.csv'

            logging.info(f'{file_name} is the file selected')

            # try-except clause
            try:
                with open(file_name, 'r') as my_file:
                    # opening the file

                    logging.info(f'Opening {file_name}')              # using loggging.info

                    colList = cr.appendFileCol(file_name)
                    # appending column name in colList
                    infoList = cr.appendFileInfo(file_name)
                    # appending information in infoList

                    infoUpdate = []     # infoUpdate is an empty list

                    with open('new_file.csv', 'w') as new_file:
                        # opening new file to store the updated information

                        while True:
                            # try-except clause

                            try:
                                c = 0
                                whichElement = input(f'Enter {colList[0]} after which you want to add another line :- ')
                                # entering the information
                                logging.info(f'{whichElement} is the element after which element will be added')

                                for i in range(0, len(infoList), len(colList)):
                                    if(whichElement != infoList[i]):
                                        c += 1

                                if(c == len(infoList) // len(colList)):
                                    raise(ce.nosuchcolumnException)

                                break       # breaking the clause when the input in valid

                            except ValueError:
                                cr.lineTime(sec=0.5)    # calling lineTime function
                                print('Invalid Input')
                                logging.info('Invalid Input')

                            except ce.nosuchcolumnException:
                                cr.lineTime(sec=0.5)
                                print(f'{whichElement} not present')
                                logging.info(f'{whichElement} not present')

                        cr.lineTime(sec=0.5)        # calling lineTime function

                        try:
                            position = infoList.index(whichElement)

                        except Exception:
                            cr.lineTime(sec=0.5)    # calling lineTime function
                            print(f'No such {colList[0]} present')

                        else:
                            for i in range(len(infoList)):
                                # appending information in list infoUpdate
                                if(i == position + len(colList)):
                                    for j in range(len(colList)):
                                        while True:
                                            # try-except clause
                                            try:
                                                x = input(f'Enter Discription In {colList[j]} :- ').strip()    # enter information

                                                for i in x:
                                                    if(i == ','):
                                                        x = x.replace(',', '-')

                                                logging.info(f'{x} is entered as {colList[j]}')    # using logging.info

                                                break       # breaking the clause when input is valid
                                            except ValueError:
                                                # if value error is caught
                                                cr.lineTime(sec=0.5)    # using lineTime function
                                                print('Invalid Input')
                                                logging.info('Invalid Input')
                                        infoUpdate.append(x)
                                        logging.info(f'{x} is entered as {colList[j]}')  # using logging.info
                                    infoUpdate.append(infoList[i])
                                else:
                                    infoUpdate.append(infoList[i])
                            # appending the information

                            ci.csvWriteFile(fileName=new_file, col=colList, info=infoUpdate)    # calling csvWriteFile function
                            cr.lineTime(sec=0.5)        # calling lineTime function

                            print('Information Added Successfully')
                            logging.info('Information Added Successfully')  # using logging.info

                    os.remove(file_name)                # removing file_name
                    os.rename('new_file.csv', file_name)      # renaming the file

            except Exception:
                # if any exception is caught
                cr.lineTime(sec=0.5)       # calling lineTime function
                print('Program Confronted Some Error')

            os.chdir('..')          # comming back from the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        cr.lineTime(sec=0.5)    # calling lineTime function
        cr.enter_Exception()    # calling enter_Exception function

    def addAtRare(self):
        # this function will add information at the end of the file

        # try-except clause
        try:
            os.chdir('csvDocument')             # chaning the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)               # calling lineTime fucntion
            print('No Such File Present')

        else:
            # is no error is caught
            fileList = cr.dispFileName()
            # calling dispFileName and assigning fileList with list l

            cr.lineTime(sec=0.5)    # calling lineTime function

            logging.info('Displaying Files Present In csvDocument')
            logging.info(fileList)
            # using logging.info

            indexFile = ci.indexFileNumber(num=0, l=fileList)    # calling indexFileNumber function and assigning the value of x to indexFile

            cr.lineTime(sec=0.5)                # calling lineTime function

            file_name = fileList[indexFile - 1] + '.csv'

            logging.info(f'{file_name} is the file selected')

            # try-except clause
            try:
                with open(file_name, 'r') as my_file:
                    # opening the file

                    logging.info(f'Opening {file_name}')              # using loggging.info

                    colList = cr.appendFileCol(file_name)
                    # appending column name in colList
                    infoList = cr.appendFileInfo(file_name)
                    # appending information in infoList

                    with open('new_file.csv', 'w') as new_file:
                        # opening new file to store the updated information

                        for i in range(len(colList)):

                            while True:
                                # try-except clause

                                try:
                                    x = input(f'Enter Discription In {colList[i]} :- ').strip()        # entering the information

                                    for i in x:
                                        if(i == ','):
                                            x = x.replace(',', '-')

                                    logging.info(f'{x} is entered as {colList[i]}')   # using logging.info

                                    break           # breaking the clause when the input is valid

                                except ValueError:
                                    cr.lineTime(sec=0.5)        # using lineTime function
                                    print('Invalid Input')
                                    logging.info('Invalid Input')   # using logging.info

                            infoList.append(x)
                        # appending the information

                        ci.csvWriteFile(fileName=new_file, col=colList, info=infoList)    # calling csvWriteFile function

                    cr.lineTime(sec=0.5)    # calling lineTime function
                    print('Information Added Successfully')
                    logging.info('Information Added Successfully')  # using logging.info
                    cr.lineTime(sec=0.5)       # calling lineTime function
                os.remove(file_name)                # removing file_name
                os.rename('new_file.csv', file_name)      # renaming the file

            except Exception:
                # if any exception is caught
                cr.lineTime(sec=0.5)       # calling lineTime function
                print('Program Confronted Some Error')

            os.chdir('..')          # comming back from the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

            cr.lineTime(sec=0.5)    # calling lineTime function

        cr.enter_Exception()    # calling enter_Exception function

    def updateLine(self):
        # this function will update the whole line

        # try-except clause
        try:
            os.chdir('csvDocument')             # chaning the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)               # calling lineTime fucntion
            print('No Such File Present')

        else:

            # is no error is caught
            fileList = cr.dispFileName()
            # calling dispFileName and assigning fileList with list l

            cr.lineTime(sec=0.5)    # calling lineTime function

            logging.info('Displaying Files Present In csvDocument')
            logging.info(fileList)
            # using logging.info

            indexFile = ci.indexFileNumber(num=0, l=fileList)    # calling indexFileNumber function and assigning the value of x to indexFile

            cr.lineTime(sec=0.5)                # calling lineTime function

            file_name = fileList[indexFile - 1] + '.csv'

            logging.info(f'{file_name} is the file selected')

            # try-except clause
            try:
                with open(file_name, 'r') as my_file:
                    # opening the file

                    logging.info(f'Opening {file_name}')              # using loggging.info

                    colList = cr.appendFileCol(file_name)
                    # appending column name in colList
                    infoList = cr.appendFileInfo(file_name)
                    # appending information in infoList

                    UpdatedinfoList = []            # UpdatedinfoList is an empty list

                    with open('new_file.csv', 'w') as new_file:
                        # opening new file to store the updated information

                        while True:
                            # try-except clause

                            try:
                                c = 0
                                x = input(f'Enter {colList[0]} after which you want to add another line :- ')
                                # entering the information
                                logging.info(f'{x} is the element after which element will be added')

                                for i in range(0, len(infoList), len(colList)):
                                    if(x != infoList[i]):
                                        c += 1

                                if(c == len(infoList) // len(colList)):
                                    raise(ce.nosuchcolumnException)

                                break       # breaking the clause when the input in valid

                            except ValueError:
                                cr.lineTime(sec=0.5)    # calling lineTime function
                                print('Invalid Input')
                                logging.info('Invalid Input')

                            except ce.nosuchcolumnException:
                                cr.lineTime(sec=0.5)
                                print(f'{x} not present')
                                logging.info(f'{x} not present')

                        cr.lineTime(sec=0.5)    # calling lineTime function

                        try:
                            position = infoList.index(x)        # assiging the index of x to variable position

                        except Exception:
                            # if any exception is caught
                            print(f'{x} is not present')
                            ci.csvWriteFile(fileName=new_file, col=colList, info=infoList)    # calling csvWriteFile function

                        else:
                            k = 0
                            length = len(colList)

                            for i in range(len(infoList)):
                                if(i == position and length != 0):
                                    cr.lineTime(sec=0.5)        # calling lineTime Function

                                    while True:
                                        try:
                                            x = input(f'Enter Discription in {colList[k]} :- ').strip()     # entering the required information

                                            for i in x:
                                                if(i == ','):
                                                    x = x.replace(',', '-')

                                            logging.info(f'{x} is entered as {colList[k]}')               # using logging.info

                                            break           # breaking the clause when the input is valid

                                        except Exception:
                                            # when any exception is encountered
                                            cr.lineTime(sec=0.5)        # calling lineTime function
                                            print('Invalid Input')
                                            logging.info('Invalid Input')       # using logging.info

                                    UpdatedinfoList.append(x)
                                    k += 1
                                    position += 1
                                    length -= 1

                                else:
                                    UpdatedinfoList.append(infoList[i])
                            # appending the updated information in the list UpdatedinfoList

                            ci.csvWriteFile(fileName=new_file, col=colList, info=UpdatedinfoList)    # calling csvWriteFile function
                            cr.lineTime(sec=0.5)        # calling lineTime funtion
                            print('Information Updated Successfully')
                            logging.info('Information Updated Successfully')  # using logging.info
                            cr.lineTime(sec=0.5)       # calling lineTime function

                os.remove(file_name)                # removing file_name
                os.rename('new_file.csv', file_name)      # renaming the file

            except Exception:
                # if any exception is caught
                cr.lineTime(sec=0.5)       # calling lineTime function
                print('Program Confronted Some Error')

            os.chdir('..')          # comming back from the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

            cr.lineTime(sec=0.5)    # calling lineTime function

        cr.enter_Exception()    # calling enter_Exception function

    def UpdateSpecific(self):
        # this function will update specific content of any specified line

        # try-except clause
        try:
            os.chdir('csvDocument')             # chaning the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)               # calling lineTime fucntion
            print('No Such File Present')

        else:
            # is no error is caught
            fileList = cr.dispFileName()
            # calling dispFileName and assigning fileList with list l

            cr.lineTime(sec=0.5)    # calling lineTime function

            logging.info('Displaying Files Present In csvDocument')
            logging.info(fileList)
            # using logging.info

            indexFile = ci.indexFileNumber(num=0, l=fileList)    # calling indexFileNumber function and assigning the value of x to indexFile

            cr.lineTime(sec=0.5)                # calling lineTime function

            file_name = fileList[indexFile - 1] + '.csv'

            logging.info(f'{file_name} is the file selected')

            # try-except clause
            try:
                with open(file_name, 'r') as my_file:
                    # opening the file

                    logging.info(f'Opening {file_name}')              # using loggging.info

                    colList = cr.appendFileCol(file_name)
                    # appending column name in colList
                    infoList = cr.appendFileInfo(file_name)
                    # appending information in infoList

                    UpdatedinfoList = []            # UpdatedinfoList is an empty list
                    find = 0                        # assiging the value 0 to varaible find

                    with open('new_file.csv', 'w') as new_file:
                        # opening new file to store the updated information

                        while True:
                            # try-except clause

                            try:
                                c = 0
                                updateFinder = input(f'Enter {colList[0]} after which you want to add another line :- ')
                                # entering the information

                                logging.info(f'{updateFinder} is the element after which element will be added')

                                for i in range(0, len(infoList), len(colList)):
                                    if(updateFinder != infoList[i]):
                                        c += 1

                                if(c == len(infoList) // len(colList)):
                                    raise(ce.nosuchcolumnException)

                                break       # breaking the clause when the input in valid

                            except ValueError:
                                cr.lineTime(sec=0.5)    # calling lineTime function
                                print('Invalid Input')
                                logging.info('Invalid Input')

                            except ce.nosuchcolumnException:
                                cr.lineTime(sec=0.5)
                                print(f'{updateFinder} not present')
                                logging.info(f'{updateFinder} not present')

                        cr.lineTime(sec=0.5)        # calling lineTime function

                        print(f'All the columns present in the file {file_name} are as follows :-')
                        cr.lineTime(sec=0.5)        # calling lineTime function
                        cr.columnNames(l=colList)  # calling columnNames function

                        numCol = cr.exceptionX(xnum=3, l=colList)  # calling exceptionX function

                        indexl = []
                        colSpecific = []           # colSpecific is an empty list

                        for i in range(numCol):
                            a = cr.exceptionX(xnum=1, l=colList)  # calling exceptionX funtion

                            while True:
                                # try-except clause
                                cr.lineTime(sec=0.5)    # calling lineTime function
                                try:
                                    x = input(f'Enter Discription In {colList[a-1]} :- ').strip()      # entering required information

                                    for i in x:
                                        if(i == ','):
                                            x = x.replace(',', '-')

                                    logging.info(f'{x} is entered as {colList[a-1]}')  # using logging.info
                                    break       # breaking the clause when the input is valid

                                except ValueError:
                                    cr.lineTime(sec=0.5)        # calling lineTime function
                                    print('Invalid Input')
                                    logging.info('Invalid Input')   # using logging.info

                            colSpecific.append(x)
                            # appending the updated information to colSpecific list
                            indexl.append(a-1)
                            # appending index in another list indexl

                        logging.info(f'{colSpecific} are the column names')

                        infoUpdated = []                   # infoSpecific is an empty list
                        addList = []                     # updated information for the specified line
                        c = 1                            # assiging the value 1 to variable c

                        for i in range(len(infoList)):
                            if(infoList[i] == updateFinder):
                                for j in range(len(colList)):
                                    if(c <= len(colList)):
                                        addList.append(infoList[i+j])
                                        c += 1
                        # appending the specific line information to addList

                        c = 0                           # assigning the value 0 to variable c

                        for i in indexl:
                            del addList[i-c]          # deleting the list item
                            c += 1

                        for i in range(len(indexl)):
                            addList.insert(indexl[i], colSpecific[i])
                        # inserting the updated information to the addList

                        c = 0

                        for i in range(len(infoList)):
                            if(infoList[i] == updateFinder):
                                for j in range(len(colList)):
                                    if(c <= len(colList) - 1):
                                        del infoList[i+j-c]
                                        c += 1
                                break

                        # deleting the x information line

                        for i in range(len(infoList)):
                            if(i == position):
                                for j in addList:
                                    infoUpdated.append(j)
                            infoUpdated.append(infoList[i])
                        # appending updated information to infoUpdated

                        ci.csvWriteFile(fileName=new_file, col=colList, info=infoUpdated)    # calling csvWriteFile function
                        cr.lineTime(sec=0.5)            # calling lineTime function
                        print('Information Updated Successfully')
                        logging.info('Information Updated Successfully')  # using logging.info

                os.remove(file_name)                    # removing the file name
                os.rename('new_file.csv', file_name)    # renaming the file

            except Exception as e:
                # if any exception is caught
                cr.lineTime(sec=0.5)       # calling lineTime function
                print('Program Confronted Some Error')

            os.chdir('..')          # comming back from the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        cr.lineTime(sec=0.5)    # calling lineTime function
        cr.enter_Exception()    # calling enter_Exception function

    def delCsvLine(self):
        # this function will delete the line as specified by the user

        # try-except clause
        try:
            os.chdir('csvDocument')             # chaning the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)               # calling lineTime fucntion
            print('No Such File Present')

        else:
            # is no error is caught
            fileList = cr.dispFileName()
            # calling dispFileName and assigning fileList with list l

            cr.lineTime(sec=0.5)    # calling lineTime function

            logging.info('Displaying Files Present In csvDocument')
            logging.info(fileList)
            # using logging.info

            indexFile = ci.indexFileNumber(num=0, l=fileList)    # calling indexFileNumber function and assigning the value of x to indexFile

            cr.lineTime(sec=0.5)                # calling lineTime function

            file_name = fileList[indexFile - 1] + '.csv'

            logging.info(f'{file_name} is the file selected')

            # try-except clause
            try:
                with open(file_name, 'r') as my_file:
                    # opening the file

                    logging.info(f'Opening {file_name}')              # using loggging.info

                    colList = cr.appendFileCol(file_name)
                    # appending column name in colList
                    infoList = cr.appendFileInfo(file_name)
                    # appending information in infoList

                    UpdatedinfoList = []            # UpdatedinfoList is an empty list
                    find = 0                        # assiging the value 0 to varaible find

                    with open('new_file.csv', 'w') as new_file:
                        # opening new file to store the updated information

                        while True:
                            # try-except clause

                            try:
                                c = 0
                                delFinder = input(f'Enter {colList[0]} after which you want to add another line :- ')
                                # entering the information
                                logging.info(f'{delFinder} is the element after which element will be added')

                                for i in range(0, len(infoList), len(colList)):
                                    if(delFinder != infoList[i]):
                                        c += 1

                                if(c == len(infoList) // len(colList)):
                                    raise(ce.nosuchcolumnException)

                                break       # breaking the clause when the input in valid

                            except ValueError:
                                cr.lineTime(sec=0.5)    # calling lineTime function
                                print('Invalid Input')
                                logging.info('Invalid Input')

                            except ce.nosuchcolumnException:
                                cr.lineTime(sec=0.5)
                                print(f'{delFinder} not present')
                                logging.info(f'{delFinder} not present')

                        try:
                            position = infoList.index(delFinder)        # assiging the index of delFinder to variable position

                        except Exception:
                            # if any exception is caught
                            cr.lineTime(sec=0.5)    # calling lineTime function
                            print(f'{delFinder} is not present')
                            ci.csvWriteFile(fileName=new_file, col=colList, info=infoList)    # calling csvWriteFile function

                        else:
                            length = len(colList)

                            for i in range(len(infoList)):
                                if(i == position and length != 0):
                                    position += 1
                                    length -= 1
                                else:
                                    UpdatedinfoList.append(infoList[i])
                            # deleting and appending he information into the list UpdatedinfoList

                            ci.csvWriteFile(fileName=new_file, col=colList, info=UpdatedinfoList)    # calling csvWriteFile function
                            print('Information Deleted Successfully')
                            logging.info('Information Deleted Successfully')  # using logging.info
                            cr.lineTime(sec=0.5)       # calling lineTime function

                os.remove(file_name)                    # removing the file name
                os.rename('new_file.csv', file_name)    # renaming the file

            except Exception as e:
                # if any exception is caught
                cr.lineTime(sec=0.5)       # calling lineTime function
                print(e)
                print('Program Confronted Some Error')

            os.chdir('..')          # comming back from the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        cr.lineTime(sec=0.5)    # calling lineTime function
        cr.enter_Exception()    # calling enter_Exception function

    def searchCsvFile(self):
        # this function will search the content as specified by the file

        # try-except clause
        try:
            os.chdir('csvDocument')             # chaning the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)               # calling lineTime fucntion
            print('No Such File Present')

        else:
            # is no error is caught
            fileList = cr.dispFileName()
            # calling dispFileName and assigning fileList with list l

            cr.lineTime(sec=0.5)    # calling lineTime function

            logging.info('Displaying Files Present In csvDocument')
            logging.info(fileList)
            # using logging.info

            indexFile = ci.indexFileNumber(num=0, l=fileList)    # calling indexFileNumber function and assigning the value of x to indexFile

            cr.lineTime(sec=0.5)                # calling lineTime function

            file_name = fileList[indexFile - 1] + '.csv'

            logging.info(f'{file_name} is the file selected')

            # try-except clause
            try:
                with open(file_name, 'r') as my_file:
                    # opening the file

                    logging.info(f'Opening {file_name}')              # using loggging.info

                    colList = cr.appendFileCol(file_name)
                    # appending column name in colList
                    infoList = cr.appendFileInfo(file_name)
                    # appending information in infoList

                    searchList = []            # UpdatedinfoList is an empty list
                    find = 0                        # assiging the value 0 to varaible find

                    while True:
                        # try-except clause

                        try:
                            c = 0
                            searchFinder = input(f'Enter {colList[0]} after which you want to add another line :- ')
                            # entering the information
                            logging.info(f'{searchFinder} is the element after which element will be added')

                            for i in range(0, len(infoList), len(colList)):
                                if(searchFinder != infoList[i]):
                                    c += 1

                            if(c == len(infoList) // len(colList)):
                                raise(ce.nosuchcolumnException)

                            break       # breaking the clause when the input in valid

                        except ValueError:
                            cr.lineTime(sec=0.5)    # calling lineTime function
                            print('Invalid Input')
                            logging.info('Invalid Input')

                        except ce.nosuchcolumnException:
                            cr.lineTime(sec=0.5)
                            print(f'{searchFinder} not present')
                            logging.info(f'{searchFinder} not present')

                    cr.lineTime(sec=0.5)        # calling lineTime function

                    position = []

                    try:
                        for i in range(0, len(infoList), len(colList)):
                            if(searchFinder == infoList[i]):
                                position.append(i)

                    except Exception:
                        # if any exception is caught
                        cr.lineTime(sec=0.5)    # calling lineTime function
                        print(f'{searchFinder} is not present')
                        ci.csvWriteFile(fileName=new_file, col=colList, info=infoList)    # calling csvWriteFile function

                    else:
                        length = len(colList)         # assigning the length of colList to variable length
                        c = 0

                        for i in range(len(infoList)):
                            if(i == position[c] and length != 0):
                                searchList.append(infoList[i])
                                length -= 1
                                position[c] += 1
                            if(length == 0):
                                length = len(colList)
                                c += 1
                                if(c == len(position)):
                                    break
                        # appending the items to be displayed in thelist searchList

                        cr.lineTime(sec=0.5)        # calling lineTime function
                        cr.displayTable(Listcol=colList, Listinfo=searchList)       # calling displayTable function
                        # displaying the appended information in a tabular format

                        logging.info('Information Searched')
                        cr.lineTime(sec=0.5)    # calling lineTime function

            except Exception:
                # if any exception is caught
                cr.lineTime(sec=0.5)       # calling lineTime function
                print('Program Confronted Some Error')

            os.chdir('..')          # comming back from the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        cr.lineTime(sec=0.5)    # calling lineTime function
        cr.enter_Exception()    # calling enter_Exception function

    def propertyCsvFile(self):
        # this function will display all the property of the file

        # try-except clause
        try:
            os.chdir('csvDocument')             # chaning the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        except Exception:
            # if any exception is caught
            cr.lineTime(sec=0.5)               # calling lineTime fucntion
            print('No Such File Present')

        else:
            # is no error is caught
            print('All The CSV Files Present in The Directory Are As Follows :- ')
            cr.lineTime(sec=0.5)            # stopping the time for 0.5 seconds

            fileList = cr.dispFileName()
            # calling dispFileName and assigning fileList with list l

            cr.lineTime(sec=0.5)    # calling lineTime function

            logging.info('Displaying Files Present In csvDocument')
            logging.info(fileList)
            # using logging.info

            indexFile = ci.indexFileNumber(num=0, l=fileList)    # calling indexFileNumber function and assigning the value of x to indexFile

            cr.lineTime(sec=0.5)                   # calling lineTime function

            file_name = fileList[indexFile - 1] + '.csv'

            logging.info(f'{file_name} is the file selected')

            mod_time = os.stat(file_name).st_mtime  # modification time

            print(f'Properties of {file_name} :-'.center(25, ' '))

            cr.lineTime(sec=0.5)                    # calling lineTime function

            print(f'1. File Name :- {file_name}')
            time.sleep(0.5)                           # stopping the time for 0.5 seconds
            print(f'2. Size :- {os.stat(file_name).st_size}')
            time.sleep(0.5)                           # stopping the time for 0.5 seconds
            print(f'3. Modification Time :- {datetime.datetime.fromtimestamp(mod_time)}')

            logging.info('Information Searched')
            cr.lineTime(sec=0.5)    # calling lineTime function

            os.chdir('..')          # comming back from the directory
            logging.info(f'{os.getcwd()} is our current working directory')     # using logging.info

        cr.lineTime(sec=0.5)    # using lineTime function
        cr.enter_Exception()    # calling enter_Exception function


obj = csvExecution()            # making an object of csvExcution class

# the end of the program
# Programmed By :- Slothfulwave@612
