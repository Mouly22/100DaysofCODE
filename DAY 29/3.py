#taking array input from the user
from array import*
arr = array('i', [])

num = int(input("Enter the length of the array: "))

for i in range(num):
    val = int(input("Enter the values of the array: "))
    arr.append(val)
print(arr)