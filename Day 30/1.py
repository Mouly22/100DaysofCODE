#first we need to define a function, and then when we want to use it, we will call that function


def greet():              #define a function
    print("Hola")     

greet()                  #call a function

def fun(x, y):           #parameter 
    sum = x + y 
    mul = x * y
    return sum, mul            #I am returning two values 

res1, res2 = fun(3, 10)        #As I am returning two values, I have to accept two values with two variables.
print(res1, res2)             

def up(x):
    print(x)

up(10)

def down(p):
    p = 4
    print(p)

down(2)