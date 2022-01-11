#take a input dict from the user
n = 2
d = dict(input("Enter: ").split() for i in range(n))        #while taking input write one keu-value in only line and go to the next line
print(d)

#or,
val="""name mouly
age 21
home bogura"""
    
y = dict(x.split() for x in val.splitlines())
print(y)

#or
n = int(input("enter a n value:"))
d = {}
for i in range(n):
    keys = input() # here i have taken keys as strings
    values =input() # here i have taken values as integers
    d[keys] = values
print(d)

#or,
n = int(input())          #n is the number of items you want to enter
d ={}                     
for i in range(n):        
    text = input().split()     #split the input text based on space & store in the list 'text'
    d[text[0]] = text[1]       #assign the 1st item to key and 2nd item to value of the dictionary
print(d)

