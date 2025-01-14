string = "baNaNa"
for x in string:
  print(x)

print(len(string))
print("NaN" in string)
print("nan" not in string)

# slicing
print(string[2:5])

# modify
print(string.replace("a", "_"))
string.replace("_", "a")

# concatenation
print(string + " - bAnAnA")

# format
print(f"My name is {string}, I am {ord(string[0])}")

# escape
print("\t meow meow \n meow")

#methods
print(string.strip())