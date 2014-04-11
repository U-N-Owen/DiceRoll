#! /usr/bin/env python

import random
import specialinputcopy as sic

# ----------- Main Program here ----------
print "Welcome to U-N-Owen's amazing dice rolling program!"
print "\n"
# use intinput to see how many dice the user wants to use
# while number of dice !=0
numberofsides = sic.int_input("How many sides does the die you want to roll have? | ")
    # number of dice - 1
dieoutcome = random.randint(1,numberofsides)
#while loop for # of dice needed
print "Here's the result of the roll |", dieoutcome
# print outcome as "d-number of faces | result"