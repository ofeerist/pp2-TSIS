import math

deg = float(input("Input degree: "))
print(f"Output radian: {math.radians(deg)}")

def trap(base1, base2, height):
    return 0.5 * (base1 + base2) * height

h = float(input("Height: "))
b1 = float(input("Base, first value: "))
b2 = float(input("Base, second value: "))
print(f"Expected Output: {trap(b1, b2, h)}")

def polygon(n, l):
    return (n * l**2) / (4 * math.tan(math.pi / n))

n = float(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
print(f"The area of the polygon is: {math.floor(polygon(n, l))}")

def paral(base, height):
    return base * height

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))
print(f"Expected Output: {paral(base, height)}")
