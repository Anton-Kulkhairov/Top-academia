import random

arr1 = [1, 2, 3, 4, 6, 7, 8]
arr2 = list("asdasdf")
print(arr1,"  ",arr2)
arr3 = [i*i for i in range(1,11) if i % 2 == 0]
print(arr3)
customers = ["Anna", "Sveta", "Kate", "Bob", "Tom", "Joe"]
problemUsers = [i for i in customers if i!= "Tom" and i!="Joe"]
print(customers)
print(problemUsers)
table=[[x*y for x in range (1,4)] for y in range (1,4)]
print(table)
array1 = ["user", 12, 3.14, False, True]
print (array1[-1])
print(len(array1))
print(array1[-4:-2])
print(array1[:-2])
array2 = [1,2,3,4,5]
array3 = ["aba","asdea", "asde", "1adsrr","11bdsrr", "2132rf"]
print(sum(array2))
print(sorted(array3))
array4 = [123,456]
array5 = [678,689, 901]
print(array5+array4)
print(array4)
array4.append("Bob")
print(array4)
array4.insert(0, "Toms")
print(array4)
array4.extend(["ffff","ttt","asdas"])
print(array4)
array4.remove("Toms")
print(array4)
array4.pop(-3)
print(array4)


mystr = "aweqwrf fds fs dfds f"
print(mystr[1])
print(len(mystr))
str1 = mystr.capitalize()
str2 = mystr.title()
print(mystr)
print(str1)
print(str2)
mystr.upper()
mystr.lower()
mystr.swapcase()
print(mystr.count("f",7, -1))

mystr1 = r"TO  TBEERE.... >:" \
		 r"reyreopprok gro" \
		 r" etwywrtewrewr" \
		 r"dgkek gke wkew k"
print(mystr1)
login = input("get Login: ")
message = "You login in system as{}".format(login)
print(message)


