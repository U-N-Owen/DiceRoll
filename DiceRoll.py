#! /usr/bin/env python

import random as rand
import specialinputcopy as sic

# ----------- Main Program here ----------
# -----Input
print "Welcome to U-N-Owen's amazing dice rolling program!"
print "\n"

numofdice = sic.int_input("How many of dice would you like to roll?|")
#store in a list of values [1,2,3,4,5 ...] (do it by  list.append
List = []
while len(List) + 1 <= numofdice:
    List.append(sic.int_input("How many sides does the die you want to roll have? | "))



# -----Output
numtimesdone = 1
List.sort()
while numtimesdone <= numofdice:
    dieoutcome = rand.randint(1,List[numtimesdone-1]) # instead of number of sides do numberofsides list value num times done
    print "Here's the result of your D" + str(List[numtimesdone-1]) + " roll |", dieoutcome #between of and the insert a "D#" marker
    numtimesdone += 1
print "Finished, above are your", numofdice, "rolls."

