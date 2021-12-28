<h2> List </h2>
A list is a sequential collection of Python data values, where each value is identified by an index. The values that make up a list are called its elements. Lists are similar to strings, which are ordered collections of characters, except that the elements of a list can have any type and for any one list, the items can be of different types.

There are several ways to create a new list. The simplest is to enclose the elements in square brackets[]
```
w = []                                           #empty list
x = [200,400,600,1000]                           #list with integer values
y = ["rock", "paper", "sizer"]                   #string values
z = ["magic", 9.0, 8, [1,3,5]]                   #multiple type values
```
A list can contain multiple datatypes even including a list in a single list.

append function
we can add items at the end of an existing list by using built-in append function.
```
my_li = ["magic", 9.0, 8, [1,3,5]]  
my_li.append("gilmore girls")
print(my_li)
```
Output:
```
['magic', 9.0, 8, [1, 3, 5], 'gilmore girls']```

We can also add multiple list together, this is called list concetenation.
```
li_1 = ['Friends','Atypical','Witcher']
li_2 = ['Meteor garden','love020',"It's okay not to be okay"]
f_li = li_1 + li_2
print(f_li)
```
Output:
```
['Friends', 'Atypical', 'Witcher', 'Meteor garden', 'love020', "It's okay not to be okay"]
```
***Index Operator***

We can access different parts of a list by using index operator, which is denoted by square brackets.
```
s_2 = ['Meteor garden','love020',"It's okay not to be okay"]
com = s_2[0] + " " + "is the best series"
print(com)
```
Output:
```
Meteor garden is the best series
```
Just like string, the numbering of list indexing always starts from zero

***List Slicing***

We can reference a range in a list by using colon notation; this is called slicing.Keep in mind, the ending range doesn't include value in resulting list and slicing doesn't modify the content of original list.

In order to make a change into a specific position of a list,we can use index operator to specify which item we would like to access; then re-assign a value as for that index.

For example,
```
s_li = ['apollo','space shuttle','vostok','soyuz','voskhod']
s_li[3] = 'gemini'
print(s_li)
```
Output:
```
['apollo', 'space shuttle', 'vostok', 'gemini', 'voskhod']
```
#the key difference between string and list -> lists are mutable while string is immutable;meaning strings can't be changed.

***Length of a list***

the len() function takes a list as a parameter and will return an integer indicating the number of items in your list.
```
space_craft = ['apollo','space shuttle','vostok','soyuz','voskhod']
print(len(space_craft))
```
Output:
```
5
```
***Count method***
this method is handy for counting the occurances of a particular item in your list.
```
lst = ["magic", 21, "snowball", [1,3,5], 3, "rain", [2, 4], "snowball", "lili" ]
y =lst.count("snowball")
print(y)
```
Output:
```
2
```



