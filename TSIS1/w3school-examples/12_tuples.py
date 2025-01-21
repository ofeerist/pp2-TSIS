thistuple = ("apple", "banana", "cherry")
print(thistuple)

y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

(e1, e2) = thistuple
print(e1, e2)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3) 