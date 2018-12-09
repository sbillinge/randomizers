'''Module that takes a text file and randomizes the lines

'''
import sys
import random
import re
import numpy as np
import datetime

if len(sys.argv)==1:                   # elegant exit if user doesn't give a filename
    print("usage: python SimonRandomizer.py <filename>")
    exit()

try:                                   # elegant exit if there is an error in the filename
    open(sys.argv[1],'r')
except IOError:
    print("sorry, I can't find a file called '"+sys.argv[1]+"', please try again.")
    exit()
    
i = open(sys.argv[1],'r')
datetag = datetime.date.today()
o = open('prepickedlist_'+str(datetag)+'.txt','w')
classlist = i.readlines()

# clean the lines to remove leading and trailing whitespace and line-ends
for i in np.arange(30):
    iter = 0
    for x in classlist:
        classlist[iter] = classlist[iter].strip()
        iter+=1

    classlist = list(filter(None, classlist)) # filter out any empty lines
    #random.shuffle(classlist)                 # now shuffle the names
    ranName = random.choice(classlist)

    # Some cleaning and pretty printing

    words = re.split(',',ranName)               # split into first and last names, assuming the format Last, First Second Third
    firstname = words[-1].split()         # first names are after the comma so [-1]

    item = 'And the lucky person is: '+firstname[0]     # pretty print with only first first name
    print(item)
    o.write(item + '\n')

o.close()

#if __name__ == "__main__"
