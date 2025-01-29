def ountogram(gram: float):
    return 28.3495231 * gram
#print(ountogram(100))

def ftoc(F: float):
    return (5 / 9) * (F - 32)
#print(ftoc(100))

def solve(numheads, numlegs):    
    x = (4 * numheads - numlegs) // 2
    y = numheads - x
    
    if x >= 0 and y >= 0 and 2*x + 4*y == numlegs:
        return x, y
    else:
        return "No solution"
#print(solve(35, 94))

def filter_prime(s: str):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    l = s.split(" ")
    return list(filter(lambda x : is_prime(int(x)), l))
#print(filter_prime("1 2 3 4 5 6 7 8 9 10"))

from itertools import permutations
def print_permutations():
    s = input()
    perm_list = permutations(s)
    for perm in perm_list:
        print(''.join(perm))
#print_permutations()

def reverse_input():
    s = input()
    l = s.split(" ")
    l.reverse()
    r = ""
    for e in l:
        r += e + " "
    return r
#print(reverse_input())

def has_33(nums):
    last = 0
    for i in nums:
        if i == last and i == 3:
            return True
        last = i
    return False

#print(has_33([1, 3, 3]))
#print(has_33([1, 3, 1, 3]))
#print(has_33([3, 1, 3]))

def spy_game(nums):
    spy = []
    for i in nums:
        if (i == 0 or i == 7):
            spy.append(i)
    if len(spy) < 3:
        return False
    
    if spy[-3] == 0 and spy[-2] == 0 and spy[-1] == 7:
        return True
    return False

#print(spy_game([1,2,4,0,0,7,5])) 
#print(spy_game([1,0,2,4,0,5,7])) 
#print(spy_game([1,7,2,0,4,5,0])) 

def sphere_volume(radius: float):
    return 4/3 * 3.14 * (radius ** 3)
#print(sphere_volume(2))

def remove_dup(l):
    n = []
    for i in l:
        if i not in n:
            n.append(i)
    return n
#print(remove_dup([1, 2, 1, 2, 3]))

def palindrome(s: str):
    return s == s[::-1]
#print(palindrome("aba"))

def histogram(l):
    for i in l:
        print("*" * i)
#histogram([4, 1, 6, 8])

import random
def game():
    print("Hello! What is your name?")
    name = input()
    target = random.randint(1, 20)
    num = 0
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    while(True):
        num+=1
        print("Take a guess.")
        guess = int(input())
        if (guess < target):
            print("Your guess is too low.")
            continue
        elif guess > target:
            print("Your guess is too high.")
            continue
        else:
            break;
    print(f"Good job, {name}! You guessed my number in {num} guesses!")
#game()