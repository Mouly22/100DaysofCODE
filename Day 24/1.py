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
for i in songs.keys():
    print(i)

songs = { 'red':'All Too Well', 1989: 'Style', 'reputation' : 'Gorgeous'}
for i in songs.values():
    print(i)

songs = { 'red':'All Too Well', 1989: 'Style', 'reputation' : 'Gorgeous'}
y = songs.keys()
songs['folklore'] = 'cardigan'
print(y)

d = {'red':'All Too Well', 1989: 'Style', 'reputation' : 'Gorgeous'}
if 'red' in d:
    print('yup')

name = ['darla','remina','sonam','kiran']
age = [23, 45, 3, 44]
res = dict(zip(name,age))
print(res)

m_zen = { 88017:'rihan', 88015:'kiran', 88018 : ['sonam','riki'], 88013: 'harmeonie', 88016 :{24: 'chinal',26:'sonu'}}
y = m_zen[88016][26]
print(y)







