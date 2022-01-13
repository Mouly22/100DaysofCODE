wds = ["red", "blue", "green"]
glue = ' '
s = glue.join(wds)
print(s)
print(wds)

print("***".join(wds))
print("".join(wds))

song = "The rain in Spain..."
wds = song.split('ai')
print(wds)

sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last = sports[-1:-4:-1]
p = sports[-1]
x = sports[len(sports)-3]
print(p)
print(x)
print(last)
lst = [0]
n_lst = lst[0]
print(type(lst))
print(type(n_lst))
lst = ['red','white','lavender','black']
print(lst[2])
[print(lst[-3])]

lst_0 =["Dairy milk", "Pringles", "Kitkat", "Coka-cola", "Harsheys", "Lays", "Cadbury"]
print(lst_0[1:6:2])
print(lst_0)

tlst = ['white', 2, ['Pringles', 'Kitkat', 'Coka-cola'], 'lavender']
print(tlst[2][1])

lst_1 = ["Dairy milk", "Pringles", "Kitkat", "Coka-cola", "Harsheys", "Lays", "Cadbury"]
print(lst_1[:])
lst_2 = ['Dairy milk', 'Pringles', 'Kitkat', 'Coka-cola', 'Harsheys', 'Lays', 'Cadbury']
print(lst_2[-1:-3:-1])
lst_3 = ['Dairy milk', 'Pringles', 'Kitkat', 'Coka-cola', 'Harsheys', 'Lays', 'Cadbury']
print(lst_3[2:])
lst_4 = ['Dairy milk', 'Pringles', 'Kitkat', 'Coka-cola', 'Harsheys', 'Lays', 'Cadbury']
print(lst_4[:4])
lst_f = ['Dairy milk', 'Pringles', 'Kitkat', 'Coka-cola', 'Harsheys', 'Lays', 'Cadbury']
print(lst_f[::2])

mlst_0 = ['bubble', 'dopamine', 'array', 'coronel', 'zem', 'lahore']
mlst_0.sort()
print(mlst_0)

mlst_1 = ['bubble', 'dopamine', 'array', 'coronel', 'zem', 'lahore']
mlst_1.insert(2,'mink')
print(mlst_1)

ths_3 = ['orange', 'pineapple', 'strawberry', 'banana']
ths_3.remove('strawberry')
print(ths_3)

klst = ['baseball', 'softball', 'track and field', 'array', 'coronel', 'curling', 'ping pong']
new = klst.index('track and field')
print(new)

my_lst = ['bubble','strawberry', 'dopamine', 'ping pong','coronel', 'zem']
new_lst = my_lst[:]
print(my_lst)

m_lst = ['bubble','strawberry', 'dopamine', 'ping pong','coronel', 'zem']
nw_lst = m_lst[:]
m_lst.insert(2,'scream')
print(nw_lst)

llyst = ['ping pong', 9.0, 'Pringles', 8, 'rain', [1, 3, 5], 'vostok']
for i in llyst:
    print(i)