dict1 = {}
dict1['name'] ='mouly'
dict1['address'] = 'bogura'
dict1['Age'] = 21
print(dict1)
dict2 = {}
print(dict2)
dict3 = {'saturn': 2, 'moon': 1, 'mars': 'red'}
dict3['moon'] = 'earth'
print(dict3)
y = dict3.get('nila')
print(y)

dict4 = {'nila': 2345, 'mili': 2356, 'mona': 3456}
y = dict4.get('rita')
print(y)

address = {'room':3,'home':4,'street':2}
print(address)
address['room']= address['room']+ 2
print(address)

store = {'bangla' : 3, 'english' : 4, 'german' : 5, 'arabic' : 2}
print(len(store))

dict4 = {'nila': 2345, 'mili': 2356, 'mona': 3456}
for i in dict4:
    print(i)

songs = { 'red':'All Too Well', 1989: 'Style', 'reputation' : 'Gorgeous'}
for i,j in songs.items():
    print(i, j)



