mylist = ["e1", 2, False]
print(mylist, len(mylist))
print(mylist[0])
print(mylist[-1])
print(mylist[:1])
print(mylist[2:])
print(3 in mylist)

mylist[2] = {"Dict": 3}
print(mylist)

mylist.append("temp")
print(mylist)

mylist.insert(3, "temp2")
print(mylist)

mytuple = (True, 0.01, "")
mylist.extend(mytuple)
[print(x) for x in mylist] 

newlist = [x for x in mylist if type(x) is bool]
print(newlist)

thislist = [100, 1, 25, 63, 6]
thislist.sort(reverse=True)
print(thislist)

copy = thislist[:]
print(copy)

print(thislist + copy)