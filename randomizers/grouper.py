'''Module that takes a text file and puts the lines into groups of four people

'''
import sys
import random
import re
import datetime
import numpy as np
import operator

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
classlist = [x.strip() for x in classlist]

classlist = list(filter(None, classlist))  # filter out any empty lines
random.shuffle(classlist)  # now shuffle the names

cclasslist = []
for x in classlist:
    words = re.split(',',
                     x)  # split into first and last names, assuming the format
    # Last, First Second Third
    firstname = words[-1].split()  # first names are after the comma so [-1]

    cclasslist.append(firstname[0].strip() + " " + words[
        0].strip())  # pretty print with only first first name

roles = {0: "Leader", 1: "Scribe", 2: "Optimist", 3: "pessimist", 4: "Realist",
         5: "Domestique"}
maxlen = max(cclasslist)
assignment = []
npergroup = 5
ngroups = int(len(cclasslist)) // int(npergroup) + 1
vals = 0
for v in roles.values():
    vals = max(vals, len(v))

if int(len(cclasslist)) % int(npergroup) == 0:
    ngroups = ngroups - 1

pad = 0
for j in np.arange(ngroups):
    for k in np.arange(npergroup):
        try:
            name = cclasslist.pop()
            assignment.append([name, j, roles.get(k)])
            pad = max(pad, len(name))
        except IndexError:
            pass

# pad = pad+vals
print(pad, vals)
for i in np.arange(ngroups):
    print("")
    print("group {}".format(int(i) + 1))
    for el in assignment:
        if el[1] == i:
            print("{0:10}: {1}".format(el[2], el[0]))
sorteda = sorted(assignment, key=operator.itemgetter(0))
print("")
for k in np.arange(0, len(classlist), 2):
    try:
        print("{0:<23} group: {1:3} | {2:<23} group: {3}".format(sorteda[k][0],
                                                                 sorteda[k][
                                                                     1] + 1,
                                                                 sorteda[k + 1][
                                                                     0],
                                                                 sorteda[k + 1][
                                                                     1] + 1))
    except IndexError:
        print("{0:<23} group: {1:3} |".format(sorteda[k][0], sorteda[k][1] + 1))
o.close()
