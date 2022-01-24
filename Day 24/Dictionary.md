A​ ​dictionary is an unordered collection that consists of ​key-value​ pairs. Dictionaries are bounded by curly braces and have a list of ​key: value ​pairs which are separated by comma (,)

```
dict1 = {}
dict1['name'] ='mouly'
dict1['address'] = 'bogura'
dict1['profession'] = 'student'
print(dict1)
```
Output:
```
{'name': 'mouly', 'address': 'bogura', 'profession': 'student'}
```
Here, name, address, profession are keys. ​Keys​ need to be immutable type and keys are case sensitive.

<h4>Empty Dictionary </h4>

```
dict2 = {}
print(dict2)
```
Output:
```
{}
```
<h4> Length of a dictionary </h4>

```
store = {'bangla' : 3, 'english' : 4, 'german' : 5, 'arabic' : 2}
print(len(store))
```
Output:
```
4
```
<h4> Dictionaries are mutable </h4>

Dictionaries are mutable while keys are immutable. So we can change the values of a dictionary.
We can access the values of a dictionary by the ```keys``` nut we can not change the keys.

```
dict3 = {'nila': 2345, 'mili': 2356, 'mona': 3456}
y = dict3['mona']
print(y)
```
Output:
```
3456
```
This is how we can access the value of a specific key of a dictionary. 

We can also get the same value by using get function. The benefit of using get function is that, it does not give an error if we can not find value of a key; rather it gives None as output.
```
dict4 = {'nila': 2345, 'mili': 2356, 'mona': 3456}
y = dict4.get('nila')
print(y)
```
Output:
```
2345
```
```
dict4 = {'nila': 2345, 'mili': 2356, 'mona': 3456}
#x = dict4['rita']                                     #if we print it, it will give a KeyError
y = dict4.get('rita')
print(y)
```
Output:
```
None
```
<h4> changing the value of a dictionary </h4>

```
dictt = {'saturn': 2, 'moon': 1, 'mars': 'red'}
print(dictt)
dictt['moon'] = 'earth'
print(dictt)
```
Output:
```
{'saturn': 2, 'moon': 1, 'mars': 'red'}
{'saturn': 2, 'moon': 'earth', 'mars': 'red'}
```
```
address = {'room':3,'home':4,'street':2}
print(address)
address['room']= address['room']+ 2
print(address)
```
Output:
```
{'room': 3, 'home': 4, 'street': 2}
{'room': 5, 'home': 4, 'street': 2}
```
Here we can see how we the change value of a key of a dictionary.

<h4> Looping through a dictionary </h4>

```
songs = { 'red':'All Too Well', 1989: 'Style', 'reputation' : 'Gorgeous'}
for i in songs.keys():
    print(i)
```
Output:
```
red
1989
reputation
```
```
songs = { 'red':'All Too Well', 1989: 'Style', 'reputation' : 'Gorgeous'}
for i in songs.values():
    print(i)
```
Output:
```
All Too Well
Style
Gorgeous
```
```
songs = { 'red':'All Too Well', 1989: 'Style', 'reputation' : 'Gorgeous'}
for i in songs.values():
    print(i)
```
Output:
```
All Too Well
Style
Gorgeous
```
```
songs = { 'red':'All Too Well', 1989: 'Style', 'reputation' : 'Gorgeous'}
for i,j in songs.items():
    print(i, j)
```
Output:
```
red All Too Well
1989 Style
reputation Gorgeous
```
<h4>If I update a dictionary, then the updated list of keys will be displayed.</h4>

```
songs = { 'red':'All Too Well', 1989: 'Style', 'reputation' : 'Gorgeous'}
y = songs.keys()
songs['folklore'] = 'cardigan'
print(y)
```
Output:
```
dict_keys(['red', 1989, 'reputation', 'folklore'])
```


