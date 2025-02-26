f = open(r"c:\Users\Артёмка\Documents\pp2\pp2-TSIS\TSIS1\w3school-examples\28_json.py")
print(f.readline())
print(f.readline())
f.close()

f = open("demofile2.txt", "w")
f.write("Now the file has more content!")
f.close()

f = open("demofile2.txt", "r")
print(f.read()) 

import os
if os.path.exists("demofile.txt"):
    pass
#   os.remove("demofile.txt")
else:
  print("The file does not exist") 