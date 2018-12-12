'''Module that takes a text file and puts the lines into groups of four people

'''
import sys
import random
import re
import datetime
import pprint as pp
import numpy as np

if len(sys.argv) == 1:  # elegant exit if user doesn't give a filename
    print("usage: python SimonRandomizer.py <filename>")
    exit()

try:  # elegant exit if there is an error in the filename
    open(sys.argv[1], 'r')
except IOError:
    print("sorry, I can't find a file called '" + sys.argv[
        1] + "', please try again.")
    exit()

i = open(sys.argv[1], 'r')
datetag = datetime.date.today()
o = open('randomGrouplist_' + str(datetag) + '.txt', 'w')
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
cclasslist = []
for x in classlist:
    words = re.split(',',
                     x)  # split into first and last names, assuming the format
    # Last, First Second Third
    firstname = words[-1].split()  # first names are after the comma so [-1]

    cclasslist.append(firstname[0] + " " + words[
        0])  # pretty print with only first first name
    maxlen = max(cclasslist)
    iter += 1


print("")
print("Alphabetically")
for k in sorted(assignment):
    print(k, " group:", assignment[k])

roles = {0:"Leader",1:"Scribe",2:"Optimist",3:"pessimist",4:"Realist",5:"Domestique"}
newassignment = {}
npergroup = 5
ngroups = int(len(cclasslist))//int(npergroup) + 1
if int(len(cclasslist))%int(npergroup) == 0:
    ngroups = ngroups - 1


for j in np.arange(ngroups):
    for k in np.arange(npergroup):
        try:
            newassignment.update({cclasslist.pop():(j,roles.get(k))})
        except IndexError:
            pass

for i in np.arange(ngroups):
    print("")
    print("group {}".format(int(i)+1))
    for k,v in newassignment.items():
        if v[0] == i:
            print("{}: {}".format(v[1],k.strip()))


o.close()
