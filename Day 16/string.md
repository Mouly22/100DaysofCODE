Strings are what we use in python when working with words. Strings are either enclosed with single quotes or double quotes.Also we can write multi line string using three qutations(single and double both)
```
my_name = "Hello! I am mouly"
myy_name = 'Helloo! I am Mouly'
x = '''this is
a multi line 
string
that we can write'''
print(my_name)
print(myy_name)
print(x)
```
Output:
```
Hello! I am mouly
Helloo! I am Mouly
this is
a multi line 
string
that we can write
```
We can also make an empty string
```
p = " "
print(p)
```
Output:
```

```
We can concatenate strings by using the plus(+) sign.
```
var1 = "we want"
var2 = "to visit a"
var3 = "zoo"
var =  var1 +" "+ var2 +" "+ var3
print(var)
```
Output:
```
we want to visit a zoo
```
Notice one thing, this + sign doesn't add any space while concatenating.

Strings are sequential collection datatype.This means a string is actually a collection of single characters. 
We can access a sub-string or part of a string using the indexing operator.
This operator is handy for accessing a single character by it's position or ***index value***
This index value for sequential collection datatypes always begins at ***zero***

