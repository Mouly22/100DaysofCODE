#search a value from the array
#for searching a value, we have to track the index; for that we will use counter value.

from array import *
arrn = array('i',[23,4,55,1,2,4])
val = int(input("Enter the value you want to find: "))
c = 0 #counter for tracking index
for i in arrn:
    if i == val:
        print(c)
        break
    c += 1

#using index function:
print(arrn.index(val))