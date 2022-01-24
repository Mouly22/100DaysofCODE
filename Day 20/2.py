lst = input("Enter list ")[1:-1].split(", ")  #take a list as an input;remove the bracket by slicing and split it using comma
dict = {}
for i in lst:
    nlst = i.split(":")
    dict.update(nlst)
    print(dict)
