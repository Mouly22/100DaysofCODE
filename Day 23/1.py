p = ("Julia", "Roberts", 1967, "Duplicity", 2009, "Actress", "Atlanta, Georgia")
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

