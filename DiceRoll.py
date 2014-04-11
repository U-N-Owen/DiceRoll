#! /usr/bin/env python

import random
import specialinputcopy

# ----------- Main Program here ----------
print "Welcome to U-N-Owen's amazing dice rolling program!"
print "\n"
numberofsides = specialinputcopy.int_input("How many sides does the die you want to roll have? | ")

dieoutcome = random.randint(1,numberofsides)
print "Here's the result of the roll |", dieoutcome

