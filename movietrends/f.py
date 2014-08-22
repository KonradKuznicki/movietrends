import os

def slurp(fName):
    f = os.open(fName, 'r')
    c = f.read('utf-8')
    f.close()
    return c

def spit(fName, content):
    f = os.open(fName, 'w')
    f.write(content)
    f.close()
