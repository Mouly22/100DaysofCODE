#we were receiving values by using *args, 

def participant(*data):
    print(data)
    for i in data:
        print(i)
    return data

y = participant("rain", 23, "dancer", 'dhaka')
print(y)


#now if we want to receive data also with keywords we need to use **kwargs.

def participant(**data):
    for i,j in data.items():
        print(i,j)
    return data

y= participant(name= "rain", age = 23, profession = "dancer", place ='dhaka')
print(y)
