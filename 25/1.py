#You will be given a String S which contains only two characters - A and B. Your task is to find some substring pattern P in that string.
#The pattern P is - a substring will contain an equal number of A and B in each side.
#For example,in AABAABBAA, we get AB, AABB, BA, BBAA. In this problem, you have to print each pattern P present in the string S 
#along with their frequency. Finally, print the largest pattern P. If there are multiple largest patterns, print the one that came first.
#Sample Input AABAABBAA      
#Sample Output
#AB - 2 times
#BA - 2 times
#AABB - 1 times
#BBAA - 1 times
#Longest Pattern - AABB

y = "AABAABBAA".split()
lst = []
x = 'AABAABBAA'
y = x.count('AB')

p = lst.append(y)
print(p)

dict = {}
while(True):
    x = input("Enter: " ) 
    if x == 'STOP':
        break 
    else:
        if x not in dict:
            dict.update({x: 1})
        else:
            dict[x] += 1
            
for x,y in dict.items():
    print(x,'-',y,'times')
