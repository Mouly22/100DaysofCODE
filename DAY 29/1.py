#array
from array import *

vals = array('i',[5,6,7, -4,4,])
print(vals)

p = array('I'),[4,57,2,57]
print(p)

s = array('f', [2.4, 5.3, 5.2])
print(s.buffer_info())    #(4310827648, 3)
print(s.typecode)   #f
#buffer_info gives us the size of the array
#(4310827648, 3)--> first one is the address and second one is the size

x = array('I',[97, 98,54,34,2])
x.reverse()
print(x)
print(x[2])
for i in range(len(x)):
    print(x[i])

for us in x:
    print(us)

x = array('u',['a','p','q','u','v'])
print(x)
print(x.buffer_info())
for i in x:
    print(i)
