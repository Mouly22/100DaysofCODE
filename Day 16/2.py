lst = ["hi", "morning", "dog", "506", "caterpillar", "balloons", 106, "yo-yo", "python", "moon", "water", "sleepy", "daffy", 45, "donald", "whiteboard", "glasses", "markers", "couches", "butterfly", "100", "magazine", "door", "picture", "window", ["Olympics", "handle"], "chair", "pages", "readings", "burger", "juggle", "craft", ["store", "poster", "board"], "laptop", "computer", "plates", "hotdog", "salad", "backpack", "zipper", "ring", "watch", "finger", "bags", "boxes", "pods", "peas", "apples", "horse", "guinea pig", "bowl", "EECS"]
print(lst[31])

name = "alan walker"
print(type(name))

p = "5"
q = 5
print(p + "45")
print(q )
x = "this is a line"
print(x[-1])
print(x[len(x)-1])

#Create a new list of the 6th through 13th elements of lst (eight items in all) and assign it to the variable output.
lst = ["swimming", 2, "water bottle", 44, "lollipop", "shine", "marsh", "winter", "donkey", "rain", ["Rio", "Beijing", "London"], [1,2,3], "gold", "bronze", "silver", "mathematician", "scientist", "actor", "actress", "win", "cell phone", "leg", "running", "horse", "socket", "plug", ["Phelps", "le Clos", "Lochte"], "drink", 22, "happyfeet", "penguins"]
output = lst[5:13]
print(output)
#Create a variable output and assign to it a list whose elements are the words in the string str1.
str1 = "OH THE PLACES YOU'LL GO"
output = str1.split(" ")
print(output)
x = "Library is a place where you can find peace"
print(x.split("a"))