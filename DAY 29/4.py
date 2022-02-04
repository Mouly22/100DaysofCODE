#took input :3
from array import *
arr = array('i',[])
alen = int(input("Enter the length of the array:"))
for i in range(alen):
    vals = int(input("enter the values: "))
    arr.append(vals)
print(arr)
