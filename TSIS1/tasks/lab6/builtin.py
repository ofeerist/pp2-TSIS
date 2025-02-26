import math
import time

# 1
def list_multiply(l):
    return math.prod(l)

# 2
def calculate_string(s):    
    upper = len(list(filter(str.isupper, s)))
    lower = len(list(filter(str.islower, s)))
    return upper, lower

# 3
def is_palindrome(s):
    return s == s[::-1]

# 4
def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  
    return math.sqrt(number)

# 5
def all_true(t):
    return all(t)

print(list_multiply([1,2,3,4,5]))
print(calculate_string("AAvsdsAS"))
print(is_palindrome("aba"))
print(delayed_sqrt(100, 1000))
print(all_true((True, True, False)))