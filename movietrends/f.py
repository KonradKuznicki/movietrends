''' module for simple file operations '''


def slurp(fName):
    ''' read entire file to memory '''
    with open(fName, 'r') as f:
        c = f.read()
    return c


def spit(fName, content):
    ''' put string to file name '''
    with open(fName, 'w') as f:
        f.write(content)
