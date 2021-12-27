x = 20
if x > 3:
    print("if it's true, no need to check afterwards")
elif x > 10:
    print("as if was true we won't check it")
else:
    print("sad")
print("all done")
#one of the three will run, not all of them.
#if there is no else; there's a case that the case won't execute also we can have more than one elif.

#Q: which of the below line will never execute?
if x<2:
    print("x is less than 2")
elif x>2:
    print("x is greater than 2")
else:
    print("somthing else")
#this else condition will never execute; any value of 2 will execute if or elif statement.

'''the try/except structure- surround a code with try/except structure.. if the code in try works,
the except is skipped or we'll get except as our output.'''
x = 'meow'
try:
    print("she is a cat")
    print(int("this will give me trackback"))
    print("not gonna work heh")
except:
    x = "leavee"
print("done",x)

#get a number from user:
p = input("Enter a number: ")
try:
    s = int(p)
except:
    s = -1
if s > 0:
    print("nice work <3 !")
else:
    print("not a number,try again <3 !")


























