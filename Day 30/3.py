def myfun(lyst):
    print(id(lyst))
    lyst[1] = 22
    print(id(lyst))
    print(lyst)

lyst = [23, 456, 546]
print(lyst)
print(id(lyst))
myfun(lyst)

#and this is pass by reference, all the id's stays same as list is mutable

def immufun(p):
    print(id(p))
    print(p)
    p = 24
    print(id(p))                 #the value of this id changes as integer is immutable
    print(p)

p = 22
print(id(p))
immufun(p)
print()

