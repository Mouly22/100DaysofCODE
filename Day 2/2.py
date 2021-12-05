#conditional execusion
#the key to is if statement
#it has a conditioon and it returns a true or false value. if this is true do the statement, orelse skip the statement.
x= 5
if x > 20:
    print("yes")
if x < 2:
    print("2 is small")

# == is a question mark version of equality
x = 5
if x ==5:
    print("equal to 5")
if x >= 1:
    print("x is greater or equal than 1")
if x <= 6:
    print("x is lessthan or equal to 6")
if x > 4:
    print("x is greater than 5")
if x < 10:
    print("x is less than 10")
if x != 0:
    print("x is NOT EQUAL to 0")

x = 10
if x ==10:
    print("x is 10")
    print("we are using indentation")
    print("this is another line")
print("out of indentation")
#blank lines and comments don't matter and don't get confused between tab and spaces

for i in range(5):
    print(i)
    if i > 2:
        print("big")
    print("done with i",i)
print("all done!")




