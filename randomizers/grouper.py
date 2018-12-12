'''Module that takes a text file and puts the lines into groups of four people

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
    ofilename = 'randomGrouplist_'+str(datetag)+'.txt'
    o = open(ofilename,'w')
    classlist = i.readlines()

    # clean the lines to remove leading and trailing whitespace and line-ends
    iter = 0
    for x in classlist:
        classlist[iter] = classlist[iter].strip()
        iter+=1

    classlist = list(filter(None, classlist)) # filter out any empty lines
    random.shuffle(classlist)                 # now shuffle the names

    iter=1
    # Some cleaning and pretty printing
    item = []
    for x in classlist:
        words = re.split(',',x)               # split into first and last names, assuming the format Last, First Second Third
        firstname = words[-1].split()         # first names are after the comma so [-1]

        item.append(firstname[0])     # pretty print with only first first name
        iter+=1

    index,iter=0,0
    while index < len(item):
        print('Group '+str(iter+1)+':')
        o.write('Group '+str(iter+1)+':\n')
        try:
            print('Leader: '+item[index])
            o.write('Leader: '+item[index]+'\n')
        except IndexError:
            pass
        try:
            print('Scribe: '+item[index+1])
            o.write('Scribe: '+item[index+1]+'\n')
        except IndexError:
            pass
        try:
            print('Optimist: '+item[index+2])
            o.write('Optimist: '+item[index+2]+'\n')
        except IndexError:
            pass
        try:
            print('Skeptic: '+item[index+3]+'\n')
            o.write('Skeptic: '+item[index+3]+'\n\n')
        except IndexError:
            pass
        index +=4
        iter +=1

    o.close()
    return ofilename


def main():
    i = "classlist.txt"
    outfilename = letsgo(i)
    os.remove(outfilename)


if __name__ == "__main__":
    main()

