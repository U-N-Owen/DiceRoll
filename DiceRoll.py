#! /usr/bin/env python

import random

# ----------- Main Program here ----------
print "Welcome to Misha's amazing dice rolling program!"
print "\n"
numberofsides = raw_input("How many sides does the die you want to roll have? | ")
try:
    numberofsides = int(numberofsides)
    dieoutcome = random.randint(1,numberofsides)
    print "Here's the result of the roll |", dieoutcome
except:
    print "That's not a number, try again later"
