def sum(x, y):
    while y:
        x, y = y, x% y
    print(x, y)
sum(100, 240)

#After each iteration...
#Iter 0: x=100, y=240; bool(y)=True
#Iter 1: x=240, y=100; bool(y)=True
#Iter 2: x=100, y=40; bool(y)=True
#Iter 3: x= 40, y=20; bool(y)=True
#Iter 4: x= 20, y=0; bool(y)=False