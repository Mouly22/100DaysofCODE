#key-value arguments:
def addfun(a, b):              #formal argument(just calling here)
    return a,b

y,z = addfun(23, 24)                  #actual argument(passing the values)
print(y,z)


#this actual argument has 4 types.

#1) position
def human(name, age):
    return name, age

m, n = human('rouja', 5)
print(m, n)                    #this is the normal process, arguments are receiving values as their position


#but now, if we don't know what position will receive which position, we will use the key method.

def school(ID, section):
    ID = ID - 2               #it might give error if we don't know the actual position of ID
    return ID, section

p, q = school(section = 'kuhu', ID = 200001)     #we are giving names of the keys within it
print(p, q)

#if i dont wanna pass an argument i need to provide an default argument for it, or else it will show an error
def facebook(name, age_res = 18):
    return name, age_res

m, n = facebook("mouly")       #even though we provide one value, it is not giving any error
print(m,n)

#now we dont know how many values we wanna receive:

def unknown(*n):

    x = 0

    for i in n:
        x = x + i

    print(x)


unknown(1,24,5,3,4,5,10,20)


#so by *args we can receive value as much as we want.



