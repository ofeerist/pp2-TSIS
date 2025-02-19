import re

ab = "abbb, abb, aoo, ao, aob, ab, ba"
# 1
# x = re.findall("ab+", ab)

# 2
# x = re.findall("ab{2,3}", ab)

und = "abz_bgd, ADvx_vgfD, nxkl_fdsaaaa, Fdsdf_fdsfsd, kgfdJk_gfdFg"
# 3
# x = re.findall(r'\b[a-z]+_[a-z]+\b', und)

cam = "Artyom, ARtyom, aRtyom, arTyom"
# 4
# x = re.findall(r"^[A-Z][a-z]+", cam)

# 5
# x = re.findall("a.b", ab)

com = "Hello, world."
# 6
# x = re.sub("[ ,.]", ":", com)

snake = "some_variable_in_snake_case"
# 7
# x = re.sub(r"[_]", " ", snake)
# x = re.sub(r"\b[a-z]", lambda m: m.group(0).upper(), x)
# x = re.sub(r"[ ]", "", x)

# 8
# x = re.split(r'[A-Z]', cam)

cas = "CamelCaseExample"
# 9
# x = re.sub("(?=[A-Z])", " ", cas)
# x = re.sub("^[ ]", "", x) # x.strip()

# 10
x = re.sub("(?<!^)(?=[A-Z])", "_", cas) # (?<!^) - negative look behind

print(x)