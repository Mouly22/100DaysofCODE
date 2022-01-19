p = ("Julia", "Duplicity", 2009, "Actress", "Atlanta",1920,  "Georgia")
print(type(p))

n_tup = ('rebert', 2009, [10, 'mango', 2.9], 'rebellion', 'ring')
print(n_tup)

val =('julia')
print(type(val))
val = ('julia',)
print(type(val))


ex_tup = (25,26,27,25,40)
if id(ex_tup[0]) == id(ex_tup[2]):
    print("true")
else:
    print("Value assigned in the 4th position will be True ")

atup = ('major lazer', 'selena', 'ariana', 2013, 'swift', 'sarika')
s = atup[-1]
print(s)
char = ('Triyon', 'Jon', 'Jaime', 'Sansa', 'Arya', 'Theon', 'Snow')
print(char[-5:-2])

tup =('cherry', 'pingpong', 'hockey') + ('Sansa', 'Arya', 'Theon', 'Snow')
print(tup)
opps = tuple(('cherry', 'pingpong', 'hockey', 'basket', 'yellow', 'brown'))

print(opps)
print(type(opps))


stup = ('yellow', 'paper', 'daisy')
print(stup)

ftup = ('bunny', 'herion', 'fan', 'van')
convert_list = list(ftup) 
convert_list[1] = 'fire'
new_tuple = tuple(convert_list)
print(new_tuple)

stars = ('Sirius', 'Canopus', 'Vega', 'Rigel', 'Procyon')

stars = ('Sirius', 'Canopus', 'Vega', 'Rigel', 'Procyon')
(c, d, a, f, e) = stars
print(d)
print('a:', c, 'b:', d, 'c:', a, 'd:', f, 'e:', e)

tup_1 = ("rain", "fall", "sun", "snow", "wind", "cry")

(one, *two, last) = tup_1

print(two)

l_tup = ("Julia", "Duplicity", 2009, "Actress", "Atlanta",1920,  "Georgia")
for i in l_tup:
    print(i)

t_ttup = ('Jon',300, 'Duplicity', 200, 'Jaime', 1520, 'Sansa')
print(len(t_ttup))

etup = ['pingpong', 'hockey', 'Sansa', 'Arya']
conversion_etup = enumerate(etup)
new_etup = tuple(conversion_etup)
print(new_etup)

nup = ['rain', 'rain', 'go', 'away']
enum = enumerate(nup, 3)
now_tup = tuple(enum)
print(now_tup)

x = ['No', 'matter', 'what', 'you', 'say', ',', 'no', 'matter', 'what', 'you', 'do!']
for i in enumerate(x):
    print(i)


p = ('rain', 'rain', 'go', 'away')
y = p.count('rain')
print(y)

n = (2, 4, 5, 45, 78, 12, 2, 3)
here = n.index(2)
print(here)
