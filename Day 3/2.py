#store and reuse pattern - Function
#we define function using def keyword.
#def does nothing but remember things and when we call the functin name it works then.
#in function, the code remembers where to come back.
#print(), int(), float() these all are functions
def rain(x):
    print("It is a rainy day",x)
    rain = "happiness"
    if rain == "happiness":
        print("Yaay")
    else:
        print("naay")
rain(5)
print("blah blah")
rain(2)

big = max("Hello world")
print(big)
#In a function we store values. A function takes some input and produces an output.
