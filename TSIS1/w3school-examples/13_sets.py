thisset = {"apple", "banana", "cherry"}
print(thisset) 

print("banana" in thisset) 

thisset.add("apple")
print(thisset)

thisset.remove("apple") # exception if no found
thisset.discard("apple") # no exception
print(thisset)

print([x for x in thisset]) 

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2) # set3 = set1 | set2 # the same
print(set3) # xd, list of int and str can not be sorted, but set can.
