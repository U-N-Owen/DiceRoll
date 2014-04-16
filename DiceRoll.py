#! /usr/bin/env python

import random as rand
import specialinputcopy as sic

# ----------- Main Program here ----------
print "Welcome to U-N-Owen's amazing dice rolling program!"
print "\n"
numberofsides = sic.int_input("How many sides does the die you want to roll have? | ")
# while loop for each die's value
numofdice = sic.int_input("How many of these dice would you like to roll?|")
#store in a list of values [1,2,3,4,5 ...] (do it by  list.append


numtimesdone = 1
while numtimesdone <= numofdice:
    dieoutcome = rand.randint(1,numberofsides) # instead of number of sides do numberofsides list value num times done
    print "Here's the result of the roll |", dieoutcome #between of and the insert a "D#" marker
    numtimesdone += 1
print "Finished, above are your", numofdice,"D" + numberofsides + " rolls."

