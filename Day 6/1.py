tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)
friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
     print('Happy New Year:',  friend)
print('Done!')
zork = 0
for thing in range(len([9, 41, 12, 3, 74, 15])) :
    zork = zork + thing
print('After', zork)

smallest_so_far = -1
for the_num in range(len([9, 41, 12, 3, 74, 15])) :
   if the_num < smallest_so_far :
      smallest_so_far = the_num
print(smallest_so_far)

def sum(x, y):
    while y:
        x, y = y, x% y
    print(x, y)
sum(100, 240)

print(100%240)



