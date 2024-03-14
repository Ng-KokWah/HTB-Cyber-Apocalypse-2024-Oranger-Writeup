#Usage: python3 test.py <text file> e.g. python3 test.py test.txt  
import sys

f = open(sys.argv[1], "r")
temp = ""
i=0
for x in f:
  #this is to check in case you decided to copy the index out of range ones also
  if "Index out of range!" in x:
    continue
  else:
    temp += x.replace('Which character (index) of the flag do you want? Enter an index: Character at Index ' + str(i) + ': ', '').rstrip()
  i+=1

print(temp)
