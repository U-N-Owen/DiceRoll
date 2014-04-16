#! /usr/bin/env python

import random
import specialinputcopy as sic

# ----------- Main Program here ----------
# -----Input
print "Welcome to U-N-Owen's amazing dice rolling program!"
print "\n"
numberofsides = sic.int_input("How many sides does the die you want to roll have? | ")
while numberofsides <=1:
    numberofsides = sic.int_input("enter a number greater than 2 | ")

numofdice = sic.int_input("How many of these dice would you like to roll?|")
while numofdice < 0
mrosu:
    numofdice = sic.int_input("you can't roll negative dice|")

# -----Output
numtimesdone = 1
while numtimesdone <= numofdice:
    dieoutcome = random.randint(1,numberofsides)
    print "Here's the result of the roll |", dieoutcome
    numtimesdone += 1
print "Finished, above are your", str(numofdice),"D" + str(numberofsides) + " rolls."

