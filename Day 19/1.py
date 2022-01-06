my_dict = {'name':'mouly','age':21}
print(my_dict.get('age'))

#nested dictionary
n_dict ={
    "dict1" : {
        "color":'lavender', 
        "price": 46000
    } ,
    "dict2" : { 
        "color": 'blue' , 
        "price": 20000
    }
}
print(n_dict)
#or
dict1 = {"hero":"peter","name":"flame"}
dict2 = {"hero":"ron", "name":"zeno"}
ndict = {"p" : dict1 , "q" : dict2}      #colon diba mouly, equal sign na
print(ndict)

#my_dict[key] = value
#pop for deleting one particlur item
#clear for removing all items from a dictionary

ndict = { 1 : "ice", 3 : "lemon", 2 : "berry" , "cheese" : 5}
print(ndict.pop("cheese"))      #ei line print dile jei key er value remove hoise oita dekhabe; i mean value ta print kore dekhabe
print(ndict)                    #ei line e kaj ses kore new j dictionary ta aslo oita print kore dekhabe
#print(ndict.clear())            #this one shows none! hehe
#print(ndict)                    #this one shows a empty dictionary
#del ndict                       #if we use del, it deletes the whole dictionary
#print(ndict)
print(ndict.popitem())           #removes an last key:value pair from a dictionary
print(ndict)

#for copying a dictionary,
#mydict = the dictionary i wanna copy.copy()
#by copying like this, it wont be value sharing, it will be address sharing.
#OR, mydict = dict(the dictionary i wanna copy) print(mydict)

#Loop through a dictionary

mydict = {"name": "mini", "age": 20, "major": "english"}
#for i in mydict:
    #print(i, end = " ")              #it prints the keys
    #print(mydict[i], end = " ")      #it prints the values

for x, y in mydict.items():
    print(x, ":", y, end = ", ")       #accessing dictionary items
print()      

#assigning variables in a dictionary with if conditional(1 line)
#The same gets implemented in a simple LC construct in a single line as:
 #[ output_expression() for(set of values to iterate) if(conditional filtering) ]
p = {x: x*x for x in range(10) if x% 2 == 0}
print(p)
 
n = {x : x+x for x in range(5)}
print(n)

#Dictionary Membership Test
# in,not in eisob

mydict = {"name": "mini", "age": 20, "major": "english"}
print(mydict.keys())
print(mydict.items())

#fromkeys --> it actually assigns default value to keys
ndict = {"name":"suicide squad"}.fromkeys(["pactress", "actressname"], "Harley Quinn")
print(ndict)
for x in ndict.items():
    print(x)
print(sorted(ndict))            #sorted keys