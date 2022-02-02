p = 5
while p < 23:
    print('result', p)
    p += 1

print()

#while loop is for condition, for loop is for sequtial.

lst = [20,34,1, 5]
for i in range(len(lst)):
    print('hehe', lst[i])


me = 25

s = int(input("How many candy do you want? " ))
for i in range((s)):
    if i >= me:
        print("Out of stock")
        break
    
    print(f"here you go {i} with candy")

print("Bye")