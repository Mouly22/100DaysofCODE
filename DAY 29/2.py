#as we have seen we can access values from the array, how can we copy and print the values from an array to another array?

from array import *
arr = array('i',[2,4,-5,46,7,3])
print(arr)
#for i in arr:
    #print(i)
#Create an array with the same value.
arr = array('i',[2,4,-55,46,7,34])
newArr = array(arr.typecode, (a for a in arr))

for i in newArr:
    print(i)

#also,
num = array('i',[2,43, 3,-55,46,7,34])
vArr = array(num.typecode, (a*a for a in num ))   #square

for p in vArr:
    print(p)

#in while loop:
i = 0
while i < len(newArr):
    print(newArr[i])
    i += 1

