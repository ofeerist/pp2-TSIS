def square(n):
    for i in range(n + 1):
        yield i ** 2

print(list(square(5)))

def even(n):
    for i in range(n + 1):
        if (i % 2 == 0):
            yield i

n = int(input())
print(list(even(n)))

def threefour(n):
    for i in range(n + 1):
        if (i % 3 == 0 and i % 4 == 0):
            yield i

print(list(threefour(n)))


def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

print(list(squares(5, 10)))

def ntoz(n):
    for i in range(n + 1):
        yield n - i

print(list(ntoz(10)))