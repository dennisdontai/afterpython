def myname():
    print("My name is Dennis")

myname()

# Parameters and arguments
def fullname(firstname,lastname):
    print(firstname+lastname)


fullname("Saka"," " "Martin")

# Tuple as an Argument
def mygames(*game):
    print(game[0])

mygames("basketball","tennis","football")

# key-value argument
def rank(position1,position2,position3):
   print("Student in first position is " + position1)

rank(position1="Martin", position2="Saka", position3="Ben")



