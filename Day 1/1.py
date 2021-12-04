x = 5 
if x < 10:
    print('true')
else:
    print('false')

print('done')
#this is conditonal statement

n = 5 
while n> 0:
    print(n)
    n -= 1
print("STOP")
#repeated step


x = "self"
for i in range(len(x)):
    print(x[i])
    


name = input()
handle = open(name)
count = dict()
for line in handle:
     words = line.split()
     for word in words:
        count[word] = count.get(word,0) + 1

bigC = None
bigW = None
for word,count in count.items():
    if bigC is None or count> bigC:
        bigW = word
        bigC = count

print(bigW, bigC)


