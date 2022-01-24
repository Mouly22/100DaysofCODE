y = 'AABAABBAA'
new = ''
for i in range(len(y)):
    if y[i] != y[i-1]:
        new += y[i]
print(new)