import json

with open("data.json", "r") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 100)
print("DN" + " " * 40 + "Description" + " " * 20 + "Speed" + " " * 10 + "MTU")
print("-" * 40 + " " + "-" *30 + " " + "-" * 13 + " " + "-" * 13)

for d in data["imdata"]:
    attr = d["l1PhysIf"]["attributes"]
    print(attr["dn"] + " " + attr["descr"] + " " * 30 + attr["speed"] + " " * 10 + attr["mtu"])