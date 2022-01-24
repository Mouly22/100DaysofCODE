#What will the output be for the following code?
let = "z"
let_two = "p"
c = let_two + let
m = c*5
print(m)
#✔️ Yes, because let_two was put before let, c has "pz" and then that is repeated five times

#Write a program that extracts the last three items in the list sports and assigns it to the variable last. 
#Make sure to write your code so that it works no matter how many items are in the list.
sports = ['cricket', 'football', 'volleyball', 'baseball', 'softball', 'track and field', 'curling', 'ping pong', 'hockey']
last = sports[-3:len(sports):1]
print(last)

#Write code that combines the following variables so that the sentence 
#“You are doing a great job, keep it up!” is assigned to the variable message.
# Do not edit the values assigned to by, az, io, or qy.
by = "You are"
az = "doing a great "
io = "job"
qy = "keep it up!"
message = by +" "+az+io+", "+qy
print(message)

#What is the type of m?
l = ['w', '7', 0, 9]
m = l[1:2]                  #slicing a list returns list
#Output: list

#What is the type of m?
l = ['w', '7', 0, 9]
m = l[1]                    #indexing
#Output: String

#What is the type of x?
b = "My, what a lovely day"
x = b.split(',')             #the .split() method returns a list.
#Output: list

#What is the type of a?
b = "My, what a lovely day"
x = b.split(',')
z = "".join(x)
y = z.split()
a = "".join(y)
#Output:string
