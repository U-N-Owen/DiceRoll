def name_input(prompt):
    name = str(raw_input(prompt))
    numberOfLetter = len(name)
    if numberOfLetter > 10:
        print "That's too long. I'll give you a nickname. How about" + name[1:10]
    else:
        print "Hello " + name
    return name

def int_input(prompt):
    incorrect = 1
    while incorrect == 1:
        try:
            number = raw_input(prompt)
            number = int(number)
            incorrect = 0
            return number
        except:
            number = raw_input("That's not a number, try again| ")
            incorrect = 1

def float_input(propmpt):
    incorrectFloat = 1
    while incorrectFloat == 1:
        try:
            numberFloat = raw_input(propmt)
            numberFloat = float(numberFloat)
            
            incorrectFloat = 0
            return numberFloat
        except:
            numberFloat = raw_input("That's not a number, try again| ")
            incorrectFloat = 1