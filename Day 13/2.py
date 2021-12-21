import random
prob = random.random()                         #returns a floating point number between 0 and 1
print(prob)

dicethrow = random.randrange(1,7)              #returns an int, one of 1,2,3,4,5,6
print(dicethrow)

#we import random module in order to make its functions available
# and it has functions like randrange, random 
#there are two possible syntax for importing and refering stuff from modules. thew first makes stuffs available 
#but doesn't give any special alias