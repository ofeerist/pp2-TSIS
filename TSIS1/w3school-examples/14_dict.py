dict = {
    "Name" : "Artyom",
    "Age" : 18,
    "Id" : "0001"
}
print(dict)

x = dict.keys()
print(x) #before the change
dict["Country"] = "KZ"
print(x) #after the change 

x = dict.values() 
print(x)

print("Name" in dict)

dict.update({
    "Name": "Oleg",
    "Age": 19,
    "Id": "002"
})
print(dict)

dict.pop("Name")
print(dict) 

for x, y in dict.items():
  print(x, y) 

users = {}
id = "u12433211324f"
users[id] = {
  "Name": "ofeerist",
  "Message_count": 1231
}
print(users[id]["Name"])