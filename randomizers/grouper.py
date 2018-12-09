'''Module that takes a text file and puts the lines into groups of four people

'''
import sys
import random
import re
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
o = open('randomGrouplist_'+str(datetag)+'.txt','w')
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
