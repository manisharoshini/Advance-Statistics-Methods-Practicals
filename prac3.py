# Property plotting of binomial distribution

import math
import matplotlib.pyplot as plt

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def BD(n,p,r):
    return nCr(n,r) * (p**r) * ((1-p)**(n-r)) # p-1 = q

n = int(input("Enter the number of trials: ")) # Always this in Interger format
p = float(input("Enter the probability of success: ")) # Since the range is between
r = int(input("Enter the number of successes: ")) # always in integer format

print("Binomial Distribution:", BD(n, p, r))
print(BD(n,p,r)*100, " % chance")
print("Mean:", n*p)
print("Standard Deviation:", math.sqrt(n*p*p-1))

plt.bar(r, BD(n,p,r))

#git add .
#git commit -m "first commit"
#git push -u origin main