<h2> Tuple </h2>

A tuple is a sequence of items of ***any type*** and is immutable. So, once we assign values to any variable we can not change them.

The representation of a tuple is a comma-separated sequence of values, enclosed in parentheses(). 
```
n_tup = ('rebert', 2009, [10, 'mango', 2.9], 'rebellion', 'ring')
print(type(n_tup))
```
Output:
```
<class 'tuple'>
```
If we want to declare single value inside a tuple, python might consider it as a normal variable inside parenthesis.
```
val =('julia')
print(type(val))
```
Output:
```
<class 'str'>
```
 How can we sort this?

we have to use a comma before closing the parenthesis. Like this:
```
val = ('julia',)
print(type(val))
```
Output:
```
<class 'tuple'>
```
<h4>Tuple constructor </h4>
We can also declare a tuple using tuple constructor.
For this, we have to declare a tuple using double first parenthesis.

``` tuple(('items',)) ```
```
opps = tuple(('cherry', 'pingpong', 'hockey', 'basket', 'yellow', 'brown'))
print(opps)
print(type(opps))
```
Output:
```
('cherry', 'pingpong', 'hockey', 'basket', 'yellow', 'brown')
<class 'tuple'>
```
<h4>Immutability of Tuple </h4>:
```
n_tup = ('rebert', 2009, [10, 'mango', 2.9], 'rebellion', 'ring')
n_tup[1] = 2010
print(n_tup)
```
Output:
```
TypeError: 'tuple' object does not support item assignment
```
As tuple is immutable, we are not allowed to change/remove any items after assigning them once in a variable.

But, we can ***DELETE*** the whole tuple completely:
```
stup = ('yellow', 'paper', 'daisy')
del stup 
print(stup)
```
Output:
```
NameError: name 'stup' is not defined.
```
In python, immutable objects has a fixed id which is the identity of an object, a location​ in ​memory​.

Items with same values have the same id.
```
e_tup = (25,26,27,25,40)
print(id(e_tup[0]))
print(id(e_tup[3]))
print(id(e_tup[1]))
```
Output:
```
4372317168
4372317168
4372317200
```
<h5>In above output, these values are not constant .Everytime we run the code, items with same value will have same value but the values will be changed everytime we run the code. </h5>

```
e_tup = (25,26,27,25,40)
if id(e_tup[0]) == id(e_tup[2]):
    print("true")
else:
    print("Value assigned in the 4th position will be True. ")
```
Output:
```
Value assigned in the 4th position will be True.
```
<h4>tuple indexing</h4>
```
atup = ('major lazer', 'selena', 'ariana', 2013, 'swift', 'sarika')
print(atup[1])
print(atup(-1))
```
Output:
```
selena
sakira
```
<h4>  Tuple Slicing </h4>
```
char = ('Triyon', 'Jon', 'Jaime', 'Sansa', 'Arya', 'Theon', 'Snow')
print(char[1:6:2])
```
Output:
```
('Jon', 'Sansa', 'Theon')
```
```
char1 = ('Triyon', 'Jon', 'Jaime', 'Sansa', 'Arya', 'Theon', 'Snow')
print(char1[-5:-2])
```
Output:
```
('Jaime', 'Sansa', 'Arya')
```
<h4> Tuple Unpacking </h4>
Although tuples are immutable(unchangable), 
```we can still change the items of a tuple by converting the tuple into a list```
 change the list, and then, convert the list back to the tuple.
