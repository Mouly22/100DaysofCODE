#if else

#find the first number divisible by 5.



y = [12, 30, 23, 4, 23]
for i in y:
    if i % 5 == 0:
        print(i)
        break

else:
    print("not found")