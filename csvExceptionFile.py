# this is csv's Exception handling file
# here we will write the user defined exception, which we expect to come while the excution of the program by the user


class enterException(Exception):
    # exception when some other key is pressed other than the enter key
    pass


class filenameException(Exception):
    # exception when the file-name entered by the user is not valid
    pass


class notcsvException(Exception):
    # exception when the file extension is not .csv
    pass


class morethanoneException(Exception):
    # exception when more than one file with same name is present
    pass


class nosuchfileException(Exception):
    # exception when wrong file name is entered
    pass


class nosuchcolumnException(Exception):
    # exception when wrong column name is entered
    pass

# the end of the program
# Programmed By :- Slothfulwave@612
