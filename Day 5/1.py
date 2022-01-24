#the def statement doesn't run the code, it just remembers the code. we have to invoke.
x = 5
[print("hello")]
def myfunction():
    print("this is a function")
    print("we are storing the value here")
print("no")
myfunction()
x = x+2
print(x)
#a parameter is a variable which carries arguments.
def greet(lang):      #lang is the parameter here
    if lang == 'es':
        print("eng")
    elif lang == 'fr':
        print("Bonjur")
    else:
        print("hello")

greet('fr')

#the return keyword returns the result in the calling expression.
def greet():
    return "Bonjur"
print(greet(), "Gleen")
print(greet(), "Sally")
#A return statement stops the function call and “returns” the result to the caller.
#If the return statement is without any expression, then the special value None is returned.
#Note: Return statement can not be used outside the function

def newfun(p1,p2):
    if p1 == "bangla" or p2 == "India":
        return "sweetest language"
    elif p1 == "english":
        return "International language"
    else:
        return "Normal language"

print(newfun("bangla","english"))

def addval(a, b):
    x = a+b
    return x
p = addval(4, 6)
print(p)

here = 'banana'
y = max(here)
z = y * 2
print(z)

def func(x) :
    print(x)

func(10)
func(20)

def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

