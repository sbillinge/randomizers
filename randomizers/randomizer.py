'''Module that takes a text file and randomizes the lines

'''
import sys
import random
import re
import datetime
import os

from randomizers.inputs import get_input

def letsgo(ifilename):
    if not ifilename:
        i = get_input()
    else:
        i = open(ifilename,"r")
    datetag = datetime.date.today()
    ofilename = 'randomClasslist_' + str(datetag) + '.txt'
    o = open(ofilename, 'w')
    classlist = i.readlines()

    # clean the lines to remove leading and trailing whitespace and line-ends
    iter = 0
    for x in classlist:
        classlist[iter] = classlist[iter].strip()
        iter += 1

    classlist = list(filter(None, classlist))  # filter out any empty lines
    random.shuffle(classlist)  # now shuffle the names

    iter = 1
    # Some cleaning and pretty printing
    for x in classlist:
        words = re.split(',',
                         x)  # split into first and last names, assuming the format Last, First Second Third
        firstname = words[-1].split()  # first names are after the comma so [-1]

        item = str(iter) + ' ' + firstname[
            0]+ " "+ words[0]  # pretty print with only first first name
        print(item)
        writem = item + '\n'
        o.write(writem)
        iter += 1
    o.close()
    return ofilename


def main():
    i = "classlist.txt"
    outfilename = letsgo(i)
    os.remove(outfilename)


if __name__ == "__main__":
    main()
