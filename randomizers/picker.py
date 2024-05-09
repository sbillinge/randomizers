'''Module that takes a text file and randomizes the lines

'''
import sys
import random
import re

if len(sys.argv)==1:                   # elegant exit if user doesn't give a filename
    print("usage: python SimonRandomizer.py <filename>")
    exit()

try:                                   # elegant exit if there is an error in the filename
    open(sys.argv[1],'r')
except IOError:
    print("sorry, I can't find a file called '"+sys.argv[1]+"', please try again.")
    exit()
    
i = open(sys.argv[1],'r')
o = open('randomClasslist.txt','w')
classlist = i.readlines()

# clean the lines to remove leading and trailing whitespace and line-ends


classlist = list(filter(None, classlist)) # filter out any empty lines
random.shuffle(classlist)                 # now shuffle the names
picked = random.choice(classlist).strip()

# Some cleaning and pretty printing

# words = re.split(',',ranName)               # split into first and last names, assuming the format Last, First Second Third
# firstname = words[-1].split()         # first names are after the comma so [-1]

item = f'And the lucky person is: {picked}'    # pretty print with only first first name
print(item)

print("randomized list:")
for item in classlist:
    print(item)

o.close()

#if __name__ == "__main__"
