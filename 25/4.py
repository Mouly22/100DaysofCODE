#Write a Python program which will take N names from the user. 
#Create a dictionary from the N names that will hold First_name, Middle_name and Last_name in separate keys.
# The inputs will take N at first and then take N names. 
# You can assume that the names will contain less than or equal 3 words and there will be single space between each part of the name.
#Sample Input:  4
#Zubayer Ahmed
#Sadia Nur Amin
#Mehedi Hasan Shawon
#Nafis

#Sample Output: { "Fname" : [“Zubayer”, “Sadia”, “Mehedi”, “Nafis”] , "Mname" : [“Nur”, “Hasan”], "Lname" : [“Ahmed”, “Amin”, “Shawon”] }

x = int(input("Enter amount: "))

for i in range(x):
    p = input("Names:")

dict = {
    "Fname": p[0], "Mname": p[1], "Lname": p[2]
}
print(dict)

