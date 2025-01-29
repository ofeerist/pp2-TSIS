def func():
    pass

# Arbitrary Arguments 
def sum(*args):
    sum = 0.0
    for arg in args:
        sum += arg;
    return sum

print(sum(1,2,3,4,5,6))

# Arbitrary Keyword Arguments 
def echo(**args):
    for arg in args:
        print (f"{arg}: {args[arg]}")

echo(Name = "Artyom", Age = 18, Major = "IS")

# Positional-Only Arguments
def vector_len(x, y, /):
  print(pow(x*x + y*y, 0.5))

vector_len(4, 3)

#Keyword-Only Arguments
def my_sort(*, list, reverse = False):
    list.sort(reverse = reverse)
    return list

print(my_sort(list=[1,5,3,4,2], reverse=True))

# Recursion

def fact(n):
   if n == 1:
       return n
   else:
       return n*fact(n-1)

print(fact(5))