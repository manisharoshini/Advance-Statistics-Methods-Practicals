#  Problems based on binomial distribution

import math 

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def BD(n,p,r):
    return nCr(n,r) * (p**r) * ((1-p)**(n-r))

n = int(input("Enter the number of trials: ")) # Always this in Interger format
p = float(input("Enter the probability of success: ")) # Since the range is between 0 and 1, this is in float format
r = int(input("Enter the number of successes: ")) # always in integer format

print("The probability of", r, "successes in", n, "trials is:", BD(n,p,r))
print("Mean:", n*p)
print("Standard Deviation:", math.sqrt(n*p*(1-p)))